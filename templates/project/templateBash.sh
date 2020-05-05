#!/bin/bash
set -e
set -u

# Laster ned lisenser fra gateway repo
rm -rf ./localGitFolder
mkdir ./localGitFolder
git clone ssh://git@stash.intern.sparebank1.no:22/axway/axway-licenses.git ./localGitFolder

# Install of api gateway and manager
ansible-playbook -i ./inventories/lol/hosts -e env=lol ./playbooks/gateway_Install.yml

# Fjerner lokal copy av lisenser
rm -rf  ./localGitFolder
