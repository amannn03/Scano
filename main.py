from scan import run_scan
from filter import parse_nmap_output
from result import display_result


def write_result_file(output, file_format, file_path):
    """Save the exact terminal output to a txt or html file."""
    if file_format == "html":
        output = (
            "<!DOCTYPE html>\n"
            "<html lang=\"en\">\n"
            "<head><meta charset=\"UTF-8\"><title>Scano Result</title></head>\n"
            "<body><pre>\n"
            f"{output}\n"
            "</pre></body>\n"
            "</html>\n"
        )

    with open(file_path, "w") as file:
        file.write(output)


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

    # Ask about saving result
    save_result = input("Do you want to save the result? (y/n): ").strip().lower()

    file_format = None
    file_path = None

    if save_result == "y":

        file_format = input("Save as (txt/html): ").strip().lower()

        while file_format not in ("txt", "html"):
            print("[!] Please enter either txt or html.")
            file_format = input("Save as (txt/html): ").strip().lower()

        file_path = input("Enter file path: ").strip()

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

    # Display formatted result and get the exact terminal output
    output = display_result(target, filtered_result, scan_name)

    # Save exact terminal output
    if save_result == "y":
        write_result_file(output, file_format, file_path)
        print(f"\n[+] Result saved to: {file_path}")


if __name__ == "__main__":
    main()