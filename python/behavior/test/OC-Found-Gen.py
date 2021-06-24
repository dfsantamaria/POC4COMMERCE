from OASIS_behavior_generator import *

file = open("OC-Found.owl", "r")
ontology = Graph()
ontology.parse(file)

namespace =  Namespace("http://www.ngi.ontochain/ontologies/oc-found.owl#")

ontology.bind("base", namespace)
ontology.bind("owl","http://www.w3.org/2002/07/owl#")


b = BehaviorManager(ontology, namespace, ontology, namespace)

for t in ontology:
    print(t)
