import os
from datetime import datetime
from openai import OpenAI
from config import Config

class ReportAgent:
    """Generates and logs natural-language summaries of system health."""

    def __init__(self, log_path="reports/system_report.log"):
        self.name = "ReportAgent"
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def generate_report(self, metrics, alerts):
        alert_text = "\n".join(alerts)
        prompt = f"""
        You are a system monitoring assistant. 
        Based on the following data, write a 2-4 sentence summary describing the system health, noting any problems, and giving suggestions.

        System metrics:
        - CPU: {metrics['cpu_percent']}%
        - Memory: {metrics['memory_percent']}%
        - Disk: {metrics['disk_percent']}%
        - Network sent: {metrics['net_sent_mb']:.2f} MB
        - Network received: {metrics['net_recv_mb']:.2f} MB

        Alerts:
        {alert_text}
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert systems monitoring assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
        )

        summary = response.choices[0].message.content.strip()

        # Log the result
        self._log_summary(metrics, summary)
        return summary

    def _log_summary(self, metrics, summary):
        """Appends each report to a log file with timestamp."""
        with open(self.log_path, "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
            f.write(f"CPU: {metrics['cpu_percent']}% | MEM: {metrics['memory_percent']}% | DISK: {metrics['disk_percent']}%\n")
            f.write(summary + "\n\n")

