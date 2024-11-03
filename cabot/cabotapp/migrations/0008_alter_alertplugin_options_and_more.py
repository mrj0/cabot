# Generated by Django 5.1.2 on 2024-11-03 22:17

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabotapp', '0001_initial_squashed_0007_statuscheckresult_consecutive_failures'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alertplugin',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='graphitestatuscheck',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='httpstatuscheck',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='icmpstatuscheck',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='jenkinsstatuscheck',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='statuscheck',
            options={'base_manager_name': 'objects', 'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='alertplugin',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='alertpluginuserdata',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='address',
            field=models.TextField(blank=True, help_text='Address (IP/Hostname) of service.'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='alerts',
            field=models.ManyToManyField(blank=True, help_text='Alerts channels through which you wish to be notified', to='cabotapp.alertplugin'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='alerts_enabled',
            field=models.BooleanField(default=True, help_text='Alert when this service is not healthy.'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='hackpad_id',
            field=models.TextField(blank=True, help_text='Gist, Hackpad or Refheap js embed with recovery instructions e.g. https://you.hackpad.com/some_document.js', null=True, verbose_name='Embedded recovery instructions'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='old_overall_status',
            field=models.TextField(default='PASSING'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='overall_status',
            field=models.TextField(default='PASSING'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='runbook_link',
            field=models.TextField(blank=True, help_text='Link to the service runbook on your wiki.'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='status_checks',
            field=models.ManyToManyField(blank=True, help_text='Checks used to calculate service status.', to='cabotapp.statuscheck'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='telephone_alert',
            field=models.BooleanField(default=False, help_text='Must be enabled, and check importance set to Critical, to receive telephone alerts.'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='users_to_notify',
            field=models.ManyToManyField(blank=True, help_text='Users who should receive alerts.', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instancestatussnapshot',
            name='overall_status',
            field=models.TextField(default='PASSING'),
        ),
        migrations.AlterField(
            model_name='service',
            name='alerts',
            field=models.ManyToManyField(blank=True, help_text='Alerts channels through which you wish to be notified', to='cabotapp.alertplugin'),
        ),
        migrations.AlterField(
            model_name='service',
            name='alerts_enabled',
            field=models.BooleanField(default=True, help_text='Alert when this service is not healthy.'),
        ),
        migrations.AlterField(
            model_name='service',
            name='hackpad_id',
            field=models.TextField(blank=True, help_text='Gist, Hackpad or Refheap js embed with recovery instructions e.g. https://you.hackpad.com/some_document.js', null=True, verbose_name='Embedded recovery instructions'),
        ),
        migrations.AlterField(
            model_name='service',
            name='instances',
            field=models.ManyToManyField(blank=True, help_text='Instances this service is running on.', to='cabotapp.instance'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_public',
            field=models.BooleanField(default=False, help_text='The service will be shown in the public home', verbose_name='Is Public'),
        ),
        migrations.AlterField(
            model_name='service',
            name='old_overall_status',
            field=models.TextField(default='PASSING'),
        ),
        migrations.AlterField(
            model_name='service',
            name='overall_status',
            field=models.TextField(default='PASSING'),
        ),
        migrations.AlterField(
            model_name='service',
            name='runbook_link',
            field=models.TextField(blank=True, help_text='Link to the service runbook on your wiki.'),
        ),
        migrations.AlterField(
            model_name='service',
            name='status_checks',
            field=models.ManyToManyField(blank=True, help_text='Checks used to calculate service status.', to='cabotapp.statuscheck'),
        ),
        migrations.AlterField(
            model_name='service',
            name='telephone_alert',
            field=models.BooleanField(default=False, help_text='Must be enabled, and check importance set to Critical, to receive telephone alerts.'),
        ),
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.TextField(blank=True, help_text='URL of service.'),
        ),
        migrations.AlterField(
            model_name='service',
            name='users_to_notify',
            field=models.ManyToManyField(blank=True, help_text='Users who should receive alerts.', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicestatussnapshot',
            name='overall_status',
            field=models.TextField(default='PASSING'),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='active',
            field=models.BooleanField(default=True, help_text='If not active, check will not be used to calculate service status and will not trigger alerts.'),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='allowed_num_failures',
            field=models.IntegerField(default=0, help_text='The maximum number of data series (metrics) you expect to fail. For example, you might be OK with 2 out of 3 webservers having OK load (1 failing), but not 1 out of 3 (2 failing).', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='calculated_status',
            field=models.CharField(blank=True, choices=[('passing', 'passing'), ('intermittent', 'intermittent'), ('failing', 'failing')], default='passing', max_length=50),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='check_type',
            field=models.CharField(choices=[('>', 'Greater than'), ('>=', 'Greater than or equal'), ('<', 'Less than'), ('<=', 'Less than or equal'), ('==', 'Equal to')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='debounce',
            field=models.IntegerField(default=0, help_text='Number of successive failures permitted before check will be marked as failed. Default is 0, i.e. fail on first failure.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='endpoint',
            field=models.TextField(help_text='HTTP(S) endpoint to poll.', null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='expected_num_hosts',
            field=models.IntegerField(default=0, help_text='The minimum number of data series (hosts) you expect to see.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='frequency',
            field=models.IntegerField(default=5, help_text='Minutes between each check.'),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='importance',
            field=models.CharField(choices=[('WARNING', 'Warning'), ('ERROR', 'Error'), ('CRITICAL', 'Critical')], default='ERROR', help_text='Severity level of a failure. Critical alerts are for failures you want to wake you up at 2am, Errors are things you can sleep through but need to fix in the morning, and warnings for less important things.', max_length=30),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='max_queued_build_time',
            field=models.IntegerField(blank=True, help_text='Alert if build queued for more than this many minutes.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='metric',
            field=models.TextField(help_text='fully.qualified.name of the Graphite metric you want to watch. This can be any valid Graphite expression, including wildcards, multiple hosts, etc.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='password',
            field=models.TextField(blank=True, help_text='Basic auth password.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='status_code',
            field=models.TextField(default=200, help_text='Status code expected from endpoint.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='text_match',
            field=models.TextField(blank=True, help_text='Regex to match against source of page.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='timeout',
            field=models.IntegerField(default=30, help_text='Time out after this many seconds.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='username',
            field=models.TextField(blank=True, help_text='Basic auth username.', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='value',
            field=models.TextField(help_text='If this expression evaluates to true, the check will fail (possibly triggering an alert).', null=True),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='verify_ssl_certificate',
            field=models.BooleanField(default=True, help_text='Set to false to allow not try to verify ssl certificates (default True)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hipchat_alias',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddIndex(
            model_name='statuscheckresult',
            index=models.Index(fields=['status_check', 'time_complete'], name='cabotapp_st_status__154201_idx'),
        ),
        migrations.AddIndex(
            model_name='statuscheckresult',
            index=models.Index(fields=['status_check', 'id'], name='cabotapp_st_status__d0483c_idx'),
        ),
    ]
