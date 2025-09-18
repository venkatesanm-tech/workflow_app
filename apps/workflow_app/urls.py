from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

# Create router for API endpoints
router = DefaultRouter()
router.register(r'node-types', api_views.NodeTypeViewSet, basename='nodetype')
router.register(r'workflows', api_views.WorkflowViewSet, basename='workflow')
router.register(r'executions', api_views.WorkflowExecutionViewSet, basename='execution')
router.register(r'variables', api_views.WorkflowVariableViewSet, basename='variable')
router.register(r'webhooks', api_views.WorkflowWebhookViewSet, basename='webhook')
router.register(r'templates', api_views.WorkflowTemplateViewSet, basename='template')

app_name = 'workflow_app'

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    
    # Additional API endpoints
    path('api/dashboard/stats/', api_views.dashboard_stats_api, name='dashboard_stats'),
    path('api/dashboard/recent-activity/', api_views.recent_activity_api, name='recent_activity'),
    path('api/executions/<uuid:execution_id>/logs/', api_views.execution_logs_api, name='execution_logs'),
    path('api/workflows/<uuid:workflow_id>/test/', api_views.test_workflow_api, name='test_workflow'),
    
    # Legacy API endpoints for compatibility
    path('api/workflow/', views.workflow_api, name='workflow_api'),
    path('api/workflows/<uuid:workflow_id>/execute/', views.execute_workflow_api, name='execute_workflow_api'),
    path('api/executions/<uuid:execution_id>/', views.execution_status_api, name='execution_status_api'),
    
    # Editor views
    path('', views.workflow_list_view, name='workflow_list'),
    path('create/', views.workflow_editor_view, name='workflow_create'),
    path('<uuid:workflow_id>/edit/', views.workflow_editor_view, name='workflow_edit'),
    path('<uuid:workflow_id>/', views.workflow_detail_view, name='workflow_detail'),
    
    # Webhook receiver
    path('webhook/<str:endpoint_path>/', views.webhook_receiver, name='webhook_receiver'),
    
    # Management views
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('templates/', views.template_list_view, name='template_list'),
    path('templates/create/', views.template_create_view, name='template_create'),
    path('templates/<uuid:template_id>/', views.template_detail_view, name='template_detail'),
    path('templates/<uuid:template_id>/edit/', views.template_edit_view, name='template_edit'),
    path('executions/', views.execution_list_view, name='execution_list'),
]
