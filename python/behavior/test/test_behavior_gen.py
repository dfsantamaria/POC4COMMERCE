from FacilityManager import *

#test
#create a fresh ontology for the agent
namespace =  Namespace("http://www.ontochain.org/myOntology#")
ontology=Graph()
ontology.bind("base", namespace)


#create a fresh ontology for the agent template
namespaceTemp =  Namespace("http://www.ontochain.org/myOntologyTemplate#")
ontologyTemp=Graph()
ontologyTemp.bind("base", namespaceTemp)

#create a fresh ontology for the agent actions
namespaceAct = Namespace("http://www.ontochain.org/myOntologyActions#")
ontologyAct=Graph()
ontologyAct.bind("base", namespaceAct)

# Create the graph
b = FacilityManager(ontology, namespace, None,
                    ontologyTemp, namespaceTemp, None,
                    ontologyAct, namespaceAct, None)


#import OASIS into the current ontology
b.addImportOASIS(ontology, namespace)
b.addImportOASIS(ontologyTemp, namespaceTemp)
b.addImportOASIS(ontologyAct, namespaceAct)


#create agent template
agentTemplateName=b.createAgentTemplate("MyAgentBehaviorTemplate")
#create behavior template
object1 = "http://www.ontochain.org/myOntologyTemplate#template-object-entity-1"
input1 = "http://www.ontochain.org/myOntologyTemplate#template-input-entity-1"
output1 = "http://www.ontochain.org/myOntologyTemplate#template-output-entity-1"
b.createAgentBehaviorTemplate("MyTemplateBehavior", "MyTemplateGoal", "MyTemplateTask",
                         ["MyTemplateTaskOperator", "turn"],
                         ["MyTemplateOperatorArgument", "off"],
                         [
                             ["MyTemplateTaskObject","refersAsNewTo", object1 ]
                         ],
                         [
                             ["MyTemplateInput1", "refersAsNewTo", input1]
                         ],
                         [
                             ["MyTemplateOutput1", "refersAsNewTo", output1]
                         ])
#connect agent to agent behavior
b.connectAgentTemplateToBehavior("MyAgentBehaviorTemplate", "MyTemplateBehavior")


#Crate agent
b.createAgent("MyAgent")
#create agent behavior
agentobject1 = "http://www.ontochain.org/myOntology#agent-object-entity-1"
agentinput1 = "http://www.ontochain.org/myOntology#agent-input-entity-1"
agentoutput1 = "http://www.ontochain.org/myOntology#agent-output-entity-1"
b.createAgentBehavior("MyAgentBehavior", "MyAgentGoal", "MyAgentTask",
                         ["MyAgentTaskOperator", "turn"],
                         ["MyAgentOperatorArgument", "off"],
                         [
                             ["MyAgentTaskObject", "refersAsNewTo", agentobject1]
                         ],
                         [
                             ["MyAgentInput1", "refersAsNewTo", agentinput1]
                         ],
                         [
                             ["MyAgentOutput1", "refersAsNewTo", agentoutput1]
                         ],
                         [
                          "MyTemplateTask",
                          [
                              ["MyAgentTaskObject", "MyTemplateTaskObject"]
                          ],
                          [
                              ["MyAgentInput1", "MyTemplateInput1"]
                          ],
                          [
                              ["MyAgentOutput1", "MyTemplateOutput1"]
                          ]
                         ])
#connect agent to agent behavior
b.connectAgentToBehavior("MyAgent", "MyAgentBehavior")



executionobject1 = "http://www.ontochain.org/myExecOntology#execution-object-entity-1"
executioninput1 = "http://www.ontochain.org/myExecOntology#execution-input-entity-1"
executionoutput1 = "http://www.ontochain.org/myExecOntology#execution-output-entity-1"
#creating agent action
b.createAgentAction("MyAgent", "planExecution", "executionGoal", "executionTask",
                         ["executionOperator", "turn"],
                         ["executionArgument", "off"],
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
                          "MyAgentTask",
                          [
                              ["executionObject", "MyAgentTaskObject"]
                          ],
                          [
                              ["executionInput1", "MyAgentInput1"]
                          ],
                          [
                              ["executionOutput1", "MyAgentOutput1"]
                          ]
                         ])



#serialization
print(ontology.serialize(format="turtle").decode("utf-8"))
print("######################################################")
print(ontologyTemp.serialize(format="turtle").decode("utf-8"))
print("######################################################")
print(ontologyAct.serialize(format="turtle").decode("utf-8"))
#saving
file = open("ontologies/agent.owl", "w")
file.write(ontology.serialize(format='xml').decode())

file = open("ontologies/agentTemplate.owl", "w")
file.write(ontologyTemp.serialize(format='xml').decode())

file = open("ontologies/agentAction.owl", "w")
file.write(ontologyAct.serialize(format='xml').decode())