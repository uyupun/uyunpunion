bind = "0.0.0.0:8081"
worker_class = "uvicorn.workers.UvicornWorker"
workers = 2
loglevel = "info"
accesslog = "-"
pidfile = "gunicorn.pid"
proc_name = "UYUNPUNION"
daemon = True
