# -----------------------------------------------------------------------------
# Connect to a particular process and add a new certificate and key from 
# P12 file to the certificate store
# -----------------------------------------------------------------------------

from java.io import File
from java.lang import Integer
from nmdeployment import NodeManagerDeployAPI
from vtrace import Tracer
from addCert import CertStoreUtil
import common
from com.vordel.archive.fed import DeploymentArchive

# Set trace to info level
t = Tracer(Tracer.INFO) 

p12File = "sample.p12"
p12Password = "fred"
alias = "My Cert"

# Connects to the Admin Node Manager and downloads a configuration from it
adminNM = NodeManagerDeployAPI.create(common.nm_apiURL, common.userName, common.password)
archive = adminNM.getDeploymentArchiveForServerByName(common.defGroupName, common.defServerName)

# Get entity store from the deployment archive
es = adminNM.getArchiveEntityStore(archive, '')

# Gets the Cert store using its short hand key
certStore = es.get('/[Certificates]name=Certificate Store');

# Loads the private key from a file
f =  File(p12File)
privateKey = CertStoreUtil.getKeyFromP12(f, p12Password)

# Loads the certificates from the P12 file
cert = CertStoreUtil.getCertFromP12(f, p12Password)

# Adds the certificate and key to the Cert store
CertStoreUtil.addCertToStore(es, alias, cert, privateKey)

# ------------------------------------------------------------------------------
# Now that the Certificate and key have been added to the Cert Store in the 
# locally saved entity store, prepare to create a Deployment Package 
# and associated package properties (name value pairs)
# Two things need to be associated with the Deployment Package:
# 1. The package properties file
# 2. The updated entitystore
# -----------------------------------------------------------------------------

# 1. Update the environment package properties with a new comment for 
#    adding the certificate from P12 file 
envProps = archive.getEnvironmentProperties();
envProps[DeploymentArchive.VERSIONCOMMENT_DEFAULT_PROPERTY] = "Add cert from P12"
archive.updateEnvironmentProperties(envProps);

# 2. Update the entity store in the archive
adminNM.updateArchiveConfiguration(archive, es)

# Deploy the Deployment Package to the server
res = adminNM.deployToServer(common.defGroupName, common.defServerName, archive) 

# Handle any errors from deployment
if res.getStatus() != True:
    t.error("Failed to deploy: " + res.getFailureReason())
    t.error("Failures: "+ Integer.toString(res.getErrorCount()))

es.close()

t.info("Added a key and cert with alias: " + alias + " and subject: " + cert.getSubjectDN().getName())
