#!/bin/bash

apt install python3-pip

pip3 install --break-system-packages nicegui
pip3 install --break-system-packages loguru

install_report_deps () {
    cd report
    bash install.sh
    cd -
}

setup_systemd() {
    cp systemd/clean-calc.service /etc/systemd/system/
    systemctl daemon-reload
    systemctl enable clean-calc.service
    systemctl restart clean-calc.service
}

#install_report_deps

setup_systemd