import socket

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 5303)
    while True:
        domain = input("Enter domainname: ")
        sock.sendto(domain.encode(), server_address)
        response, _ = sock.recvfrom(1024)
        print("Response:", response.decode())
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != 'y':
            break
    sock.close()

run_client()
