# 💬 Python Chat App

A multi-threaded TCP group chat application built from scratch using Python
sockets. Multiple clients can connect simultaneously and exchange messages
in real time.

## 📸 Demo

*(coming soon)*

## 🔧 How It Works

The server listens for incoming TCP connections and spawns a new thread for
each client. When a message arrives from one client, the server broadcasts
it to all other connected clients.

The client uses two threads simultaneously:
- **Receive thread** — constantly listens for incoming messages
- **Main thread** — waits for user input and sends messages

This solves the problem of needing to do two blocking operations at once.

## 📦 Installation

```bash
git clone https://github.com/prajwalkarna/python-chat-app.git
cd python-chat-app
python server.py
```

## 🚀 Usage

**Terminal 1 — start the server:**
```bash
python server.py
```

**Terminal 2 and 3 — connect clients:**
```bash
python client.py
```

**Available commands:**
```
/users    → show who is currently online
/quit     → disconnect from the server
```

## 📊 Example Output

**Server:**

```
==================================================
Chat Server Started
Listening on 0.0.0.0:9999
Waiting for connections...
[+] Alice joined the chat
[+] Bob joined the chat
[Alice] hello!
[Bob] hey Alice!
[-] Alice disconnected
```

**Client:**

```
Enter your username: Bob
Connected to chat server!
You: hey Test1!
You:
[Test2] hello!
You: /users
You:
Online: Test1, Test2
```

## 📚 What I Learned

- Client-server architecture — how servers accept and manage connections
- Multi-threading on both server and client side
- Race conditions and how to prevent them with locks
- Why daemon threads are used for background tasks
- SO_REUSEADDR socket option and why it matters
- How real chat applications broadcast messages
- Handling client disconnections gracefully

## 🛠️ Technologies

- Python 3
- `socket` — TCP connections
- `threading` — concurrent client handling and receiving
- Linux (CachyOS)

## ⚠️ Note

Currently works on local network. To use over the internet,
change `HOST` in `client.py` to the server's public IP address.
