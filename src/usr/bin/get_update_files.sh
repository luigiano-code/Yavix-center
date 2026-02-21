#!/bin/bash

sudo rm -rf /usr/bin/update.sh
curl -O https://raw.githubusercontent.com/luigiano-code/Yavix-repository/main/update.sh
sudo mv update.sh /usr/bin/update.sh
