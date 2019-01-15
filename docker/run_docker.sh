#!/bin/sh

IMAGE_NAME='thhuang/sheet_music_ai'

PRJ_ROOT='.'
INPUT_PATH='/data/thhuang/SheetMusicAI_input'
OUTPUT_PATH='/data/thhuang/SheetMusicAI_output'
SSH_PORT='9753'

docker run --detach \
           --name sheet_music_ai \
           --hostname sheet_music_ai \
           --privileged \
           --publish ${SSH_PORT}:22 \
           ${IMAGE_NAME}
