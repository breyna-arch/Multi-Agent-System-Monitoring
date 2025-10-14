class AnomalyAgent:
    """Analyzes system metrics to detect potential issues or high loads."""

    def __init__(self):
        self.name = "AnomalyAgent"

    def analyze(self, metrics):
        alerts = []

        if metrics["cpu_percent"] > 85:
            alerts.append(f"High CPU usage detected: {metrics['cpu_percent']}%")
        if metrics["memory_percent"] > 85:
            alerts.append(f"Memory usage critically high: {metrics['memory_percent']}%")
        if metrics["disk_percent"] > 90:
            alerts.append(f"Disk usage nearly full: {metrics['disk_percent']}%")
        
        if not alerts:
            alerts.append("System is operating normally.")
        
        return alerts

