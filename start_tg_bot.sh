#!/usr/bin/env bash

IMAGE_NAME='sagurov/telegram-notification-bot'
VERSION="latest"
CONTAINER_NAME="tg-notify-bot"

TG_TOKEN=""
DS_WEBHOOK_URL=""

docker stop "$CONTAINER_NAME"
docker rm "$CONTAINER_NAME"

docker run -d --name "$CONTAINER_NAME" \
           -e TG_TOKEN="${TG_TOKEN}" \
           -e DS_WEBHOOK_URL="${DS_WEBHOOK_URL}" \
           "${IMAGE_NAME}:${VERSION}"
