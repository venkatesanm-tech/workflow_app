# Generated migration to fix user model references

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('workflow_app', '0004_fix_foreign_keys'),
    ]

    operations = [
        # Update the foreign key fields to reference the correct user model
        migrations.AlterField(
            model_name='workflow',
            name='created_by',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='workflows',
                to='system.User'
            ),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='shared_with',
            field=models.ManyToManyField(
                blank=True,
                related_name='shared_workflows',
                to='system.User'
            ),
        ),
        migrations.AlterField(
            model_name='workflowexecution',
            name='triggered_by_user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='system.User'
            ),
        ),
        migrations.AlterField(
            model_name='workflowvariable',
            name='created_by',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='system.User'
            ),
        ),
        migrations.AlterField(
            model_name='workflowtemplate',
            name='created_by',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='system.User'
            ),
        ),
    ]