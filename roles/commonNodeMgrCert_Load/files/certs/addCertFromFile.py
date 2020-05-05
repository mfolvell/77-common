# -----------------------------------------------------------------------------
# Connect to a particular process and add a new certificate to the 
# certificate store
# -----------------------------------------------------------------------------

from java.io import File, FileInputStream
from java.security.cert import CertificateFactory
from nmdeployment import NodeManagerDeployAPI
from vtrace import Tracer
from addCert import CertStoreUtil 
import common
from com.vordel.archive.fed import DeploymentArchive

# Set trace to info level
t = Tracer(Tracer.INFO) 

certFileName = "mycert.cer"
alias = "My Cert"

# Connects to the Admin Node Manager and downloads a configuration from it
adminNM = NodeManagerDeployAPI.create(common.nm_apiURL, common.userName, common.password)
archive = adminNM.getDeploymentArchiveForServerByName(common.defGroupName, common.defServerName)

# Gets the entity store from the deployment archive
es = adminNM.getArchiveEntityStore(archive, '')

# Gets the Cert Store using the short hand key
certStore = es.get('/[Certificates]name=Certificate Store');

# Loads the certificate from a file 
cf = CertificateFactory.getInstance("X.509");
f =  File(certFileName)
cert = cf.generateCertificate(FileInputStream(f))
t.info("Loaded certificate from file: " + cert.getSubjectDN().getName())

# Adds the Cert to the Cert Store
CertStoreUtil.addCertToStore(es, alias, cert)

# ------------------------------------------------------------------------------
# Now that the cert has been added to the locally saved entity store, 
# prepare to create a Deployment Package and associated package 
# properties (name value pairs)
# Two things need to be associated with the Deployment Package:
# 1. The package properties file
# 2. The updated entitystore
# -----------------------------------------------------------------------------

# 1. Update the environment package properties with a new comment for 
#    adding a cert to the Cert store
envProps = archive.getEnvironmentProperties();
envProps[DeploymentArchive.VERSIONCOMMENT_DEFAULT_PROPERTY] = "Add cert with alias %s" % alias
archive.updateEnvironmentProperties(envProps);

# 2. Update the entity store in the archive
adminNM.updateArchiveConfiguration(archive, es)

# Deploy the Deployment Package to the server
adminNM.deployToServer(common.defGroupName, common.defServerName, archive) 
es.close()
