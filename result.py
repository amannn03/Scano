def build_output(target, result, scan_name):
    """Build the exact terminal output as a string."""
    lines = [
        "",
        "=" * 50,
        f"              {scan_name.upper()}",
        "=" * 50,
        f"\nTarget: {target}",
        f"Status: {result['status']}",
    ]

    if result["hostname"]:
        lines.append(f"Hostname: {result['hostname']}")

    if result["os"] or result["device"]:
        lines.append("\n[ OS INFORMATION ]")
        if result["os"]:
            lines.append(f"OS: {result['os']}")
        if result["device"]:
            lines.append(f"Device: {result['device']}")

    lines.append("\n[ PORTS ]")
    lines.append(f"Found: {len(result['ports'])}")

    if result["ports"]:
        for p in result["ports"]:
            lines.append(
                f"{p['port']}/{p['protocol']}  "
                f"{p['state']}  "
                f"{p['service']}  "
                f"{p['version']}"
            )
    else:
        lines.append("No open ports found.")

    if result["distance"]:
        lines.append(f"\nNetwork Distance: {result['distance']}")

    if result["warnings"]:
        lines.append("\n[ WARNING ]")
        for warning in result["warnings"]:
            lines.append(warning)

    lines.append("\n" + "=" * 50)
    return "\n".join(lines)


def display_result(target, result, scan_name):
    """Print the result and return the output as a string."""
    output = build_output(target, result, scan_name)
    print(output)
    return output