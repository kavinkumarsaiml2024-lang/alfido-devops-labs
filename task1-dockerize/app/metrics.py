import psutil
import platform

def collect_metrics():
    return {
        "os": platform.platform(),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage("/").percent,
        "load_average": psutil.getloadavg()
    }
