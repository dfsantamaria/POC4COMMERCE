from OASIS_behavior_generator import *

#test
#create a fresh ontology
namespace =  Namespace("http://www.ontochain.org/myOntology#")
ontology=Graph()
ontology.bind("xml:base", namespace)
ontology.bind("owl","http://www.w3.org/2002/07/owl#")
# Create the graph
b = Behavior(ontology, namespace)
#import OASIS into the current ontology
b.addImportOASIS()
#Crate agent
b.createAgent("MyAgent")
print(ontology.serialize(format="turtle").decode("utf-8"))