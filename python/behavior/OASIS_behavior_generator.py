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
        #print(self.baseNamespace, self.oasisNamespace, self.oasisABoxNamespace)
        return self.baseAgent

    # Add to ontology with the selected namespace an owl:imports axiom for each passed IRI.
    #INPUT the ontology and the ontology IRI that will include the owl:imports axiom, a list of IRI to be included in the ontology
    def addImportAxioms(self, ontology, ontologyNS, namespaceToImport):
        for s in namespaceToImport:
            ontology.add((URIRef(ontologyNS), OWL.imports, URIRef(s)))

    #import OASIS and OASIS-Abox in the current ontology
    def addImportOASIS(self):
        self.addImportAxioms(self.baseOntology, self.baseNamespace, [self.oasisNamespace, self.oasisABoxNamespace])


