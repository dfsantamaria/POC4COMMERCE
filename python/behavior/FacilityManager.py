from OASIS_behavior_generator import *

class FacilityManager(BehaviorManager):
      def __init__(self, ontologyGraph, ontologyNamespace, ontologyURL, ontologyTemplateGraph,
                   ontologyTemplateNamespace, templateURL,
                   actionGraph, actionNamespace, actionURL):
        BehaviorManager.__init__(self, ontologyGraph, ontologyNamespace, ontologyURL,
                                 ontologyTemplateGraph, ontologyTemplateNamespace, templateURL,
                                 actionGraph, actionNamespace, actionURL)

        self.addOntoMap("ocfound", "https://www.dmi.unict.it/santamaria/projects/oasis/sources/ontochain/OC-Found.owl", None, None)
        self.ontologies.append(self.loadOntology(self.ontoMap["ocfound"]["url"]))





