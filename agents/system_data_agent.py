import psutil
import time

class SystemDataAgent:
    """Collects real-time system metrics such as CPU, memory, and disk usage."""

    def __init__(self):
        self.name = "SystemDataAgent"

    def collect_metrics(self):
        """Collects basic system statistics."""
        metrics = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "net_sent_mb": psutil.net_io_counters().bytes_sent / (1024 * 1024),
            "net_recv_mb": psutil.net_io_counters().bytes_recv / (1024 * 1024)
        }
        return metrics
