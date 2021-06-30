from FacilityManager import *


file = open("meeting-210629.owl", "r")
ontology = Graph()
ontology.parse(file)

namespace =  Namespace("http://www.ngi.ontochain/ontologies/meeting.owl#")

ontology.bind("base", namespace)
ontology.bind("owl","http://www.w3.org/2002/07/owl#")


b = FacilityManager(ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-210629.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-210629.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-210629.owl")

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




#Creating a new agent
b.createAgent("MyQualityValuer")
myValuerObject=namespace+"myValuerEvaluationObject"
myValuerInput=namespace+"myValuerObjectAsset"
b.addClassAssertion(ontology, myValuerObject, namespace+"QualityValuation")
b.addClassAssertion(ontology, myValuerInput, b.getOASISEntityByName("Asset"))

b.addClassAssertion(ontology, myValuerObject, namespace+"QualityValuation")
b.addClassAssertion(ontology, myValuerInput, b.getOASISEntityByName("Asset"))
b.createAgentBehavior("MyQualityValuerBehavior", "MyQualityValuerGoal", "MyQualityValuerTask",
                         ["MyQualityValuerTaskOperator", "compute"],
                         ["MyQualityValuerArgument", "quality_valuation"],
                         [
                             ["MyQualityValuerTaskObject", "refersAsNewTo", myValuerObject]
                         ],
                         [
                             ["MyQualityValuerInput1", "refersAsNewTo", myValuerInput]
                         ],
                         [
                             ["MyQualityValuerOutput1", "refersAsNewTo", myValuerObject]
                         ],
                         [
                          "ValuerTemplateTask",
                          [
                              ["MyQualityValuerTaskObject", "ValuerTemplateTaskObject"]
                          ],
                          [
                              ["MyQualityValuerInput1", "ValuerTemplateTaskInput1"]
                          ],
                          [
                              ["MyQualityValuerOutput1", "ValuerTemplateTaskOutput1"]
                          ]
                         ])
#connect agent to agent behavior
b.connectAgentToBehavior("MyQualityValuer", "MyQualityValuerBehavior")


#connect action to agent
#creating agent action
executionobject1 = namespace+"execution-object-entity-1"
executioninput1 = namespace+"execution-input-entity-1"
executionoutput1 = namespace+"execution-output-entity-1"
b.createAgentAction("MyQualityValuer", "planExecution", "executionGoal", "executionTask",
                         ["executionOperator", "compute"],
                         ["executionArgument", "quality_valuation"],
                         [
                             ["executionObject", "refersExactlyTo", executionobject1]
                         ],
                         [
                             ["executionInput1", "refersExactlyTo", executioninput1]
                         ],
                         [
                             ["executionOutput1", "refersExactlyTo", executionoutput1]
                         ],
                         [
                          "MyQualityValuerTask",
                          [
                              ["executionObject", "MyQualityValuerTaskObject"]
                          ],
                          [
                              ["executionInput1", "MyQualityValuerInput1"]
                          ],
                          [
                              ["executionOutput1", "MyQualityValuerOutput1"]
                          ]
                         ])





file = open("meeting-210629.owl", "w")
file.write(ontology.serialize(format='xml').decode())
