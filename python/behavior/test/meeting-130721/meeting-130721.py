from FacilityManager import *


file = open("meeting-130721.owl", "r")
ontology = Graph()
ontology.parse(file)

namespace =  Namespace("http://www.ngi.ontochain/ontologies/meeting.owl#")
occommerce = Namespace("http://www.ngi.ontochain/ontologies/oc-commerce.owl#")
ocfound = Namespace("http://www.ngi.ontochain/ontologies/oc-found.owl#")
gr = Namespace("http://purl.org/goodrelations/v1#")

ontology.bind("base", namespace)

b = FacilityManager(ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl")

#Creating an Apple Seller
b.createAgent("AppleProducer")
myProducerIdentity= namespace +"AppleProducerIdentity"
b.addObjPropAssertion(ontology, namespace+"AppleProducer", ocfound+"hasDigitalIdentity", myProducerIdentity)

myProducerObject= namespace + "AppleProducerResource"
b.addClassAssertion(ontology, myProducerObject, namespace + "Apple")
b.createAgentBehavior("AppleProducerBehavior", "AppleProducerGoal", "AppleProducerTask",
                         ["AppleProducerOperator", "produce"],
                         [],
                         [
                             ["AppleProducerTaskObject", "refersAsNewTo", myProducerObject]
                         ],
                         [],
                         [
                             ["AppleProducerOutput1", "refersAsNewTo", myProducerObject]
                         ],
                         [])
#offering behavior
myOfferingObject= namespace + "appleOfferingResource"
b.addClassAssertion(ontology, myOfferingObject, occommerce + "Offering")
b.createAgentBehavior("AppleOfferingBehavior", "AppleOfferingGoal", "AppleOfferingTask",
                         ["AppleOfferingOperator", "publish"],
                         [],
                         [
                             ["AppleOfferingTaskObject", "refersAsNewTo", myOfferingObject]
                         ],
                         [],
                         [
                         ],
                         [])

#connect agent to agent behavior
b.connectAgentToBehavior("AppleProducer", "AppleOfferingBehavior")
b.connectAgentToBehavior("AppleProducer", "AppleProducerBehavior")


#User Bob
b.createAgent("Bob")
bobIdentity= namespace +"BobIdentity"
b.addObjPropAssertion(ontology, namespace+"Bob", ocfound+"hasDigitalIdentity", bobIdentity)
bobObject= namespace + "bobOfferingResource"
b.addClassAssertion(ontology, bobObject, occommerce + "Offering")
b.createAgentBehavior("bobOfferingBehavior", "bobOfferingGoal", "bobOfferingTask",
                         ["bobOfferingOperator", "accept"],
                         [],
                         [
                             ["bobOfferingTaskObject", "refersAsNewTo", bobObject]
                         ],
                         [],
                         [
                         ],
                         [])
b.connectAgentToBehavior("Bob", "bobOfferingBehavior")

#Creating a shipping Agent
b.createAgent("FedexCourier")
fedexIdentity= namespace +"FedexCourierIdentity"
b.addObjPropAssertion(ontology, namespace+"FedexCourier", ocfound+"hasDigitalIdentity", fedexIdentity)
myFedexShipObject= namespace + "FedexCourierResource"
myFedexShipOutput = namespace + "FedexShipTrackCode"
b.addClassAssertion(ontology, myFedexShipObject, b.getOASISEntityByName("PhysicalAsset"))
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
paypalIdentity= namespace +"PaypalMoneyTransferIdentity"
b.addObjPropAssertion(ontology, namespace+"PaypalMoneyTransfer", ocfound+"hasDigitalIdentity", paypalIdentity)
myPaypalMTObject= namespace + "paypalResource"
myPaypalMTOutput = namespace + "PaypalReceipt"
myPaypalMTInput2= namespace + "PaypalMTAccountSource"
myPaypalMTInput3= namespace + "PaypalMTAccountDestination"
myPaypalMTInput4= namespace + "PaypalMTAssetToPayFor"
b.addClassAssertion(ontology, myPaypalMTObject, b.getOASISEntityByName("FIATCurrency"))
b.addClassAssertion(ontology, myPaypalMTInput2, namespace+"PaypalAccount")
b.addClassAssertion(ontology, myPaypalMTInput3, namespace+"PaypalAccount")
b.addClassAssertion(ontology, myPaypalMTInput4, b.getOASISEntityByName("Asset"))
b.createAgentBehavior("PaypalMTBehavior", "PaypalMTGoal", "PaypalMTTask",
                         ["PaypalMTOperator", "transfer"],
                         [],
                         [
                             ["PaypalMTObject", "refersAsNewTo", myPaypalMTObject]
                         ],
                         [
                             ["PaypalMTInput1", "refersAsNewTo", myPaypalMTObject],
                             ["PaypalMTInput2", "refersAsNewTo", myPaypalMTInput2],
                             ["PaypalMTInput3", "refersAsNewTo", myPaypalMTInput3],
                             ["PaypalMTInput4", "refersAsNewTo", myPaypalMTInput4]

                         ],
                         [
                             ["PaypalMTOutput1", "refersAsNewTo", myPaypalMTOutput]
                         ],
                         [])

#connect agent to agent behavior
b.connectAgentToBehavior("PaypalMoneyTransfer", "PaypalMTBehavior")



# producing apple
appleBatch = namespace +"appleBatch"
b.addClassAssertion(ontology, appleBatch, namespace+"Apple")
b.createAgentAction("AppleProducer", "appleBatchCreation", "appleBatchGoal", "appleBachTask",
                         ["appleBatchOperator", "produce"],
                         [],
                         [
                             ["appleBatchObject", "refersExactlyTo", appleBatch]
                         ],
                         [
                         ],
                         [
                             ["appleBatchOutput1", "refersExactlyTo", appleBatch]
                         ],
                         [
                          "AppleProducerTask",
                          [
                            ["appleBatchObject", "AppleProducerTaskObject"]
                          ],
                          [],
                          [
                              ["appleBatchOutput1", "AppleProducerOutput1"]
                          ]
                         ])

# publishing a new offer
appleOffering = namespace +"appleGoodOffering"
b.addClassAssertion(ontology, appleOffering, occommerce+"Offering")
b.addObjPropAssertion(ontology,appleOffering, occommerce+"isOfferingAbout", appleBatch)
#put quantity and quality information
appleOfferingPriceDetActi = namespace + "appleGoodOfferingPriceDetActivity"
appleOfferingPrice = namespace + "appleGoodOfferingPrice"


#creating the supplychain related with the offering
suppChainmanagement = namespace+"goodOffSupplyChainMan"
suppChainRelease = namespace +"goodOffSupplyChainRelease"
suppChainDelivery = namespace+"goodOffSupplyChainDelivery"
suppChainPayment = namespace+"goodOffSupplyChainPayment"

b.addClassAssertion(ontology,suppChainmanagement, ocfound+"SupplyChainManagement")
b.addObjPropAssertion(ontology,appleOffering, ocfound+"hasSupplyChainManagement", suppChainmanagement)
b.addObjPropAssertion(ontology, suppChainmanagement, ocfound+"hasSupplyChainActivity", suppChainRelease)
b.addObjPropAssertion(ontology, suppChainmanagement, ocfound+"hasSupplyChainActivity", suppChainDelivery)
b.addObjPropAssertion(ontology, suppChainmanagement, ocfound+"hasSupplyChainActivity", suppChainPayment)

b.addClassAssertion(ontology, suppChainRelease, ocfound+"SupplyChainReleaseActivity")
b.addObjPropAssertion(ontology, suppChainRelease, ocfound+"supplyChainActivityImplementedBy", namespace+"AppleProducerBehavior")
b.addClassAssertion(ontology, suppChainDelivery, ocfound+"SupplyChainDeliveryActivity")
b.addObjPropAssertion(ontology, suppChainDelivery, ocfound+"supplyChainActivityImplementedBy", namespace+"FedexShipBehavior")
b.addClassAssertion(ontology, suppChainPayment, ocfound+"SupplyChainPaymentActivity")
b.addObjPropAssertion(ontology, suppChainPayment, ocfound+"supplyChainActivityImplementedBy", namespace+"PaypalMTBehavior")

b.addClassAssertion(ontology, appleOfferingPrice, occommerce+"Price")
b.addClassAssertion(ontology, appleOfferingPriceDetActi, occommerce+"PriceDeterminationActivity")
b.addObjPropAssertion(ontology, appleOfferingPriceDetActi, occommerce+"priceDeterminationPerformedOn", appleOffering)
b.addObjPropAssertion(ontology, appleOfferingPriceDetActi, occommerce+"hasPriceValue", appleOfferingPrice)
b.addDataPropAssertion(ontology, appleOfferingPrice, gr+"hasCurrency", "euro", XSD.string)
b.addDataPropAssertion(ontology, appleOfferingPrice, gr+"hasCurrencyValue", "1000", XSD.float)

b.createAgentAction("AppleProducer", "appleOfferingCreation", "appleOfferingCreationGoal", "appleOfferingCreationTask",
                         ["appleOfferingCreationOperator", "publish"],
                         [],
                         [
                             ["appleOfferingCreationObject", "refersExactlyTo", appleOffering]
                         ],
                         [
                         ],
                         [

                         ],
                         [
                          "AppleOfferingTask",
                          [
                            ["appleOfferingCreationObject", "AppleOfferingTaskObject"]
                          ],
                          [],
                          [
                          ]
                         ])

file = open("meeting-130721.owl", "w")
file.write(ontology.serialize(format='xml').decode())

input("Press a key for the second phase")

#accepting the offering
b.createAgentAction("Bob", "acceptOffAction", "acceptOffGoal", "acceptOffTask",
                         ["acceptOffOperator", "accept"],
                         [],
                         [
                             ["acceptOffObject", "refersExactlyTo", appleOffering]
                         ],
                         [
                         ],
                         [
                         ],
                         [
                          "bobOfferingTask",
                          [
                            ["acceptOffObject", "bobOfferingTaskObject"]
                          ],
                          [],
                          []
                    ])

b.addClassAssertion(ontology, appleOffering, occommerce+"AcceptedOffering")

#paying for the object
payTransferringOperation = namespace +"goodOfferingMoneyTransfer"
bobPaypalAccount = namespace +"bobPaypal"
producerPaypalAccount = namespace + "producerPaypal"
b.addDataPropAssertion(ontology, payTransferringOperation, occommerce+"hasCurrencyValue", "1000", XSD.float)
b.addClassAssertion(ontology, namespace+"payGoodOfferingInput2", occommerce+"PaymentSource")
b.addClassAssertion(ontology, namespace+"payGoodOfferingInput3", occommerce+"PaymentDestination")
b.addClassAssertion(ontology, namespace+"payGoodOfferingInput4", occommerce+"PayedObject")
b.createAgentAction("PaypalMoneyTransfer", "payGoodOfferingAction", "payGoodOfferingGoal", "payGoodOfferingTask",
                         ["payGoodOfferingOperator", "transfer"],
                         [],
                         [
                             ["payGoodOfferingObject", "refersExactlyTo", payTransferringOperation]
                         ],
                         [
                            ["payGoodOfferingInput1", "refersExactlyTo", payTransferringOperation],
                            ["payGoodOfferingInput2", "refersExactlyTo", bobPaypalAccount],
                            ["payGoodOfferingInput3", "refersExactlyTo", producerPaypalAccount],
                            ["payGoodOfferingInput4", "refersExactlyTo", appleBatch]
                         ],
                         [
                             ["payGoodOfferingOutput1", "refersExactlyTo", payTransferringOperation]
                         ],
                         [
                          "PaypalMTTask",
                          [
                            ["payGoodOfferingObject", "PaypalMTObject"]
                          ],
                          [
                              ["payGoodOfferingInput1", "PaypalMTInput1"],
                              ["payGoodOfferingInput2", "PaypalMTInput2"],
                              ["payGoodOfferingInput3", "PaypalMTInput3"],
                              ["payGoodOfferingInput4", "PaypalMTInput4"]
                          ],
                          [
                              ["payGoodOfferingOutput1", "PaypalMTOutput1"]
                          ]
                         ])


shipGoodOfferingReceipt=namespace+"shipGoodOfferingReceipt-track"
b.createAgentAction("FedexCourier", "shipGoodOfferingAction", "shipGoodOfferingGoal", "shipGoodOfferingTask",
                         ["shipGoodOfferingOperator", "ship"],
                         [],
                         [
                            ["shipGoodOfferingObject", "refersExactlyTo", appleBatch]
                         ],
                         [
                             ["shipGoodOfferingInput1", "refersExactlyTo", appleBatch]
                         ],
                         [
                             ["shipGoodOfferingOutput", "refersExactlyTo", shipGoodOfferingReceipt]
                         ],
                         [
                          "FedexShipTask",
                          [
                            ["shipGoodOfferingObject", "FedexShipObject"]
                          ],
                          ["shipGoodOfferingInput1", "FedexShipInput"],
                          ["shipGoodOfferingOutput","FedexShipOutput1"]
                    ])


file = open("meeting-130721.owl", "w")
file.write(ontology.serialize(format='xml').decode())