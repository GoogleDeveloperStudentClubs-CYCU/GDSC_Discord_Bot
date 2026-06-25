#!/bin/bash

BOT_DIR="/home/ubuntu/GDSC_Discord_Bot"

BOT_COMMAND="python -u main.py"

if [ ! -d "$BOT_DIR" ]; then
    echo "錯誤: 機器人目錄 '$BOT_DIR' 不存在。請檢查腳本中的 BOT_DIR 設定。"
    exit 1
fi

cd "$BOT_DIR" || exit

if pgrep -f "$BOT_COMMAND" > /dev/null
then
    # 如果 pgrep 找到了符合的程序，代表機器人正在線上
    echo "$(date): [INFO] Discord bot is already running."
else
    # 如果沒找到，代表機器人已離線，需要啟動
    echo "$(date): [WARNING] Discord bot is not running. Starting it now..."

    nohup $BOT_COMMAND >> "$LOG_FILE" 2>&1 &
fi
