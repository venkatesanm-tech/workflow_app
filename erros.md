Page not found (404)
Request Method:	POST
Request URL:	http://127.0.0.1:8000/workflow/api/workflows/
Using the URLconf defined in system.urls, Django tried these URL patterns, in this order:

admin/
createtoken/ [name='token_obtain_pair']
refreshtoken/ [name='token_refresh']
generatekey/
getjwtusingtoken/ [name='get_jwt']
web_app_login/
log/
web_app_logout/
checksession/
forgotpassword/
reset_link/
resetpassword/
test/
cronjob
query_builder/
menu/
query
api/
[name='workflow_list']
create/ [name='workflow_create']
<uuid:workflow_id>/edit/ [name='workflow_edit']
<uuid:workflow_id>/ [name='workflow_detail']
webhook/<str:endpoint_path>/ [name='webhook_receiver']
dashboard/ [name='dashboard']
templates/ [name='template_list']
templates/create/ [name='template_create']
templates/<uuid:template_id>/ [name='template_detail']
templates/<uuid:template_id>/edit/ [name='template_edit']
executions/ [name='execution_list']
query/
^uploads/(?P<path>.*)$
api/schema/ [name='schema']
api/schema/swagger-ui/ [name='swagger-ui']
api/schema/redoc/ [name='redoc']
__debug__/
^static/(?P<path>.*)$
The current path, workflow/api/workflows/, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.

Hide »
 History
/workflow/api/workflows/
 Versions
Django 3.2.25
 Time
CPU: 46.38ms (50.51ms)
 Settings
 Headers
 Request
<no view>
 SQL
0 queries in 0.00ms
 Static files
0 files used
 Templates
 Cache
0 calls in 0.00ms
 Signals
50 receivers of 15 signals
 Logging
0 messages

Intercept redirects

Profiling
DJDT
×
History
×
Versions
×
Time
×
Settings from system.settings.development
×
Headers
×
Request
×
SQL queries from 0 connections
×
Static files (186 found, 0 used)
×
Templates (1 rendered)
×
Cache calls from 1 backend
×
Signals
×
Log messages
 python manage.py migrate
/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/models/base.py:321: RuntimeWarning: Model 'system.query' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/models/base.py:321: RuntimeWarning: Model 'system.log' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/models/base.py:321: RuntimeWarning: Model 'shared.paymentmaster' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
System check identified some issues:

WARNINGS:
?: (debug_toolbar.staticfiles.W001) debug_toolbar requires the STATICFILES_DIRS directories to exist.
        HINT: Running manage.py collectstatic may help uncover the issue.
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
        HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, django_celery_beat, django_celery_results, menu, sessions, shared, system, test1, workflow_app
Running migrations:
  Applying workflow_app.0001_initial...Traceback (most recent call last):
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/mysql/base.py", line 73, in execute
    return self.cursor.execute(query, args)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/cursors.py", line 148, in execute
    result = self._query(query)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/cursors.py", line 310, in _query
    conn.query(q)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 548, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 775, in _read_query_result
    result.read()
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 1156, in read
    first_packet = self.connection._read_packet()
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 725, in _read_packet
    packet.raise_for_error()
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/protocol.py", line 221, in raise_for_error
    err.raise_mysql_exception(self._data)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/err.py", line 143, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.OperationalError: (3780, "Referencing column 'created_by_id' and referenced column 'id' in foreign key constraint 'workflow_app_workflo_created_by_id_b04e8d7d_fk_system_t_' are incompatible.")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/core/management/base.py", line 398, in execute
    output = self.handle(*args, **options)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/core/management/base.py", line 89, in wrapped
    res = handle_func(*args, **kwargs)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/core/management/commands/migrate.py", line 244, in handle
    post_migrate_state = executor.migrate(
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 117, in migrate
    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 147, in _migrate_all_forwards
    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 230, in apply_migration
    migration_recorded = True
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 118, in __exit__
    self.execute(sql)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 145, in execute
    cursor.execute(sql, params)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 98, in execute
    return super().execute(sql, params)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 66, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 75, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/backends/mysql/base.py", line 73, in execute
    return self.cursor.execute(query, args)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/cursors.py", line 148, in execute
    result = self._query(query)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/cursors.py", line 310, in _query
    conn.query(q)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 548, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 775, in _read_query_result
    result.read()
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 1156, in read
    first_packet = self.connection._read_packet()
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/connections.py", line 725, in _read_packet
    packet.raise_for_error()
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/protocol.py", line 221, in raise_for_error
    err.raise_mysql_exception(self._data)
  File "/var/www/html/GRM/venv/lib/python3.8/site-packages/pymysql/err.py", line 143, in raise_mysql_exception
    raise errorclass(errno, errval)
django.db.utils.OperationalError: (3780, "Referencing column 'created_by_id' and referenced column 'id' in foreign key constraint 'workflow_app_workflo_created_by_id_b04e8d7d_fk_system_t_' are incompatible.")
(venv) venkatesan.m@ISS-L-086:/var/www/html/GRM$ python manage.py setup_node_types
/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/models/base.py:321: RuntimeWarning: Model 'system.query' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/models/base.py:321: RuntimeWarning: Model 'system.log' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
/var/www/html/GRM/venv/lib/python3.8/site-packages/django/db/models/base.py:321: RuntimeWarning: Model 'shared.paymentmaster' was already registered. Reloading models is not advised as it can lead to inconsistencies, most notably with related models.
  new_class._meta.apps.register_model(new_class._meta.app_label, new_class)
System check identified some issues:

WARNINGS:
?: (debug_toolbar.staticfiles.W001) debug_toolbar requires the STATICFILES_DIRS directories to exist.
        HINT: Running manage.py collectstatic may help uncover the issue.
Created node type: Webhook
Created node type: Schedule
Created node type: Manual
Created node type: HTTP Request
Created node type: Database Query
Created node type: Advanced Query Builder
Created node type: Transform Data
Created node type: JSON Parser
Created node type: Condition
Created node type: Switch
Created node type: Send Email
Created node type: Slack Notification
Created node type: Delay
Created node type: Save to Database
Created node type: Export to File
Created node type: Send Webhook
Created node type: Write File
Created node type: Log Message
Created node type: Execute Command
Created node type: HTTP Response
Successfully set up node types: 20 created, 0 updated
(venv) venkatesan.m@ISS-L-086:/var/www/html/GRM$ 