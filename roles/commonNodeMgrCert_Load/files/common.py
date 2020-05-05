import sys
from optparse import OptionParser
import configutil

class MyOptionParser(OptionParser):
    def error(self, msg): # ignore unknown arguments
        pass

parser = MyOptionParser()

parser.add_option("-s", "--certURL", dest="certURL", help="URL for local certificate", default="https://localhost:8090/api")
parser.add_option("-g", "--group", dest="group", help="API Server Group", default="Group1")
parser.add_option("-n", "--service", dest="service", help="API Server", default="APIServer1")
parser.add_option("-u", "--username", dest="user")
parser.add_option("-p", "--password", dest="password")
parser.add_option("-d", "--url", dest="url", help="Traffic monitor URL for API", default="https://localhost:8090/api")


copyargs = sys.argv[:]
(options, args) = parser.parse_args(args=copyargs)

# Node Manager API URLs
nm_apiURL = options.url

print ("certURL=" + options.certURL)

# Traffic Monitor URLs - these are invoked on the Gateway via Node Manager
gw_opsURLStart = nm_apiURL + "/router/service/"
gw_opsURLEnd = "/ops/"

# Default API Server
defServerName = options.service
defGroupName = options.group
certURL = options.certURL

userName,password = configutil.getUserCredentials(options.user,options.password)

# command line username/passwords
#userName = options.user
#password = options.password
