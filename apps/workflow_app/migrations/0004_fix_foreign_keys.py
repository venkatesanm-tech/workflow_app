# Generated migration to fix foreign key issues

from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('workflow_app', '0003_auto_20250918_0940'),
    ]

    operations = [
        # Drop existing foreign key constraints
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflow DROP FOREIGN KEY workflow_app_workflo_created_by_id_b04e8d7d_fk_system_t_;",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowexecution DROP FOREIGN KEY workflow_app_workflo_triggered_by_user_i_7c8b9e2a_fk_system_t_;",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowvariable DROP FOREIGN KEY workflow_app_workflo_created_by_id_8f5a2c1d_fk_system_t_;",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowtemplate DROP FOREIGN KEY workflow_app_workflo_created_by_id_9a6b3d4e_fk_system_t_;",
            reverse_sql="-- No reverse SQL needed"
        ),
        
        # Modify columns to use VARCHAR instead of UUID for foreign keys
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflow MODIFY COLUMN created_by_id VARCHAR(36) NOT NULL;",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowexecution MODIFY COLUMN triggered_by_user_id VARCHAR(36) NULL;",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowvariable MODIFY COLUMN created_by_id VARCHAR(36) NOT NULL;",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowtemplate MODIFY COLUMN created_by_id VARCHAR(36) NOT NULL;",
            reverse_sql="-- No reverse SQL needed"
        ),
        
        # Re-add foreign key constraints
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflow ADD CONSTRAINT workflow_app_workflow_created_by_id_fk FOREIGN KEY (created_by_id) REFERENCES system_user(id);",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowexecution ADD CONSTRAINT workflow_app_workflowexecution_triggered_by_user_id_fk FOREIGN KEY (triggered_by_user_id) REFERENCES system_user(id);",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowvariable ADD CONSTRAINT workflow_app_workflowvariable_created_by_id_fk FOREIGN KEY (created_by_id) REFERENCES system_user(id);",
            reverse_sql="-- No reverse SQL needed"
        ),
        migrations.RunSQL(
            "ALTER TABLE workflow_app_workflowtemplate ADD CONSTRAINT workflow_app_workflowtemplate_created_by_id_fk FOREIGN KEY (created_by_id) REFERENCES system_user(id);",
            reverse_sql="-- No reverse SQL needed"
        ),
    ]