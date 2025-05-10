#!/bin/bash
read -p "Masukkan IP lawan chat: " ip
echo "Ketik pesanmu. Tekan Ctrl+C untuk keluar."
while true; do
  read -p "you@whois chat: " pesan
  echo "friend@whois chat: $pesan" | nc $ip 22
done
