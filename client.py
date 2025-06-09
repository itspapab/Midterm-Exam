# client.py
import socket

# Server details
HOST = '127.0.0.1'  # This should match the server's IP address
PORT = 65432        # This must match the server's listening port

def start_client():
    try:
        # Create socket using IPv4 and TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))  # Connect to the server
            print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

            # Send a message
            message = input("[CLIENT] Enter message to send: ")
            client_socket.sendall(message.encode())

            # Receive a response
            response = client_socket.recv(1024)
            print(f"[CLIENT] Server responded: {response.decode()}")

    except ConnectionRefusedError:
        print("[CLIENT ERROR] Connection refused. Is the server running?")
    except Exception as e:
        print(f"[CLIENT ERROR] {e}")

if __name__ == "__main__":
    start_client()
