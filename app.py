# import nonexistent_module_xyz 
from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

IST = ZoneInfo("Asia/Kolkata")

def get_ist_time():
    return datetime.now(IST).strftime("%d-%m-%Y %H:%M:%S IST")

DB_PASS = "admin@123"

@app.route("/")
def home():
    current_time = get_ist_time()
    return f"""
    <html>
        <head>
            <title>Python Web App</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding-top: 100px;
                }}
                .container {{
                    background: white;
                    width: 500px;
                    margin: auto;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
                }}
                h1 {{
                    color: #2c3e50;
                }}
                p {{
                    font-size: 20px;
                    color: #27ae60;
                }}
                .timestamp {{
                    font-size: 14px;
                    color: #7f8c8d;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello GSPANN From DSSP Portal</h1>
                <p>Pipeline Test Successful</p>
                <div class="timestamp">Deployed at: {current_time}</div>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "UP",
        "timestamp": get_ist_time()
    }

if __name__ == "__main__":
    print(f"[LOG] Flask App Started at {get_ist_time()}")
    app.run(host="0.0.0.0", port=5000)
