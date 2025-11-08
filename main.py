import sqlite3
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import os

DB_NAME = "log.db"

# TODO: Define your bonus features here
# Example 1: Calculate how many times CPU > 80%
# Example 2: Send alert email if CPU > 90%
# Example 3: Generate text summary report with top 3 CPU peaks

def load_data():
    if not os.path.exists(DB_NAME):
        print("Database not found. Please ensure log.db exists.")
        return None
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM system_log", conn)
    conn.close()
    return df

def count_high_cpu(df):
    # TODO: Count entries with CPU usage above threshold
    pass

def generate_summary(df):
    # TODO: Generate text-based summary (average, max, etc.)
    pass

def send_email_alert(message):
    # TODO: Send a test email (optional)
    # Hint: use smtplib or just print to console for simulation
    pass

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        # TODO: Call your custom features
        pass
