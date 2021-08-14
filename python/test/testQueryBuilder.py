from OCCSE.QueryBuilderModule import *
from OCCSE.RepositoryManager import *
from OCCSE.ReasonerInterface import *
from owlready2 import *


#q=Query([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], ["prova"], ["p1","p2"])
#print(q.build())

#OC-Found default queries
blondie = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/Blondie 1.0.owl").load()
ocfound = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-found.owl").load()
occommerce = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-commerce.owl").load()
ocethereum = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-ethereum.owl").load()
onto = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/meeting-130721.owl").load()


repositoryManager = RepositoryManager(None)
print(repositoryManager.getRepository(), repositoryManager.getChanged())
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/Blondie 1.0.owl"])
print(repositoryManager.getRepository(), repositoryManager.getChanged())
repositoryManager.removeRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/Blondie 1.0.owl"])
print(repositoryManager.getRepository())


#sync_reasoner_hermit(default_world, debug = 9)
reasonerInterface=ReasonerInterface("hermit")
print(reasonerInterface.selectedReasoner)
reasonerInterface.runReasoner(default_world)

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




qf1=QueryQF1(prefix)
print(qf1.build())
print(list(default_world.sparql(qf1.build())))

qf2=QueryQF2(prefix)
print(qf2.build())
print(list(default_world.sparql(qf2.build())))


qf3=QueryQF3(prefix, "meeting130721:batch2563Offering")
print(qf3.build())
print(list(default_world.sparql(qf3.build())))


qf4=QueryQF4(prefix, "meeting130721:batch2563Offering")
print(qf4.build())
print(list(default_world.sparql(qf4.build())))

qf5=QueryQF5(prefix, "meeting130721:batch2563Offering")
print(qf5.build())
print(list(default_world.sparql(qf5.build())))

qf6=QueryQF6(prefix, "meeting130721:batch2563Offering")
print(qf6.build())
print(list(default_world.sparql(qf6.build())))

qf7=QueryQF7(prefix, "meeting130721:batch2563Offering")
print(qf7.build())
print(list(default_world.sparql(qf7.build())))

#OC-Commerce default queries
qc1=QueryQC1(prefix)
print(qc1.build())
print(list(default_world.sparql(qc1.build())))

qc2=QueryQC2(prefix, "meeting130721:batch2563Offering")
print(qc2.build())
print(list(default_world.sparql(qc2.build())))

qc3=QueryQC3(prefix)
print(qc3.build())
print(list(default_world.sparql(qc3.build())))

#OC-Ethereum default queries
qe1=QueryQE1(prefix)
print(qe1.build())
print(list(default_world.sparql(qe1.build())))

qe2=QueryQE2(prefix, "meeting130721:appleBatch2563Token")
print(qe2.build())
print(list(default_world.sparql(qe2.build())))

qe3=QueryQE3(prefix, "meeting130721:Apple")
print(qe3.build())
print(list(default_world.sparql(qe3.build())))

qe4=QueryQE4(prefix)
print(qe4.build())
print(list(default_world.sparql(qe4.build())))