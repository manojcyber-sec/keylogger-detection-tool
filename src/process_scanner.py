import psutil
import datetime
import os

# Keywords often used by keyloggers
SUSPICIOUS_KEYWORDS = [
    "pynput",
    "keyboard",
    "keylogger",
    "hook"
]

# Trusted system processes (ignore these)
TRUSTED_PROCESSES = [
    "python.exe",
    "cmd.exe",
    "explorer.exe",
    "svchost.exe",
    "chrome.exe",
    "msedge.exe",
    "system",
    "registry"
]


def scan_processes():
    """
    Scan all running processes
    """
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes


def log_detection(process):
    """
    Save suspicious process info to log file
    """

    os.makedirs("logs", exist_ok=True)

    log_file = "logs/detection_log.txt"

    with open(log_file, "a") as f:

        f.write("\n[ALERT] Suspicious process detected\n")
        f.write(f"PID: {process['pid']}\n")
        f.write(f"Name: {process['name']}\n")
        f.write(f"Path: {process['exe']}\n")
        f.write(f"Time: {datetime.datetime.now()}\n")
        f.write("-----------------------------\n")


def detect_suspicious(processes):
    """
    Detect suspicious processes
    """

    suspicious = []

    for process in processes:

        name = str(process.get("name", "")).lower()
        exe = str(process.get("exe", "")).lower()
        cmdline_list = process.get("cmdline") or []
        cmdline = " ".join(cmdline_list).lower()

        # Ignore trusted processes
        if name in TRUSTED_PROCESSES:
            continue

        # Ignore this scanner itself
        if "process_scanner.py" in cmdline:
            continue

        if "dashboard/app.py" in cmdline:
            continue

        # Check suspicious keywords
        for keyword in SUSPICIOUS_KEYWORDS:

            if keyword in name or keyword in exe or keyword in cmdline:

                suspicious.append(process)

                log_detection(process)

                break

    return suspicious


def main():

    print("🔍 Scanning running processes...")
    print("----------------------------------")

    processes = scan_processes()

    suspicious_processes = detect_suspicious(processes)

    if suspicious_processes:

        print("\n⚠ Suspicious Processes Detected:\n")

        for proc in suspicious_processes:

            print(f"PID: {proc['pid']}")
            print(f"Name: {proc['name']}")
            print(f"Path: {proc['exe']}")
            print("-----------------------------")

    else:

        print("\n✅ No suspicious processes detected.")


if __name__ == "__main__":
    main()