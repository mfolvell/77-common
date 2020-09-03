#!/bin/bash
./APIGateway_7.6.2_Install_linux-x86-64_BN5.run \
 --mode unattended \
 --prefix /opt/Axway-7.6.2 \
 --enable-components apimgmt,apigateway,nodemanager,apimgmt,cassandra \
 --disable-components qstart,policystudio,analytics,apitester,configurationstudio,packagedeploytools \
 --licenseFilePath /opt/Axway-7.6.2/apigateway/conf/licenses/apiGateway.lic \
 --apimgmtLicenseFilePath /opt/Axway-7.6.2/apigateway/conf/licenses/apiMgr.lic \
 --firstInNewDomain vag01 \
 --adminpasswd changeme \
 --apiadminpasswd changeme \
 --rnmPassword changeme \
 --cassandraInstalldir /opt/db/cassandra \
 --cassandraJDK /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.232.b09-0.el7_7.x86_64/jre \
