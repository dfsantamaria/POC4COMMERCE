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

print("QF1: ", occse.performQueryQF1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")]))
print("QF2: ", occse.performQueryQF2([("meeting130721", "http://www.ngi.ontochain/ontologies/meeting.owl#")]))
print("QF3: ", occse.performQueryQF3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering"))
print("QF4: ", occse.performQueryQF4([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering"))
print("QF5: ", occse.performQueryQF5([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering"))
print("QF6: ", occse.performQueryQF6([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering"))
print("QF7: ", occse.performQueryQF7([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering"))

#OC-Commerce default queries
print("QC1: ", occse.performQueryQC1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")]))
print("QC2: ", occse.performQueryQC2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering"))
print("QC3: ", occse.performQueryQC3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")]))

#OC-Ethereum default queries
print("QE1: ", occse.performQueryQE1([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")]))
print("QE2: ", occse.performQueryQE2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:appleBatch2563Token"))
print("QE3: ", occse.performQueryQE3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")],"meeting130721:Apple"))
print("QE4: ",  occse.performQueryQE4([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")]))

#custom query
#occse.removePrefixes([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])
query=Query([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "Select DISTINCT ?x WHERE { ?x a occom:Offering.} LIMIT 10")
print("Custom Query 1: ", occse.performQuery(query))

query=Query([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "Select DISTINCT ?x WHERE { ?x a ?param1 .} LIMIT 10", [("?param1", "occom:Offering")])
print("The query is: \n ", query.build())
print("The query before execution is \n", occse.getQuery(query))


print("Custom Query 2: ", occse.performQuery(query))


