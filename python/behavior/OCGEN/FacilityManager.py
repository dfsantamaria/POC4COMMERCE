from OCGEN.OASIS_behavior_generator import *

class FacilityManager(BehaviorManager):
      def __init__(self, ontologyGraph, ontologyNamespace, ontologyURL,
                   ontologyTemplateGraph, ontologyTemplateNamespace, templateURL,
                   actionGraph, actionNamespace, actionURL):
        BehaviorManager.__init__(self, ontologyGraph, ontologyNamespace, ontologyURL,
                                 ontologyTemplateGraph, ontologyTemplateNamespace, templateURL,
                                 actionGraph, actionNamespace, actionURL,
                                 None, None, None)

        self.startOntology("ocfound", "OC-Found.owl", None,
                           self.loadOntology("OC-Found.owl"), None, None)

        self.startOntology("occommerce",
                           "OC-Commerce.owl", None,
                           self.loadOntology("OC-Commerce.owl"), None, None)

        self.startOntology("ocether",
                           "generator/ontologies/OC-Ethereum.owl", None,
                           self.loadOntology("OC-Ethereum.owl"),
                           None, None)




      #Get the IRI of OC-Found entities given their entity name
      def getOCFoundEntityByName(self, name):
         return self.ontoMap["ocfound"]["namespace"] + name

      # Get the IRI of OC-Commerce entities given their entity name
      def getOCCommerceEntityByName(self, name):
        return self.ontoMap["occommerce"]["namespace"] + name

      # Get the IRI of OC-Commerce entities given their entity name
      def getOCEthereumEntityByName(self, name):
         return self.ontoMap["ocether"]["namespace"] + name
