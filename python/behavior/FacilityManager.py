from OASIS_behavior_generator import *

class FacilityManager(BehaviorManager):
      def __init__(self, ontologyGraph, ontologyNamespace, ontologyURL, ontologyTemplateGraph,
                   ontologyTemplateNamespace, templateURL):  # INPUT: the user ontology, the user ontology namespace
        BehaviorManager.__init__(self, ontologyGraph, ontologyNamespace, ontologyURL, ontologyTemplateGraph, ontologyTemplateNamespace, templateURL)

        self.addOntoMap("ocfound", "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/OC-Found.owl", None, None)
        self.ontologies.append(self.loadOntology(self.ontoMap["ocfound"]["url"]))





