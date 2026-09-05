def display_result(target, result):
    """Display parsed Nmap results in a beginner-friendly format."""

    print("\n" + "=" * 50)
    print("                 SCAN RESULT")
    print("=" * 50)

    # Target information
    print(f"\nTarget: {target}")

    # Host status
    if result["host_status"] == "up":
        print("Status: ONLINE")
    elif result["host_status"] == "down":
        print("Status: OFFLINE")
    else:
        print("Status: UNKNOWN")

    # Port information
    ports = result["ports"]

    print(f"\nOpen Ports: {len(ports)}")

    if not ports:
        print("\nNo open ports found.")
        return

    print("-" * 50)

    for port in ports:
        print(f"\nPort: {port['port']}/{port['protocol']}")
        print(f"State: {port['state']}")
        print(f"Service: {port['service']}")

        if port["version"]:
            print(f"Version: {port['version']}")

        print(f"Meaning: {get_service_meaning(port['service'])}")


def get_service_meaning(service):
    """Return a beginner-friendly explanation of a service."""

    meanings = {
        "ssh": "Remote administration service.",
        "http": "Web server used for websites.",
        "https": "Secure web server used for websites.",
        "ftp": "File transfer service.",
        "smtp": "Used for sending emails.",
        "dns": "Translates domain names into IP addresses.",
        "mysql": "Database server.",
        "postgresql": "PostgreSQL database server.",
        "rdp": "Remote desktop service.",
        "telnet": "Remote login service. It is not encrypted.",
    }

    return meanings.get(
        service.lower(),
        "A network service running on this port."
    )