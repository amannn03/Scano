from scan import run_scan
from filter import parse_nmap_output
from result import display_result


def show_scan_menu():
    """Display the scan menu and return the user's choice."""

    print("\n" + "=" * 50)
    print("                 SCAN MENU")
    print("=" * 50)

    print("1) Basic Scan        -- Host + Common Ports")
    print("2) Service Scan      -- Services + Versions")
    print("3) Full Port Scan    -- All TCP Ports")
    print("4) UDP Scan          -- Common UDP Ports")
    print("5) OS Detection      -- OS + Device Info")
    print("6) Detailed Scan     -- Ports + Services + OS")
    print("7) Vulnerability     -- Security Checks")
    print("8) Network Discovery -- Find Live Hosts")
    print("9) Port Scan         -- Selected Ports")
    print("10) Custom Scan      -- Custom Nmap Options")
    print("0) Exit")

    print("=" * 50)

    return input("\nSelect scan: ").strip()


def main():
    print("\n" + "=" * 50)
    print("              Starting Scano")
    print("=" * 50)

    target = input("Enter target IP address: ").strip()

    choice = show_scan_menu()

    if choice == "0":
        print("\nGoodbye!")
        return

    # Run selected scan
    raw_result = run_scan(target, choice)

    # Check for errors
    if raw_result.startswith("[!]"):
        print(raw_result)
        return

    # Filter Nmap output
    filtered_result = parse_nmap_output(raw_result)

    # Get scan name
    scan_name = {
        "1": "Basic Scan",
        "2": "Service Scan",
        "3": "Full Port Scan",
        "4": "UDP Scan",
        "5": "OS Detection",
        "6": "Detailed Scan",
        "7": "Vulnerability Scan",
        "8": "Network Discovery",
        "9": "Port Scan",
        "10": "Custom Scan"
    }.get(choice, "Scan")

    # Display formatted result
    display_result(target, filtered_result, scan_name)


if __name__ == "__main__":
    main()