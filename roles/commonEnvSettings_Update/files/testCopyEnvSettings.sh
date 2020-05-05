#!~bin~bash

# Input parametere
grp=gr1
path_update=/opt/Axway-7.6.2/apigateway/install
apigw_home=/opt/Axway-7.6.2/apigateway
hostnameShort=lol-apigw-admin01

sh ./copyEnvSettings.sh $grp $path_update $apigw_home $hostnameShort
