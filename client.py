import socket
import sys
import threading

HOST = "127.0.0.1"
PORT = 9999


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")

            if not message:
                print("\n [!] Disconnected from server.")
                sys.exit(0)

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except:
            print("\n [!] Connection lost.")
            sys.exit(0)


def start_client():
    username = input(" Enter your username: ").strip()

    if not username:
        print(" Error: username cannot be empty")
        sys.exit(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f" Error: Could not connect to {HOST}:{PORT}")
        print("Make sure the server is running.")
        sys.exit(1)

    print(f"\n Connected to chat server!")
    print(f" Type your message and press Enter to send.")
    print(f" Type /quit to exit. \n")

    client_socket.send(username.encode("utf-8"))

    receive_thread = threading.Thread(
        target=receive_messages, args=(client_socket,), daemon=True
    )
    receive_thread.start()

    while True:
        try:
            message = input("You: ").strip()

            if not message:
                continue

            if message == "/quit":
                print("Goodbye!")
                break

            client_socket.send(message.encode("utf-8"))

        except KeyboardInterrupt:
            print("\n Goodbye!")
            break

    client_socket.close()


if __name__ == "__main__":
    start_client()
