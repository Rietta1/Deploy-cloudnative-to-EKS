import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_momory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU or Memory Utilization detected. Please scale up"
    return f"CPU Utilization: {cpu_percent} and Memory Utilization: {mem_percent}"

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')