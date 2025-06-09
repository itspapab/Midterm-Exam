# port_scanner.py
import socket
from datetime import datetime

def scan_ports(host, start_port, end_port):
    print(f"[*] Starting scan on host: {host}")
    print(f"[*] Scanning ports {start_port} to {end_port}")
    start_time = datetime.now()

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Half-second timeout
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"[OPEN] Port {port} is open")
                # else:
                #     print(f"[CLOSED] Port {port} is closed")  # Uncomment if you want to show closed ports

    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved.")
    except socket.error:
        print("[ERROR] Couldn't connect to server.")
    except Exception as e:
        print(f"[ERROR] {e}")

    end_time = datetime.now()
    print(f"\n[*] Scan completed in: {end_time - start_time}")

if __name__ == "__main__":
    target = input("Enter target host (e.g., 127.0.0.1 or scanme.nmap.org): ")
    try:
        start = int(input("Enter start port (e.g., 20): "))
        end = int(input("Enter end port (e.g., 100): "))
        if start > end:
            raise ValueError("Start port must be less than or equal to end port.")
        scan_ports(target, start, end)
    except ValueError as ve:
        print(f"[INPUT ERROR] {ve}")
