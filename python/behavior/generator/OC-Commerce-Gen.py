from OASIS_behavior_generator import *

file = open("ontologies/OC-Commerce.owl", "r")
ontology = Graph()
ontology.parse(file)
namespace =  Namespace("http://www.ngi.ontochain/ontologies/oc-found.owl#")
ontology.bind("base", namespace)

b = BehaviorManager(ontology, namespace, "ontologies/OC-Commerce.owl",
                    ontology, namespace, "ontologies/OC-Commerce.owl",
                    None, None, None,
                    None, None, None)

valuerObject=namespace+"offeringObject"
valuerInput=namespace+"objectAsset"

b.addClassAssertion(ontology, valuerObject, namespace+"Offering")
b.addClassAssertion(ontology, valuerInput, b.getOASISEntityByName("Asset"))

#Valuer Template Creation
b.createAgentBehaviorTemplate("PublishOfferingTemplateBehavior", "PublishOfferingTemplateGoal", "PublishOfferingTemplateTask",
                         ["PublishOfferingTemplateTaskOperator", "publish"],
                         ["PublishOfferingOperatorArgument", "offering"],
                         [
                             ["PublishOfferingTemplateTaskObject", "refersAsNewTo", valuerObject]
                         ],
                         [
                             ["PublishOfferingTemplateTaskInput1", "refersAsNewTo", valuerInput]
                         ],
                         [
                             ["PublishOfferingTaskOutput1", "refersAsNewTo", valuerObject]
                         ])

agentTemplateName=b.createAgentTemplate("CommercialAgentBehaviorTemplate")

b.connectAgentTemplateToBehavior("CommercialAgentBehaviorTemplate","PublishOfferingTemplateBehavior")

file = open("ontologies/OC-Commerce.owl", "w")
file.write(ontology.serialize(format='xml').decode())
