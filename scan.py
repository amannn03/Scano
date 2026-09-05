import subprocess


SCAN_TYPES = {
    "1": ("Basic Scan", ["-F"]),
    "2": ("Service Scan", ["-sV"]),
    "3": ("Full Port Scan", ["-p-"]),
    "4": ("UDP Scan", ["-sU", "--top-ports", "100"]),
    "5": ("OS Detection", ["-O"]),
    "6": ("Detailed Scan", ["-sT", "-sV", "-O","-p-"]),
    "7": ("Vulnerability Scan", ["--script", "vuln"]),
    "8": ("Network Discovery", ["-sn"]),
}


def run_scan(target, choice):
    """Run Nmap scan and return the output."""

    if choice in SCAN_TYPES:
        name, arguments = SCAN_TYPES[choice]
        arguments = arguments.copy()

    elif choice == "9":
        name = "Port Scan"

        ports = input("Enter ports (e.g. 22,80,443): ").strip()

        if not ports:
            return "[!] No ports specified."

        arguments = ["-p", ports]

    elif choice == "10":
        name = "Custom Scan"

        custom_options = input(
            "Enter scan options (e.g. -sS -O): "
        ).strip()

        if not custom_options:
            return "[!] No Nmap options specified."

        arguments = custom_options.split()

    else:
        return "[!] Invalid scan choice."

    command = ["nmap", *arguments, target]

    print(f"\n[+] Starting {name}...")
    print(f"[+] Command: {' '.join(command)}")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode != 0:
            return f"\n[!] Nmap Error:\n{result.stderr.strip()}"

        return result.stdout

    except FileNotFoundError:
        return "[!] Nmap is not installed or not found in PATH."

    except PermissionError:
        return "[!] Permission denied while running Nmap."

    except Exception as error:
        return f"[!] Unexpected error: {error}"