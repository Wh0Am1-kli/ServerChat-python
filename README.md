# Terminal Chat Server

Chat server ringan berbasis Python untuk komunikasi tim hacking **WhoIs** via TCP socket. Dirancang agar simple, stabil, dan bisa jalan di VPS tanpa root.

## Fitur
- Multi-user chat (broadcast)
- Identitas pengguna (username@server)
- Username disimpan otomatis, tidak perlu login ulang
- Port default: **3441**
- Bisa dijalankan di Termux, VPS, atau PC

## Struktur File
- `chat_server.py` — Server chat Python (run di VPS)
- `chat_client.py` — Client Python (run di Termux/PC)
- `.username` — File lokal penyimpan username client

## Cara Pakai

### Jalankan Server (di VPS)
```bash
python3 chat_server.py
```
### Jalankan Chat (di Terminal, CMD, Termux)
```bash
python3 chat_client.py
