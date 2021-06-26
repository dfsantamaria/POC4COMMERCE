from OASIS_behavior_generator import *

file = open("OC-Found.owl", "r")
ontology = Graph()
ontology.parse(file)

namespace =  Namespace("http://www.ngi.ontochain/ontologies/oc-found.owl#")

ontology.bind("base", namespace)
ontology.bind("owl","http://www.w3.org/2002/07/owl#")


b = BehaviorManager(ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/OC-Found.owl", ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/OC-Found.owl")

valuerObject=namespace+"evaluationObject"
valuerInput=namespace+"objectAsset"

b.addClassAssertion(ontology, valuerObject, namespace+"QualityValuation")
b.addClassAssertion(ontology, valuerInput, b.getOASISEntityByName("Asset"))

#Valuer Template Creation
b.createAgentBehaviorTemplate("ValuerTemplateBehavior", "ValuerTemplateGoal", "ValuerTemplateTask",
                         ["ValuerTemplateTaskOperator", "compute"],
                         ["ValuerTemplateTaskOperatorArgument", "quality_evaluation"],
                         [
                             ["ValuerTemplateTaskObject","refersAsNewTo", valuerObject]
                         ],
                         [
                             ["ValuerTemplateTaskInput1", "refersAsNewTo", valuerInput]
                         ],
                         [
                             ["ValuerTemplateTaskOutput1", "refersAsNewTo", valuerObject]
                         ])
agentTemplateName=b.createAgentTemplate("ValuerAgentBehaviorTemplate")
b.connectAgentTemplateToBehavior("ValuerAgentBehaviorTemplate","ValuerTemplateBehavior")

file = open("OC-Found.owl", "w")
file.write(ontology.serialize(format='xml').decode())
