from settings import get_settings

settings = get_settings()

bind = "0.0.0.0:8080"
worker_class = "uvicorn.workers.UvicornWorker"
workers = 2
loglevel = "info"
accesslog = "-"
proc_name = "UYUNPUNION"
daemon = True
