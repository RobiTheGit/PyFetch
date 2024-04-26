#!/usr/bin/bash
if [[ -d ~/.local/bin ]]; then
cp main.py ~/.local/bin/pyfetch
else
mkdir -p ~/.local/bin
cp main.py ~/.local/bin/pyfetch
fi

