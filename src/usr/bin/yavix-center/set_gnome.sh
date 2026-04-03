#!/bin/bash

sudo sed -i 's/^Session=.*/Session=gnome/' /var/lib/AccountsService/users/$USER

sudo systemctl restart gdm
