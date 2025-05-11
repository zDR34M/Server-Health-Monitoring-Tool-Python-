import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")

if cpu > 80:
    print("⚠️ High CPU usage!")
if memory > 80:
    print("⚠️ High Memory usage!")
if disk > 80:
    print("⚠️ High Disk usage!")
