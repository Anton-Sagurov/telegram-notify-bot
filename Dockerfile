FROM python:3.10-alpine

ENV TG_TOKEN="token"

# ENV variables for building the image
ENV USER="tgbot"
ENV UID="1000"
ENV GID="1000"
ENV HOME="/opt/app"

RUN mkdir "$HOME" && \
    chown "$UID:$GID" "$HOME" && \
    addgroup -g "$GID" "$USER" && \
    adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

USER "$USER"

COPY ./tg-notify-bot ./requirements.txt "$HOME/tg-notify-bot/"
WORKDIR "$HOME"
# Modify the $USER PATH variable
ENV PATH="$PATH:$HOME/.local/bin"

RUN python -m pip install --user --no-cache-dir -r ./tg-notify-bot/requirements.txt

ENTRYPOINT ["python", "-m", "tg-notify-bot"]
