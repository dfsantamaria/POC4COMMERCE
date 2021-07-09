from FacilityManager import *


file = open("meeting-130721.owl", "r")
ontology = Graph()
ontology.parse(file)

namespace =  Namespace("http://www.ngi.ontochain/ontologies/meeting.owl#")

ontology.bind("base", namespace)

b = FacilityManager(ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl")

#Creating an Apple Seller
b.createAgent("AppleProducer")
myProducerObject= namespace + "AppleProducerResource"
b.addClassAssertion(ontology, myProducerObject, b.getOASISEntityByName("Asset"))
b.createAgentBehavior("AppleProducerBehavior", "AppleProducerGoal", "AppleProducerTask",
                         ["AppleProducerOperator", "produce"],
                         [],
                         [
                             ["AppleProducerTaskObject", "refersAsNewTo", myProducerObject]
                         ],
                         [],
                         [
                             ["MyQualityValuerOutput1", "refersAsNewTo", myProducerObject]
                         ],
                         [])
#connect agent to agent behavior
b.connectAgentToBehavior("AppleProducer", "AppleProducerBehavior")

#Creating a shipping Seller
b.createAgent("FedexCourier")
myFedexShipObject= namespace + "FexedCourierResource"
myFedexShipOutput = namespace + "FedexShipTrackCode"
b.addClassAssertion(ontology, myFedexShipObject, b.getOASISEntityByName("Asset"))
b.createAgentBehavior("FedexShipBehavior", "FedexShipGoal", "FedexShipTask",
                         ["FedexShipOperator", "ship"],
                         [],
                         [
                             ["FedexShipObject", "refersAsNewTo", myFedexShipObject]
                         ],
                         [
                             ["FedexShipInput", "refersAsNewTo", myFedexShipObject]
                         ],
                         [
                             ["FedexShipOutput1", "refersAsNewTo", myFedexShipOutput]
                         ],
                         [])
#connect agent to agent behavior
b.connectAgentToBehavior("FedexCourier", "FedexShipBehavior")

#Creating a transfer money agent
b.createAgent("PaypalMoneyTransfer")
myPaypalMTObject= namespace + "paypalResource"
myPaypalMTOutput = namespace + "PaypalReceipt"
myPaypalMTInput2= namespace + "PaypalMTAccountSource"
myPaypalMTInput3= namespace + "PaypalMTAccountDestination"
b.addClassAssertion(ontology, myPaypalMTObject, b.getOASISEntityByName("FIATCurrency"))
b.addClassAssertion(ontology, myPaypalMTInput2, namespace+"PaypalAccount")
b.addClassAssertion(ontology, myPaypalMTInput3, namespace+"PaypalAccount")
b.createAgentBehavior("PaypalMTBehavior", "PaypalMTGoal", "PaypalMTTask",
                         ["PaypalMTOperator", "transfer"],
                         [],
                         [
                             ["FedexShipObject", "refersAsNewTo", myPaypalMTObject]
                         ],
                         [
                             ["PaypalMTInput1", "refersAsNewTo", myFedexShipObject],
                             ["PaypalMTInput2", "refersAsNewTo", myPaypalMTInput2],
                             ["PaypalMTInput3", "refersAsNewTo", myPaypalMTInput3]

                         ],
                         [
                             ["PaypalMTOutput1", "refersAsNewTo", myPaypalMTOutput]
                         ],
                         [])
#connect agent to agent behavior
b.connectAgentToBehavior("PaypalMoneyTransfer", "PayaplMTBehavior")
file = open("meeting-130721.owl", "w")
file.write(ontology.serialize(format='xml').decode())
