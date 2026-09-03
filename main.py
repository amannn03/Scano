from scan import run_scan


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

    result = run_scan(target, choice)

    print("\n" + "=" * 50)
    print("                 SCAN RESULT")
    print("=" * 50)

    print(result)


if __name__ == "__main__":
    main()