import os
from datetime import datetime, timedelta
from openai import OpenAI

def read_logs_in_range(log_path, hours=1):
    """Reads all log entries within the last `hours` from system_report.log."""
    if not os.path.exists(log_path):
        return "No log data available yet."

    cutoff = datetime.now() - timedelta(hours=hours)
    collected = []

    with open(log_path, "r") as f:
        current_entry = []
        for line in f:
            if line.startswith("[") and "]" in line:
                # New log entry found
                timestamp_str = line.strip()[1:20]
                try:
                    ts = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    if ts >= cutoff:
                        if current_entry:
                            collected.append("".join(current_entry))
                        current_entry = [line]
                except ValueError:
                    pass
            else:
                current_entry.append(line)

        if current_entry:
            collected.append("".join(current_entry))

    return "\n".join(collected) if collected else "No recent log entries found."

def summarize_logs_with_ai(log_path, hours=1):
    """Generates a summary of recent logs using the OpenAI API."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    recent_logs = read_logs_in_range(log_path, hours)

    prompt = f"""
    Summarize the system's health based on the following logs from the last {hours} hour(s).
    Highlight performance trends, issues, and general stability.

    Logs:
    {recent_logs}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior system operations analyst."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=250,
    )

    return response.choices[0].message.content.strip()
