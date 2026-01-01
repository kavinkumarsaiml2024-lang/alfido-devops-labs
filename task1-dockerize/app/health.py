import psutil

def health_check():
    return {
        "cpu_ok": psutil.cpu_percent() < 85,
        "memory_ok": psutil.virtual_memory().percent < 85,
        "disk_ok": psutil.disk_usage("/").percent < 90,
        "status": "healthy"
    }
