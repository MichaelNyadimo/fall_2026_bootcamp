import sys
from pathlib import Path

def scan_log_file():
    if len(sys.argv) < 2:
        print("Missing log file path.")
        return

    log_path = Path(sys.argv[1])

    if not log_path.exists():
        print(f"Log file not found: {log_path}")
        return

    error_count = 0
    warn_count = 0
    critical_count = 0

    with log_path.open("r") as file:
        for line in file:
            if "CRITICAL" in line:
                critical_count += 1
            elif "ERROR" in line:
                error_count += 1
