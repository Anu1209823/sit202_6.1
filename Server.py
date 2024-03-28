import socket

DNS = {
    "google.com": {"type": "A", "value": "193.178.0.2"},
    "www.google.com": {"type": "CNAME", "value": "google.com"}
}

def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#for tcp SOCK_STREAM, IF_INET6
    sock.bind(('localhost', 5303))
    print("DNS Server is running...")
    while True:
        try:
            data, client_address = sock.recvfrom(1024)
            domain = data.decode().strip()
            if domain in DNS:
                record = DNS[domain]
                response = f"Domain: {domain} Type: {record['type']} Value: {record['value']}"
                sock.sendto(response.encode(), client_address)
                print(f"Response Sent to {client_address}: {response}")
            else:
                error_response = "Error: Hostname not found. Please enter a valid hostname."
                sock.sendto(error_response.encode(), client_address)
                print(f"Error Response Sent to {client_address}: {error_response}")
        except Exception as e:
            print("An error occurred:", e)

run_server()
