from OCCSE.RepositoryManager import *
from OCCSE.ReasonerInterface import *
from OCCSE.OCCSE import *
from OCCSE.QueryBuilderModule import *
from owlready2 import *

prefix = [("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
                        ("owl", "http://www.w3.org/2002/07/owl#"),
                        ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
                        ("xsd", "http://www.w3.org/2001/XMLSchema#"),
                        ("oabox", "http://www.dmi.unict.it/oasis-abox.owl#"),
                        ("oasis", "http://www.dmi.unict.it/oasis.owl#"),
                        ("occom", "http://www.ngi.ontochain/ontologies/oc-commerce.owl#"),
                        ("ocfound", "http://www.ngi.ontochain/ontologies/oc-found.owl#"),
                        ("ocether", "http://www.ngi.ontochain/ontologies/oc-ethereum.owl#"),
                        ("gr", "http://purl.org/goodrelations/v1#"),
                        ("blon", "http://www.semanticblockchain.com/Blondie.owl#"),
                        ("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")]

repositoryManager = RepositoryManager(None)
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/Blondie 1.0.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-found.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-commerce.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-ethereum.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/meeting-130721.owl"])

reasonerInterface=ReasonerInterface("hermit")


occse = OCCSE(repositoryManager, reasonerInterface)
occse.loadRepository()
occse.syncReasoner()

qf1=QueryQF1(prefix)
print(list(occse.performQuery(qf1)))

qf2=QueryQF2(prefix)
print(list(occse.performQuery(qf2)))


qf3=QueryQF3(prefix, "meeting130721:batch2563Offering")
print(list(occse.performQuery(qf3)))


qf4=QueryQF4(prefix, "meeting130721:batch2563Offering")
print(list(occse.performQuery(qf4)))

qf5=QueryQF5(prefix, "meeting130721:batch2563Offering")
print(list(occse.performQuery(qf5)))

qf6=QueryQF6(prefix, "meeting130721:batch2563Offering")
print(list(occse.performQuery(qf6)))

qf7=QueryQF7(prefix, "meeting130721:batch2563Offering")
print(list(occse.performQuery(qf7)))

#OC-Commerce default queries
qc1=QueryQC1(prefix)
print(list(occse.performQuery(qc1)))

qc2=QueryQC2(prefix, "meeting130721:batch2563Offering")
print(list(occse.performQuery(qc2)))

qc3=QueryQC3(prefix)
print(list(occse.performQuery(qc3)))

#OC-Ethereum default queries
qe1=QueryQE1(prefix)
print(list(occse.performQuery(qe1)))

qe2=QueryQE2(prefix, "meeting130721:appleBatch2563Token")
print(list(occse.performQuery(qe2)))

qe3=QueryQE3(prefix, "meeting130721:Apple")
print(list(occse.performQuery(qe3)))

qe4=QueryQE4(prefix)
print(list(occse.performQuery(qe4)))