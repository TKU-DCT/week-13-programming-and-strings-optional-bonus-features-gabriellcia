import sqlite3
import pandas as pd
import smtplib
from email.mime.text import MIMEText   # ← ini yang benar
import os

DB_NAME = "log.db"

# BONUS FEATURES:
# 1. Hitung berapa kali CPU > 80%
# 2. Buat ringkasan teks (avg, min, max, top 3 CPU)
# 3. Simulasi email alert kalau CPU > 90%
# 4. Simpan ringkasan ke file teks


def load_data():
    """Load data dari database ke DataFrame pandas."""
    if not os.path.exists(DB_NAME):
        print("Database not found. Please ensure log.db exists.")
        return None

    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM system_log", conn)
    conn.close()
    return df


def count_high_cpu(df, threshold=80):
    """Hitung berapa banyak baris dengan CPU > threshold."""
    if "cpu" not in df.columns:
        print("Column 'cpu' not found in system_log table.")
        return 0

    count = (df["cpu"] > threshold).sum()
    return int(count)


def generate_summary(df):
    """
    Generate text-based summary:
    - avg / min / max CPU, MEM, DISK
    - top 3 CPU peaks (dengan timestamp kalau ada)
    """
    lines = []
    lines.append("SYSTEM SUMMARY")
    lines.append("--------------")
    lines.append(f"Total log entries: {len(df)}")
    lines.append("")

    # CPU
    if "cpu" in df.columns:
        lines.append("CPU usage (%)")
        lines.append(
            f"  Avg: {df['cpu'].mean():.2f}, "
            f"Min: {df['cpu'].min():.2f}, "
            f"Max: {df['cpu'].max():.2f}"
        )

        # Top 3 peaks
        top3 = df.sort_values("cpu", ascending=False).head(3)
        lines.append("  Top 3 CPU peaks:")
        for _, row in top3.iterrows():
            if "timestamp" in df.columns:
                lines.append(f"    - {row['timestamp']} -> {row['cpu']:.2f}%")
            else:
                lines.append(f"    - CPU: {row['cpu']:.2f}%")
        lines.append("")

    # Memory
    if "mem" in df.columns:
        lines.append("Memory usage (%)")
        lines.append(
            f"  Avg: {df['mem'].mean():.2f}, "
            f"Min: {df['mem'].min():.2f}, "
            f"Max: {df['mem'].max():.2f}"
        )
        lines.append("")

    # Disk
    if "disk" in df.columns:
        lines.append("Disk usage (%)")
        lines.append(
            f"  Avg: {df['disk'].mean():.2f}, "
            f"Min: {df['disk'].min():.2f}, "
            f"Max: {df['disk'].max():.2f}"
        )
        lines.append("")

    return "\n".join(lines)


def send_email_alert(message):
    """
    Simulasi kirim email alert.
    Untuk tugas ini cukup print ke console sebagai 'fake email'.
    """
    print("\n=== EMAIL ALERT (SIMULATION) ===")
    print("To: admin@example.com")
    print("Subject: ⚠️ High CPU Alert")
    print("")
    print(message)
    print("=== END OF EMAIL ===\n")

    # Contoh kode kalau mau kirim email beneran (TIDAK dipakai di tugas):
    #
    # sender = "youremail@example.com"
    # receiver = "admin@example.com"
    # msg = MIMEText(message)
    # msg["Subject"] = "High CPU Alert"
    # msg["From"] = sender
    # msg["To"] = receiver
    #
    # with smtplib.SMTP("smtp.example.com", 587) as server:
    #     server.starttls()
    #     server.login("USERNAME", "PASSWORD")
    #     server.send_message(msg)


def save_summary_to_file(summary_text, filename="system_summary.txt"):
    """Simpan ringkasan ke file teks."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary_text)
    print(f"Summary saved to {filename}")


if __name__ == "__main__":
    df = load_data()

    if df is not None:
        # Tambahkan 1 baris log palsu agar CPU > 90% untuk simulasi alert
        if {"timestamp", "cpu", "mem", "disk"}.issubset(df.columns):
            df.loc[len(df)] = {
                "timestamp": "2025-12-10 12:00",
                "cpu": 95,
                "mem": 70,
                "disk": 50,
            }

        # 1) Hitung berapa kali CPU > 80%
        high_cpu_count = count_high_cpu(df, threshold=80)
        print(f"CPU usage exceeded 80% a total of {high_cpu_count} times.\n")

        # 2) Generate text-based summary
        summary = generate_summary(df)
        print(summary)

        # 3) Simpan summary ke file
        save_summary_to_file(summary)

        # 4) Simulasi email alert jika CPU > 90%
        if "cpu" in df.columns and df["cpu"].max() > 90:
            max_cpu = df["cpu"].max()
            email_msg = (
                "Alert! CPU usage exceeded 90%.\n"
                f"Maximum recorded CPU usage: {max_cpu:.2f}%."
            )
            send_email_alert(email_msg)
        else:
            print("\nNo CPU value above 90%. No alert email simulated.")
