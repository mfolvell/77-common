#!/bin/bash

# Input parametere
grp=$1
path_update=$2
apigw_home=$3
hostnameShort=$4

echo "grp=" $grp "path_update="$path_update "apigw_home="$apigw_home "hostnameShort="$hostnameShort

# =========================================================
# Copying the config file to the spesific instanse folder (with backup of the old)
INSTANCE=`./get_gateway_instance.sh $apigw_home $hostnameShort`
GROUPNO=`./get_gateway_group.sh $grp $apigw_home `
echo INSTANCE=$INSTANCE
echo GROUPNO=$GROUPNO

### Check if  directory does not exist ###
if [ ! -d "$apigw_home/groups/$GROUPNO/$INSTANCE/conf/backup" ]
then
    mkdir "$apigw_home/groups/$GROUPNO/$INSTANCE/conf/backup"
fi

cd "$apigw_home/groups/$GROUPNO/$INSTANCE/conf/"

CURRENTEPOCTIME=`date +"%Y%m%d-%H%M%S"`


mv ./envSettings.props ./backup/envSettings.props.$CURRENTEPOCTIME
sed -i "s~¤¤inst¤¤~$INSTANCE~g" "$path_update/envSettings.props"
cp "$path_update/envSettings.props" ./envSettings.props
