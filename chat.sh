#!/bin/bash
echo "Menunggu pesan di port 22..."
while true; do
  nc -l -p 22
done
