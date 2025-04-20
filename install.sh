#!/bin/bash
set -e
set -o pipefail
basedir="$(realpath "$(dirname "$0")")"
mkdir -p "$HOME"/.local/bin
rsync -av "$basedir/" "$HOME/.local/bin/plotty-code/"
ln -s "$HOME/.local/bin/plotty-code/plotty" "$HOME/.local/bin/plotty" 
