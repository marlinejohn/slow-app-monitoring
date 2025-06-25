from flask import Flask
import time
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import start_http_server

app = Flask(__name__)

# Gauge to track in-flight requests
in_flight_requests = Gauge('myapp_pending_requests', 'Number of in-flight requests')

@app.route("/work")
def work():
    in_flight_requests.inc()
    time.sleep(6)
    in_flight_requests.dec()
    return "Done", 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

