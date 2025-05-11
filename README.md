# 🖥️ Server Health Monitoring Tool (Python)

A lightweight Python tool to monitor your server's **CPU**, **Memory**, and **Disk usage** in real time. Designed for automation on Linux systems using `cron`, this tool helps detect performance issues early and logs alerts for further analysis.

---

## 📌 Features

- ✅ Monitors CPU, RAM, and Disk usage
- ⚠️ Displays warnings when thresholds are exceeded
- 📝 Logs alerts to a log file
- 🔁 Can run automatically every 5 minutes using cron
- 💡 Written entirely in Python using `psutil`

---

## 🧰 Technologies Used

- Python 3
- psutil
- Ubuntu Linux (cron for scheduling)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/zDR34M/server-monitor.git
cd server-monitor
```

### 2. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 3. Run the Script Manually
```bash
python3 monitor.py
```

---

## ⏰ Automate with Cron (Linux)

To run the script every 5 minutes:

1. Open the crontab editor:
```bash
crontab -e
```

2. Add this line (update the path):
```
*/5 * * * * /usr/bin/python3 /home/yourusername/server-monitor/monitor.py >> /home/yourusername/server-monitor/monitor.log 2>&1
```

---

## 📄 Example Output

```
CPU Usage: 23.4%
Memory Usage: 58.2%
Disk Usage: 67.9%
```

If any metric exceeds 80%:

```
⚠️ High CPU usage!
⚠️ High Memory usage!
```

---

## 🔧 Future Improvements

- Add email or Slack notifications
- Monitor multiple remote servers via SSH
- Build a simple web dashboard (Flask)
- Use YAML/JSON config file for thresholds

---

## 📂 Project Structure

```
server-monitor/
├── monitor.py           # Main script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore
```

---

## 👨‍💻 Author

**Tareq Suliman**  
📧 tareq.cr07@gmail.com  
🌍 [LinkedIn Profile](https://www.linkedin.com/in/tareq-suliman/)

---

## 📄 License

This project is open-source and available under the MIT License.
