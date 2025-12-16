from flask import Flask, jsonify, render_template_string, request
import socket
import datetime
import platform
import time

app = Flask(__name__)

request_count = 0  # per-instance request counter

HTML_TEMPLATE = """
<!doctype html>
<html>
  <head>
    <title>System Status Dashboard</title>
  </head>
  <body>
    <h1>System Status Dashboard</h1>
    <p>This request was served by: <b>{{ hostname }}</b></p>
    <p>Server time: {{ server_time }}</p>
    <p>Operating system: {{ os_info }}</p>
    <p>Requests handled by this instance: <b>{{ request_count }}</b></p>
    <hr>
    <p>Health check endpoint: <code>/health</code></p>
    <p>JSON status endpoint: <code>/status</code></p>
    <p>CPU load test endpoint: <code>/load?seconds=5</code></p>
  </body>
</html>
"""

def get_basic_info():
    hostname = socket.gethostname()
    server_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    os_info = f"{platform.system()} {platform.release()}"
    return hostname, server_time, os_info

@app.route("/")
def home():
    global request_count
    request_count += 1

    hostname, server_time, os_info = get_basic_info()

    return render_template_string(
        HTML_TEMPLATE,
        hostname=hostname,
        server_time=server_time,
        os_info=os_info,
        request_count=request_count,
    )

@app.route("/status")
def status():
    hostname, server_time, os_info = get_basic_info()

    data = {
        "hostname": hostname,
        "server_time": server_time,
        "os": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
        },
        "request_count": request_count,
    }
    return jsonify(data), 200

@app.route("/health")
def health():
    #Simple health check endpoint for the load balancer
    return "OK", 200

@app.route("/load")
def load():
    """Artificially generate CPU load for a few seconds to trigger scaling."""
    try:
        seconds = float(request.args.get("seconds", "5"))
    except ValueError:
        seconds = 5.0

    end_time = time.time() + seconds
    while time.time() < end_time:
        pass

    return f"CPU load generated for {seconds} seconds on {socket.gethostname()}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
