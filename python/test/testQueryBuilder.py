from OCCSE.QueryBuilderModule import *
from owlready2 import *

#q=Query([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], ["prova"], ["p1","p2"])
#print(q.build())

#OC-Found default queries
blondie = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/Blondie 1.0.owl").load(only_local=True)
ocfound = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-found.owl").load()
occommerce = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-commerce.owl").load()
ocethereum = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/oc-ethereum.owl").load()
onto = get_ontology("file://C:/Users/danie/PycharmProjects/Ontochain/test/meeting-130721/meeting-130721.owl").load()


qf1=QueryQF1()
print(qf1.build())
print(list(default_world.sparql(qf1.build())))

qf2=QueryQF2()
print(qf2.build())
print(list(default_world.sparql(qf2.build())))


qf3=QueryQF3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")
print(qf3.build())
print(list(default_world.sparql(qf3.build())))


qf4=QueryQF4([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")
print(qf4.build())
print(list(default_world.sparql(qf4.build())))

qf5=QueryQF5([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")
print(qf5.build())
print(list(default_world.sparql(qf5.build())))

qf6=QueryQF6([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")
print(qf6.build())
print(list(default_world.sparql(qf6.build())))

qf7=QueryQF7([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")
print(qf7.build())
print(list(default_world.sparql(qf7.build())))

#OC-Commerce default queries
qc1=QueryQC1()
print(qc1.build())
print(list(default_world.sparql(qc1.build())))

qc2=QueryQC2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:batch2563Offering")
print(qc2.build())
print(list(default_world.sparql(qc2.build())))

qc3=QueryQC3()
print(qc3.build())
print(list(default_world.sparql(qc3.build())))

#OC-Ethereum default queries
qe1=QueryQE1()
print(qe1.build())
print(list(default_world.sparql(qe1.build())))

qe2=QueryQE2([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:appleBatch2563Token")
print(qe2.build())
print(list(default_world.sparql(qe2.build())))

qe3=QueryQE3([("meeting130721","http://www.ngi.ontochain/ontologies/meeting.owl#")], "meeting130721:Apple")
print(qe3.build())
print(list(default_world.sparql(qe3.build())))

qe4=QueryQE4()
print(qe4.build())
print(list(default_world.sparql(qe4.build())))