#!/bin/bash

hostnameShort=lol-apigw-admin01

apigwHome=/opt/Axway-7.6.2/apigateway
grp=gr1
systemUser=admin
adminPassord=changeme
script=loadCertFromHost.py
scriptPath="$apigwHome/samples/scripts"
patchUpdate=/opt/Axway-7.6.2/apigateway/install

 ./run.sh certs/addCertsFromSSL.py  -n "$hostnameShort"  -u "$systemUser" -p "$adminPassord" -g "$grp" 
