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

reasonerInterface=ReasonerInterface("peller")


occse = OCCSE(repositoryManager, reasonerInterface)


occse.loadRepository()
occse.syncReasoner()

#occse.addPrefixes([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])

print(list(occse.performQueryQF1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print(list(occse.performQueryQF2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print(list(occse.performQueryQF3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print(list(occse.performQueryQF4([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print(list(occse.performQueryQF5([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print(list(occse.performQueryQF6([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print(list(occse.performQueryQF7([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))

#OC-Commerce default queries
print(list(occse.performQueryQC1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print(list(occse.performQueryQC2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")))
print(list(occse.performQueryQC3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))

#OC-Ethereum default queries
print(list(occse.performQueryQE1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
print(list(occse.performQueryQE2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:appleBatch2563Token")))
print(list(occse.performQueryQE3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")],"meeting130721:Apple")))
print(list(occse.performQueryQE4([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])))
#custom query
#occse.removePrefixes([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])
query=Query([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], ["Select DISTINCT ?x WHERE { ?x a occom:Offering.} LIMIT 10"])
print(list(occse.performQuery(query)))


