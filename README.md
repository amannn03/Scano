# Scano 🛡️

A simple, beginner-friendly network scanner built with **Nmap** and **Python**. It lets you run common Nmap scans through an easy interactive menu, then shows the results in a clean, readable format — and optionally saves them to a file.

No need to memorize Nmap commands — just pick a number from the menu and Scano does the rest!

---

## ✨ Features

- **10 built-in scan options** — from a quick basic scan to full vulnerability checks
- **Interactive menu** — choose a scan by typing a number
- **Clean results** — sees through raw Nmap output and shows only what matters (open ports, services, OS info)
- **Save your results** — export to `.txt` or `.html` files
- **Beginner friendly** — no Nmap experience needed to get started

---

## 📋 Requirements

Before you can run Scano, you need:

1. **Python 3** (any recent version)
2. **Nmap** installed on your system

### Install Nmap

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt install nmap
  ```
- **Linux (Fedora):**
  ```bash
  sudo dnf install nmap
  ```
- **macOS (Homebrew):**
  ```bash
  brew install nmap
  ```
- **Windows:** Download the installer from [nmap.org](https://nmap.org/download.html)

> 💡 To run most Nmap scans you'll need **root/administrator privileges**, otherwise you may hit permission errors.

---

## 🚀 How to Run

From the project folder, run:

```bash
python main.py
```

That's it! Follow the on-screen prompts.

---

## 🕹️ Using Scano

When you run the program, you'll be asked for three things:

### 1. Target IP address
The computer or device you want to scan, e.g. `192.168.1.10`. You can also use a hostname like `example.com`.

> ⚠️ **Only scan devices you own or have permission to scan.**

### 2. Save result? (y/n)
Type `y` to save the output to a file. You'll then choose:
- **Format:** `txt` or `html`
- **File path:** where to save it, e.g. `result.txt`

### 3. Select a scan

| Option | Description |
|--------|-------------|
| `1` **Basic Scan** | Host + common ports — quick overview |
| `2` **Service Scan** | What services are running + versions |
| `3` **Full Port Scan** | Every TCP port (slowest) |
| `4` **UDP Scan** | Common UDP ports |
| `5` **OS Detection** | Operating system + device info |
| `6` **Detailed Scan** | Ports + services + OS in one go |
| `7` **Vulnerability** | Security checks for known issues |
| `8` **Network Discovery** | Find live hosts on the network |
| `9` **Port Scan** | Scan ports you choose (e.g. `22,80,443`) |
| `10` **Custom Scan** | Type your own Nmap options |
| `0` **Exit** | Close the program |

Type the number and press **Enter**. Scano runs the scan, shows you the results, and (if you chose to) saves them to your file.

---

## 📁 Project Structure

```
Scano/
├── main.py      # Entry point — the menu and program flow
├── scan.py      # Runs the Nmap command for each scan type
├── filter.py    # Turns raw Nmap output into clean, readable data
├── result.py    # Formats and prints the results nicely
└── README.md    # README.md file
```
---

## 🔧 Troubleshooting

1. **Nmap not installed** — install Nmap from the [Requirements](#-requirements) section above.
2. **Permission denied** — run with `sudo`:
   ```bash
   sudo python main.py
   ```

## 🔒 Legal & Ethical Warning

Scano is a **network security tool**. Use it **only** on devices, servers, and networks that you own or have **explicit permission** to test. Unauthorized scanning is illegal in many places and can get you into serious trouble.

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.
