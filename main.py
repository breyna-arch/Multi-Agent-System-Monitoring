from agents.system_data_agent import SystemDataAgent
from agents.anomaly_agent import AnomalyAgent
from agents.report_agent import ReportAgent
import time

def main():
    data_agent = SystemDataAgent()
    anomaly_agent = AnomalyAgent()
    report_agent = ReportAgent()

    print("SystemMonitoring AI Monitoring Active...")
    while True:
        metrics = data_agent.collect_metrics()
        alerts = anomaly_agent.analyze(metrics)

        print(f"\n[{metrics['timestamp']}]")
        print(f"CPU: {metrics['cpu_percent']}% | MEM: {metrics['memory_percent']}% | DISK: {metrics['disk_percent']}%")
        for alert in alerts:
            print(alert)

        summary = report_agent.generate_report(metrics, alerts)
        print("\nAI Summary:")
        print(summary)

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()

