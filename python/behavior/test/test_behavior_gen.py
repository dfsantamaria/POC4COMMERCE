from OASIS_behavior_generator import *

#test
#create a fresh ontology for the agent
namespace =  Namespace("http://www.ontochain.org/myOntology#")
ontology=Graph()
ontology.bind("base", namespace)
ontology.bind("owl","http://www.w3.org/2002/07/owl#")

#create a fresh ontology for the agent template
namespaceTemp =  Namespace("http://www.ontochain.org/myOntologyTemplate#")
ontologyTemp=Graph()
ontologyTemp.bind("base", namespaceTemp)
ontologyTemp.bind("owl","http://www.w3.org/2002/07/owl#")

# Create the graph
b = Behavior(ontology, namespace, ontologyTemp, namespaceTemp)



#import OASIS into the current ontology
b.addImportOASIS(ontology, namespace)
b.addImportOASIS(ontologyTemp, namespaceTemp)


#create agent template
agentTemplateName=b.createAgentTemplate("MyAgentBehaviorTemplate")
#create behavior template
object1 = "http://www.ontochain.org/myOntologyTemplate#object-entity-1"
input1 = "http://www.ontochain.org/myOntologyTemplate#input-entity-1"
output1 = "http://www.ontochain.org/myOntologyTemplate#output-entity-1"
b.createBehaviorTemplate("MyBehavior", "MyGoal", "MyTask",
                         ["MyTaskOperator", "turn"],
                         ["MyOperatorArgument", "off"],
                         [
                             ["MyTaskObject","refersAsNewTo", object1 ]
                         ],
                         [
                             ["MyInput1", "refersAsNewTo", input1]
                         ],
                         [
                             ["MyOutput1", "refersAsNewTo", output1]
                         ])
#connect agent to agent behavior
b.connectAgentToBehaviorTemplate("MyAgentBehaviorTemplate", "MyBehavior")


#Crate agent
b.createAgent("MyAgent")
print(ontology.serialize(format="turtle").decode("utf-8"))
print("######################################################")
print(ontologyTemp.serialize(format="turtle").decode("utf-8"))


#save
file = open("agent.owl", "w")
file.write(ontology.serialize(format='xml').decode())

file = open("agentTemplate.owl", "w")
file.write(ontologyTemp.serialize(format='xml').decode())
