from flask import Flask, render_template
from agents.system_data_agent import SystemDataAgent
from agents.anomaly_agent import AnomalyAgent
from agents.report_agent import ReportAgent
from utils.summary_utils import summarize_logs_with_ai

app = Flask(__name__)

data_agent = SystemDataAgent()
anomaly_agent = AnomalyAgent()
report_agent = ReportAgent()

@app.route("/")
def dashboard():
    metrics = data_agent.collect_metrics()
    alerts = anomaly_agent.analyze(metrics)
    summary = report_agent.generate_report(metrics, alerts)
    hourly_summary = summarize_logs_with_ai("reports/system_report.log", hours=1)

    return render_template("dashboard.html", 
                           metrics=metrics,
                           alerts=alerts,
                           summary=summary,
                           hourly_summary=hourly_summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
