#!/bin/bash
export PYTHONPATH=/data/data/com.termux/files/usr/lib/python3.12/site-packages

BOT_PATH="/data/adb/bot.py"
PYTHON_BIN="/data/data/com.termux/files/usr/bin/python"

while true; do
    if ! pgrep -f "$BOT_PATH" > /dev/null; then
        echo "[$(date)] Iniciando bot.py"
        $PYTHON_BIN "$BOT_PATH"
        echo "[$(date)] bot.py finalizó. Reiniciando en 5 segundos..."
    else
        echo "[$(date)] bot.py ya se está ejecutando. Esperando..."
    fi
    sleep 5
done
