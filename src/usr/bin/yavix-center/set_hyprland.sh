#/bin/bash

sudo sed -i 's/^Session=.*/Session=hyprland/' /var/lib/AccountsService/users/$USER

sleep 1

sudo sed -i 's/^Session=.*/Session=hyprland/' /var/lib/AccountsService/users/$USER

sudo systemctl restart gdm

