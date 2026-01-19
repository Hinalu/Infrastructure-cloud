from flask import Flask, render_template
from datetime import datetime

# Task Pf3: Custom Microservice
# Displays the specific "Skills Test" homepage required by Task 3

app = Flask(__name__)

@app.route("/")
def home():
    # Get current date and time for the requirement
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", current_time=now)

if __name__ == "__main__":
    # Runs on port 5050 as requested in the Docker task
    app.run(host="0.0.0.0", port=5050)