import re


def parse_nmap_output(output):
    """Parse Nmap output and return structured scan data."""

    result = {
        "host_status": "unknown",
        "ports": []
    }

    # Check host status
    if "Host is up" in output:
        result["host_status"] = "up"

    elif "Host seems down" in output:
        result["host_status"] = "down"

    # Match Nmap port lines
    pattern = re.compile(
        r"^(\d+)/(tcp|udp)\s+(\w+)\s+(\S+)(?:\s+(.*))?$"
    )

    for line in output.splitlines():

        line = line.strip()

        match = pattern.match(line)

        if not match:
            continue

        port, protocol, state, service, version = match.groups()

        result["ports"].append({
            "port": int(port),
            "protocol": protocol,
            "state": state,
            "service": service,
            "version": version.strip() if version else ""
        })

    return result