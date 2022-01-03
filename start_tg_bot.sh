#!/usr/bin/env bash

IMAGE_NAME='sagurov/telegram-notification-bot'
VERSION=$(<./VERSION)
CONTAINER_NAME="tg-notify-bot"

TG_TOKEN=""

docker stop "$CONTAINER_NAME"
docker rm "$CONTAINER_NAME"

docker run -d --name "$CONTAINER_NAME" \
           -e TG_TOKEN="${TG_TOKEN}" \
           "${IMAGE_NAME}:${VERSION}"
