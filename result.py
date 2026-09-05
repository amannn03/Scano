def display_result(target, result, scan_name):

    print("\n" + "=" * 50)
    print(f"              {scan_name.upper()}")
    print("=" * 50)

    print(f"\nTarget: {target}")
    print(f"Status: {result['status']}")

    if result["hostname"]:
        print(f"Hostname: {result['hostname']}")

    # OS information
    if result["os"] or result["device"]:
        print("\n[ OS INFORMATION ]")

        if result["os"]:
            print(f"OS: {result['os']}")

        if result["device"]:
            print(f"Device: {result['device']}")

    # Ports
    print(f"\n[ PORTS ]")
    print(f"Found: {len(result['ports'])}")

    if result["ports"]:
        for p in result["ports"]:
            print(
                f"{p['port']}/{p['protocol']}  "
                f"{p['state']}  "
                f"{p['service']}  "
                f"{p['version']}"
            )
    else:
        print("No open ports found.")

    # Network
    if result["distance"]:
        print(f"\nNetwork Distance: {result['distance']}")

    # Warnings
    if result["warnings"]:
        print("\n[ WARNING ]")
        for warning in result["warnings"]:
            print(warning)

    print("\n" + "=" * 50)