# -----------------------------------------------------------------------------
# Connect to a particular process and add a new certificate downloaded
# from an SSL server
# -----------------------------------------------------------------------------

from java.lang import Integer
from java.net import URL
from java.security import SecureRandom
from java.util import ArrayList
from javax.net.ssl import HostnameVerifier, HttpsURLConnection, SSLContext, X509TrustManager
from addCert import CertStoreUtil
from nmdeployment import NodeManagerDeployAPI
from vtrace import Tracer
import common
from com.vordel.archive.fed import DeploymentArchive

# Set trace to info level
t = Tracer(Tracer.INFO)

# -----------------------------------------------------------------------------
# Class to Create a TrustManager
# -----------------------------------------------------------------------------
class MyX509TrustManager(X509TrustManager):
    certs = None

    def __init__(self):
        self.certs = ArrayList()

    def checkClientTrusted(self, chain, authType):
        t.debug("checkClientTrusted")

    def checkServerTrusted(self, chain, authType):
        t.debug("checkServerTrusted")
        for cert in chain:
            self.certs.add(cert)

    def getAcceptedIssuers(self):
        t.debug("getAcceptedIssuers")

# -----------------------------------------------------------------------------
# Class to create a HostnameVerifier
# -----------------------------------------------------------------------------
class MyHostnameVerifier(HostnameVerifier):

    def verify(self, hostname, session):
        t.info("verify host: " + hostname)
        return True;


url = "https://www.amazon.com"

tm = MyX509TrustManager()
trustManagers = [tm]

# Returns a SSLContext object that implements the SSL secure socket protocol.
sc =  SSLContext.getInstance("SSL");

# -----------------------------------------------------------------------------
# Initializes the context with :
# - KeyManagers which are responsible for managing the key material which is
#   used to authenticate the local SSLSocket to its peer. If no key material
#   is available, the socket will be unable to present authentication credentials.
# - TrustManagers are responsible for managing the trust material that is used
#   when making trust decisions, and for deciding whether credentials presented
#   by a peer should be accepted.
# - The SecureRandom class produces a cryptographically strong random
#   number generator (RNG).
# -----------------------------------------------------------------------------
sc.init(None, trustManagers, SecureRandom());

# Gets a SocketFactory object for this context and sets the default
# SSLSocketFactory to it. The socket factories are used when creating
# sockets for the secure https URL connections.
HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());

# Gets a HostnameVerifier and sets the default HostnameVerifier to it.
# If URL's hostname and the server's identification hostname mismatch, the
# verification mechanism can call back to implementers of the
# HostnameVerifiers interface to determine if the connection should be allowed.
HttpsURLConnection.setDefaultHostnameVerifier(MyHostnameVerifier());

# Gets a connection to the remote object referred to by the URL.
url=common.certURL
print("url=" + url)
u = URL(url)
http = u.openConnection();
http.connect();

t.info("Found " + Integer.toString(tm.certs.size()) + " certificates to be added from " + url)

# Connects to the Admin Node Manager and downloads a configuration from it
adminNM = NodeManagerDeployAPI.create(common.nm_apiURL, common.userName, common.password)
archive = adminNM.getDeploymentArchiveForServerByName(common.defGroupName, common.defServerName)

# Gets the entity store from the deployment archive
es = adminNM.getArchiveEntityStore(archive, '')

# Gets the Cert store using the short hand key
certStore = es.get('/[Certificates]name=Certificate Store');

# -----------------------------------------------------------------------------
# For every Certificate get the distinguished name and add it to the
# Cert Store.
# -----------------------------------------------------------------------------
for cert in tm.certs:
    alias = cert.getSubjectDN().getName()
    CertStoreUtil.addCertToStore(es, alias, cert)

# ------------------------------------------------------------------------------
# Now that the certificates have been added in the locally saved entity store,
# prepare to create a Deployment Package and associated package
# properties (name value pairs)
# Two things need to be associated with the Deployment Package:
# 1. The package properties file
# 2. The updated entitystore
# -----------------------------------------------------------------------------

# 1. Update the environment package properties with a new comment
#    for adding certs from SSL
envProps = archive.getEnvironmentProperties();
envProps[DeploymentArchive.VERSIONCOMMENT_DEFAULT_PROPERTY] = "Add certs from SSL"
archive.updateEnvironmentProperties(envProps);

# 2. Update the entity store in the archive
adminNM.updateArchiveConfiguration(archive, es)

# Deploy the Deployment Package to the server
adminNM.deployToServer(common.defGroupName, common.defServerName, archive)
es.close()
