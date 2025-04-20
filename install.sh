#!/bin/bash
set -e
set -o pipefail
basedir="$(realpath "$(dirname "$0")")"
mkdir -p "$HOME"/.local/bin
rsync -av "$basedir/" "$HOME/.local/bin/plotty-code/"
rsync -av "$basedir/plotty" "$HOME/.local/bin/plotty"
