#!/bin/bash

# Input parametere
apigw_home=$1
app_config_path=$2

### Check if  directory does not exist ###
if [ ! -d "$apigw_home/$app_config_path/backup" ]
then
    mkdir "$apigw_home/$app_config_path/backup"
fi

cd "$apigw_home/$app_config_path"
CURRENTEPOCTIME=`date +"%Y%m%d-%H%M%S"`

cp -f "$apigw_home/$app_config_path/app.config" ./backup/app.config.$CURRENTEPOCTIME
cp -f "$apigw_home/install/app.config"  "$apigw_home/$app_config_path"
