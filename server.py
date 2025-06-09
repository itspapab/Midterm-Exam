# server.py
import socket

# Set up the server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def start_server():
    try:
        # Create socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))  # Bind to address and port
            server_socket.listen()             # Start listening for connections
            print(f"[SERVER] Listening on {HOST}:{PORT}...")

            # Accept a connection from a client
            conn, addr = server_socket.accept()
            with conn:
                print(f"[SERVER] Connected by {addr}")
                while True:
                    data = conn.recv(1024)  # Receive up to 1024 bytes
                    if not data:
                        print("[SERVER] Client disconnected.")
                        break
                    print(f"[SERVER] Received: {data.decode()}")
                    response = f"Echo from server: {data.decode()}"
                    conn.sendall(response.encode())  # Send response back to client

    except Exception as e:
        print(f"[SERVER ERROR] {e}")

if __name__ == "__main__":
    start_server()
