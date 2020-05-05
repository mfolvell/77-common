#!/bin/bash
set -e
set -u

# Install of api gateway and manager
ansible-playbook -i ./inventories/lol/hosts -e env=lol ./playbooks/tempPlayBook.yml
