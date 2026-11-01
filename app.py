import time, math, random
from flask import Flask, jsonify, render_template

app = Flask(__name__)
START = time.time()
LAT0, LON0 = 25.2048, 55.2708

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/telemetry")
def telemetry():
    t = int(time.time() - START)
    return jsonify({
        "t": t,
        "alt": round(min(100, t * 5), 1),
        "speed": round(12 + random.uniform(-1, 1), 1),
        "lat": round(LAT0 + 0.0005 * math.sin(t / 20), 5),
        "lon": round(LON0 + 0.0005 * math.cos(t / 20), 5),
        "battery": round(max(0, 100 - 0.2 * t), 1),
        "temp": round(30 + t * 0.05 + random.uniform(-0.5, 0.5), 1),
        "link": "OK" if random.random() > 0.05 else "LOST",
    })

if __name__ == "__main__":
    app.run(debug=True)
