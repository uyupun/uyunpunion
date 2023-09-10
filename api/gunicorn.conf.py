import os

from dotenv import load_dotenv

load_dotenv()

address = os.getenv("ADDRESS", "0.0.0.0")
port = os.getenv("PORT", "8080")

bind = f"{address}:{port}"
worker_class = "uvicorn.workers.UvicornWorker"
workers = 2
loglevel = "info"
accesslog = "-"
pidfile = "gunicorn.pid"
proc_name = "UYUNPUNION"
daemon = os.getenv("DAEMON", "false").lower() == "true"
