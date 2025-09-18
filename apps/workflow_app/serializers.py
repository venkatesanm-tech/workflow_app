from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    NodeType, Workflow, WorkflowExecution, NodeExecution,
    WorkflowWebhook, WorkflowSchedule, WorkflowTemplate, WorkflowVariable
)

User = get_user_model()

class NodeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeType
        fields = [
            'id', 'name', 'display_name', 'category', 'description',
            'icon', 'color', 'config_schema', 'handler_class', 'is_active'
        ]
        read_only_fields = ['id']

class WorkflowVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowVariable
        fields = [
            'id', 'name', 'value', 'scope', 'description', 
            'is_encrypted', 'is_secret', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']
        extra_kwargs = {
            'value': {'write_only': True}  # Don't expose secret values
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Hide secret values in API responses
        if instance.is_secret:
            data['value'] = '***HIDDEN***'
        return data

class WorkflowSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    shared_with_names = serializers.StringRelatedField(source='shared_with', many=True, read_only=True)
    variables = WorkflowVariableSerializer(many=True, read_only=True)
    execution_count = serializers.SerializerMethodField()
    last_execution_status = serializers.SerializerMethodField()

    class Meta:
        model = Workflow
        fields = [
            'id', 'name', 'description', 'status', 'version', 'definition',
            'timeout_seconds', 'max_retries', 'retry_delay_seconds',
            'is_scheduled', 'cron_expression', 'timezone', 'tags',
            'created_by', 'created_by_name', 'shared_with', 'shared_with_names',
            'variables', 'execution_count', 'last_execution_status',
            'created_at', 'updated_at', 'last_executed_at'
        ]
        read_only_fields = ['id', 'created_by', 'version', 'created_at', 'updated_at', 'last_executed_at']

    def get_execution_count(self, obj):
        return obj.executions.count()

    def get_last_execution_status(self, obj):
        last_execution = obj.executions.first()
        return last_execution.status if last_execution else None

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Increment version on definition changes
        if 'definition' in validated_data and validated_data['definition'] != instance.definition:
            instance.version += 1
        return super().update(instance, validated_data)

class NodeExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeExecution
        fields = [
            'id', 'node_id', 'node_type', 'node_name', 'status',
            'execution_order', 'started_at', 'finished_at', 'duration_ms',
            'input_data', 'output_data', 'error_message', 'error_details'
        ]
        read_only_fields = ['id']

class WorkflowExecutionSerializer(serializers.ModelSerializer):
    workflow_name = serializers.CharField(source='workflow.name', read_only=True)
    triggered_by_username = serializers.CharField(source='triggered_by_user.username', read_only=True)
    node_executions = NodeExecutionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkflowExecution
        fields = [
            'id', 'workflow', 'workflow_name', 'status', 'triggered_by',
            'triggered_by_user', 'triggered_by_username', 'started_at',
            'finished_at', 'duration_seconds', 'input_data', 'output_data',
            'error_message', 'error_details', 'node_executions'
        ]
        read_only_fields = ['id', 'started_at', 'finished_at', 'duration_seconds']

class WorkflowWebhookSerializer(serializers.ModelSerializer):
    workflow_name = serializers.CharField(source='workflow.name', read_only=True)

    class Meta:
        model = WorkflowWebhook
        fields = [
            'id', 'workflow', 'workflow_name', 'name', 'endpoint_path',
            'http_method', 'is_active', 'require_auth', 'api_key',
            'allowed_ips', 'request_timeout', 'max_payload_size',
            'created_at', 'last_triggered_at', 'trigger_count'
        ]
        read_only_fields = ['id', 'created_at', 'last_triggered_at', 'trigger_count']

class WorkflowScheduleSerializer(serializers.ModelSerializer):
    workflow_name = serializers.CharField(source='workflow.name', read_only=True)

    class Meta:
        model = WorkflowSchedule
        fields = [
            'id', 'workflow', 'workflow_name', 'is_active', 'cron_expression',
            'timezone', 'max_executions', 'execution_count', 'start_date',
            'end_date', 'created_at', 'last_executed_at', 'next_execution_at'
        ]
        read_only_fields = ['id', 'created_at', 'last_executed_at', 'execution_count']

class WorkflowTemplateSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = WorkflowTemplate
        fields = [
            'id', 'name', 'description', 'category', 'template_definition',
            'is_public', 'created_by', 'created_by_name', 'created_at',
            'usage_count', 'tags'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'usage_count']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

# Specialized serializers for different operations
class WorkflowExecuteSerializer(serializers.Serializer):
    input_data = serializers.JSONField(default=dict, required=False)
    sync = serializers.BooleanField(default=False, required=False)
    test_mode = serializers.BooleanField(default=False, required=False)

class WorkflowImportSerializer(serializers.Serializer):
    workflow_data = serializers.JSONField()
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)

class WorkflowExportSerializer(serializers.Serializer):
    include_executions = serializers.BooleanField(default=False)
    include_variables = serializers.BooleanField(default=False)

class NodeValidationSerializer(serializers.Serializer):
    node_type = serializers.CharField()
    config = serializers.JSONField()

    def validate(self, data):
        node_type_name = data['node_type']
        config = data['config']
        
        try:
            node_type = NodeType.objects.get(name=node_type_name, is_active=True)
        except NodeType.DoesNotExist:
            raise serializers.ValidationError(f"Node type '{node_type_name}' not found")
        
        # Validate config against schema
        schema = node_type.config_schema
        if schema and 'fields' in schema:
            required_fields = [f['name'] for f in schema['fields'] if f.get('required', False)]
            for field_name in required_fields:
                if field_name not in config:
                    raise serializers.ValidationError(f"Required field '{field_name}' is missing")
        
        return data
