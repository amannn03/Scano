import re


def parse_nmap_output(output):
    result = {
        "status": "ONLINE" if "Host is up" in output else "OFFLINE",
        "hostname": "",
        "ports": [],
        "os": "",
        "device": "",
        "distance": "",
        "warnings": []
    }

    # Hostname
    match = re.search(r"Nmap scan report for (.+)", output)
    if match:
        result["hostname"] = match.group(1).strip()

    # Ports
    for line in output.splitlines():
        match = re.match(
            r"(\d+)/(tcp|udp)\s+(\S+)\s+(\S+)(?:\s+(.*))?",
            line.strip()
        )

        if match:
            port, protocol, state, service, version = match.groups()

            result["ports"].append({
                "port": port,
                "protocol": protocol,
                "state": state,
                "service": service,
                "version": version or ""
            })

    # OS
    match = re.search(r"OS details:\s*(.+)", output)
    if match:
        result["os"] = match.group(1).strip()

    match = re.search(r"Device type:\s*(.+)", output)
    if match:
        result["device"] = match.group(1).strip()

    # Network distance
    match = re.search(r"Network Distance:\s*(.+)", output)
    if match:
        result["distance"] = match.group(1).strip()

    # Warnings
    for line in output.splitlines():
        if "Warning:" in line or "Too many fingerprints" in line:
            result["warnings"].append(line.strip())

    return result