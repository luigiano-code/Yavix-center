#!/bin/bash

paccache -rk1

orphans=$(pacman -Qtdq)

if [ -n "$orphans" ]; then
    pacman -Rns --noconfirm $orphans
else
    echo "nothing to do"
fi

rm -rf ~/.cache/*
mkdir -p ~/.cache

journalctl --vacuum-time=2weeks

