import socket
import threading

HOST = "0.0.0.0"
PORT = 9999

clients = []
lock = threading.Lock()


def broadcast(message, sender_socket=None):
    with lock:
        for client_socket, username in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode("utf-8"))
                except:
                    pass


def handel_client(client_socket, address):
    print(f" [+] New connection from {address}")

    try:
        username = client_socket.recv(1024).decode("utf-8").strip()
    except:
        client_socket.close()
        return

    with lock:
        clients.append((client_socket, username))

    print(f" [+] {username} joined the chat")
    broadcast(f" *** {username} joined the chat ***", client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")

            if not message:
                break

            if message.strip().startswith("/users"):
                with lock:
                    user_list = ", ".join([u for _, u in clients])
                client_socket.send(f" Online: {user_list}".encode("utf-8"))
                continue

            broadcast(f"[{username}] {message}", client_socket)
            print(f" [{username}] {message}")

        except:
            break

    with lock:
        clients.remove((client_socket, username))

    client_socket.close()
    broadcast(f" *** {username} left the chat ***")
    print(f" [-] {username} disconnected")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))

    server_socket.listen(5)

    print(f"\n{'=' * 50}")
    print(f" Chat Server Started")
    print(f" Listening on {HOST}:{PORT}")
    print(f" Waiting for connections...")
    print(f"{'=' * 50}\n")

    try:
        while True:
            client_socket, address = server_socket.accept()

            thread = threading.Thread(
                target=handel_client, args=(client_socket, address), daemon=True
            )
            thread.start()

    except KeyboardInterrupt:
        print("\n [!] Server shutting down...")

    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
