import multiprocessing
import os

workers = multiprocessing.cpu_count() * 2 + 1
threads = workers

port = int(os.environ.get("PORT", 8000))

bind = f"0.0.0.0:{port}"
env = "DJANGO_SETTINGS_MODULE=gestotus.settings"
loglevel = "debug"
accesslog = "gunicorn.access"
errorlog = "gunicorn.error"
chdir = "/app"
capture_output = True