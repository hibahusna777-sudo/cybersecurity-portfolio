import socket

target = input("Enter target IP or hostname: ")

common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]

print(f"\nScanning {target}...\n")

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    if sock.connect_ex((target, port)) == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()

print("\nScan completed.")
