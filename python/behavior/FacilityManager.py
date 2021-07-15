from OASIS_behavior_generator import *

class FacilityManager(BehaviorManager):
      def __init__(self, ontologyGraph, ontologyNamespace, ontologyURL,
                   ontologyTemplateGraph, ontologyTemplateNamespace, templateURL,
                   actionGraph, actionNamespace, actionURL):
        BehaviorManager.__init__(self, ontologyGraph, ontologyNamespace, ontologyURL,
                                 ontologyTemplateGraph, ontologyTemplateNamespace, templateURL,
                                 actionGraph, actionNamespace, actionURL,
                                 None, None, None)

        self.startOntology("ocfound", "https://www.dmi.unict.it/santamaria/projects/oasis/sources/ontochain/OC-Found.owl", None,
                           self.loadOntology("https://www.dmi.unict.it/santamaria/projects/oasis/sources/ontochain/OC-Found.owl"), None, None)

        self.startOntology("occommerce",
                           "https://www.dmi.unict.it/santamaria/projects/oasis/sources/ontochain/OC-Commerce.owl", None,
                           self.loadOntology("https://www.dmi.unict.it/santamaria/projects/oasis/sources/ontochain/OC-Commerce.owl"), None, None)

        self.startOntology("ocether",
                           "https://www.dmi.unict.it/santamaria/projects/oasis/sources/ontochain/OC-Ethereum.owl", None,
                           self.loadOntology("https://www.dmi.unict.it/santamaria/projects/oasis/sources/ontochain/OC-Ethereum.owl"),
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
