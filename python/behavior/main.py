from rdflib import *

class Behavior:
    def __init__(self, ontologyGraph, ontologyNamespace): # INPUT: the user ontology, the user ontology namespace
        self.oasisURL = "https://www.dmi.unict.it/santamaria/projects/oasis/sources/rdf/oasis-rdf.owl"  # OASIS ontology URL
        self.oasisABoxURL = "https://www.dmi.unict.it/santamaria/projects/oasis/sources/rdf/oasis-abox-rdf.owl"  # OASIS-ABox ontology URL

        #
        #oasis ontology data
        #
        self.oasisOnt = self.loadOntology(self.oasisURL)  # OASIS ontology object
        self.oasisABoxOnt = self.loadOntology(self.oasisABoxURL)  # OASIS-ABox ontology object

        self.oasisNamespace=self.getNamespace(self.oasisOnt)  # OASIS ontology namespace
        self.oasisABoxNamespace=self.getNamespace(self.oasisABoxOnt)  # OASIS-ABox ontology namespace

        #
        #user ontology data
        #
        self.baseOntology = ontologyGraph  # User ontology
        if ontologyNamespace == None: #Computing user ontology namespace
           self.baseNamespace = self.getNamespace(self.baseOntology)
        else:
           self.baseNamespace = ontologyNamespace
        self.baseAgent = None  # User agent name

        return

    #create an ontology object from a given URL
    def loadOntology(self, ontoURL):
        g=Graph()
        g.load(ontoURL)
        return g

    # Get the base namespace of an ontology given the ontology object
    def getNamespace(self, ontology):
        namespace = ""
        for ns_prefix, ns_namespace in ontology.namespaces():
            if ns_prefix == "":
               namespace=ns_namespace
        if not namespace.endswith('#'):
            return namespace+"#"
        return namespace

    # Get the IRI of OASIS entities given their entity name
    def getOASISEntityByName(self, name):
        return self.oasisNamespace + name

    # Create an user agent given the agent entity name
    def createAgent(self, agentName):
        self.baseAgent = self.baseNamespace + agentName
        self.baseOntology.add((URIRef(self.baseAgent), RDF.type, self.getOASISEntityByName("Agent")))
        return self.baseAgent






#test
namespace =  Namespace("http://www.ontochain.org/myOntology#")
ontology=Graph()
ontology.bind("myOntology", namespace)
# Create the graph
b = Behavior(ontology, namespace)
#Crate agent
b.createAgent("MyAgent")
print(ontology.serialize(format="turtle").decode("utf-8"))
