from OCCSE.RepositoryManager import *
from OCCSE.ReasonerInterface import *
from OCCSE.OCCSE import *
from OCCSE.QueryBuilderModule import *



repositoryManager = RepositoryManager(None)
repositoryManager.addRepositories(["file://../ocgen-test/Blondie 1.0.owl"])
repositoryManager.addRepositories(["file://../ocgen-test/oc-found.owl"])
repositoryManager.addRepositories(["file://../ocgen-test/oc-commerce.owl"])
repositoryManager.addRepositories(["file://../ocgen-test/oc-ethereum.owl"])
repositoryManager.addRepositories(["file://../ocgen-test/ocgen-test.owl"])

reasonerInterface=ReasonerInterface("pellet")


occse = OCCSE(repositoryManager, reasonerInterface)


occse.loadRepository()
occse.syncReasoner()

#occse.addPrefixes([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")])

print("QF1: ", occse.performQueryQF1([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")]))
print("QF2: ", occse.performQueryQF2([("ocgen-test", "http://www.ngi.ontochain/ontologies/ocgen-test.owl#")]))
print("QF3: ", occse.performQueryQF3([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "ocgen-test:batch2563Offering"))
print("QF4: ", occse.performQueryQF4([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "ocgen-test:batch2563Offering"))
print("QF5: ", occse.performQueryQF5([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "ocgen-test:batch2563Offering"))
print("QF6: ", occse.performQueryQF6([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "ocgen-test:batch2563Offering"))
print("QF7: ", occse.performQueryQF7([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "ocgen-test:batch2563Offering"))

#OC-Commerce default queries
print("QC1: ", occse.performQueryQC1([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")]))
print("QC2: ", occse.performQueryQC2([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "ocgen-test:batch2563Offering"))
print("QC3: ", occse.performQueryQC3([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")]))

#OC-Ethereum default queries
print("QE1: ", occse.performQueryQE1([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")]))
print("QE2: ", occse.performQueryQE2([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "ocgen-test:appleBatch2563Token"))
print("QE3: ", occse.performQueryQE3([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")],"ocgen-test:Apple"))
print("QE4: ",  occse.performQueryQE4([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")]))

#custom query
#occse.removePrefixes([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")])
query=Query([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "Select DISTINCT ?x WHERE { ?x a occom:Offering.} LIMIT 10")
print("Custom Query 1: ", occse.performQuery(query))

query=Query([("ocgen-test","http://www.ngi.ontochain/ontologies/ocgen-test.owl#")], "Select DISTINCT ?x WHERE { ?x a ?param1 .} LIMIT 10", [("?param1", "occom:Offering")])
print("The query is: \n ", query.build())
print("The query before execution is \n", occse.getQuery(query))


print("Custom Query 2: ", occse.performQuery(query))

print("Editing the query 2. Empty result is expected")
query.setParameters([("?param1", "occom:StandardOffering")])
print("The query is: \n ", query.build())
print("The query before execution is \n", occse.getQuery(query))
print("Custom Query 2: ", occse.performQuery(query))
