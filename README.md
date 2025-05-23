# Terminal Chat Server

Chat server ringan berbasis Python untuk komunikasi via TCP socket. Dirancang agar simple, stabil, dan bisa jalan di VPS tanpa root.

## Fitur
- Multi-user chat (broadcast)
- Identitas pengguna (username@server)
- Username disimpan otomatis, tidak perlu login ulang
- Port default: **1234** (Ganti Port di 'chat_server.py')
- Bisa dijalankan di Termux, VPS, atau PC

## Struktur File
- `chat_server.py` — Server chat Python (run di VPS)
- `chat_client.py` — Client Python (run di Termux/PC)
- `.username` — File lokal penyimpan username client

## Download

### Untuk Server (VPS)
```bash
wget https://raw.github.com/Wh0Am1-kli/ServerChat-python/main/chat_server.py
```
### Untuk Client (Termux & Linux)
```bash
wget https://raw.github.com/Wh0Am1-kli/ServerChat-python/main/chat_client.py
```
## Cara Pakai

### Jalankan Server (di VPS)
```bash
python3 chat_server.py
```
### Jalankan Chat (di Linux dan Termux)
```bash
python3 chat_client.py

