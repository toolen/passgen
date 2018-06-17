.. _settings

Settings
==========

CORS
-----------------

You can disable CORS by environment variable::

   PASSGEN_CORS_ENABLED=False


Gunicorn
-----------------

Gunicorn settings can be specified by using environment variable GUNICORN_CMD_ARGS. All available command line arguments can be used. For example, to specify the bind address and number of workers::

   GUNICORN_CMD_ARGS="--bind=127.0.0.1:8080 --workers=3"
