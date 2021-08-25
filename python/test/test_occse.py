from OCCSE.RepositoryManager import *
from OCCSE.ReasonerInterface import *
from OCCSE.OCCSE import *
from OCCSE.QueryBuilderModule import *



repositoryManager = RepositoryManager(None)
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/Blondie 1.0.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-found.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-commerce.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-ethereum.owl"])
repositoryManager.addRepositories(["file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/meeting-130721.owl"])

reasonerInterface=ReasonerInterface("pellet")


occse = OCCSE(repositoryManager, reasonerInterface)


occse.loadRepository()
occse.syncReasoner()

#occse.addPrefixes([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])

print("QF1: ",  list(occse.performQueryQF1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print("QF2: ", list(occse.performQueryQF2([("meeting130721", "http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print("QF3: ", list(occse.performQueryQF3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print("QF4: ", list(occse.performQueryQF4([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print("QF5: ", list(occse.performQueryQF5([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print("QF6: ", list(occse.performQueryQF6([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print("QF7: ", list(occse.performQueryQF7([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))

#OC-Commerce default queries
print("QC1: ",list(occse.performQueryQC1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print("QC2: ",list(occse.performQueryQC2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print("QC3: ",list(occse.performQueryQC3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))

#OC-Ethereum default queries
print("QE1: ",list(occse.performQueryQE1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print("QE2: ",list(occse.performQueryQE2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:appleBatch2563Token")))
print("QE3: ",list(occse.performQueryQE3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")],"meeting130721:Apple")))
print("QE4: ",list(occse.performQueryQE4([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))

#custom query
#occse.removePrefixes([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])
query=Query([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "Select DISTINCT ?x WHERE { ?x a occom:Offering.} LIMIT 10")
print("Custom Query 1: ", list(occse.performQuery(query)))

query=Query([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "Select DISTINCT ?x WHERE { ?x a ?param1 .} LIMIT 10", ["?param1", "occom:Offering"])
print("Custom Query 2: ", list(occse.performQuery(query)))


