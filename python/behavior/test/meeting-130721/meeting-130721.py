from FacilityManager import *


file = open("meeting-130721.owl", "r")
ontology = Graph()
ontology.parse(file)

namespace =  Namespace("http://www.ngi.ontochain/ontologies/meeting.owl#")
gr = Namespace("http://purl.org/goodrelations/v1#")
blondie = Namespace("http://www.semanticblockchain.com/Blondie.owl")

ontology.bind("base", namespace)

b = FacilityManager(ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl",
                    ontology, namespace, "C:/Users/danie/PycharmProjects/POC4COMMERCE/test/meeting-210629/meeting-130721.owl")

#Creating an Apple Seller
b.createAgent("AppleProducer")
myProducerIdentity= namespace +"AppleProducerIdentity"
b.addObjPropAssertion(ontology, namespace+"AppleProducer", b.getOCFoundEntityByName("hasDigitalIdentity"), myProducerIdentity)

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

#Creating Apple SmartContract Behavior
b.addClassAssertion(ontology, namespace+"AppleProducer", b.getOCEthereumEntityByName("EthereumSmartContractAgent"))
myTokenMint = namespace+"myAppleToken"
b.addObjPropAssertion(ontology, namespace+"AppleToken", RDFS.subClassOf, b.getOCEthereumEntityByName("EthereumTokenERC721"))
b.addClassAssertion(ontology, myTokenMint, namespace+"AppleToken")
b.createAgentBehavior("SmartContractMintBehavior", "SmartContractMintGoal", "SmartContractMintTask",
                         ["SmartContractMintOperator", "mint"],
                         [],
                         [
                             ["SmartContractMintObject", "refersAsNewTo", myTokenMint]
                         ],
                         [],
                         [],
                         [])


#offering behavior
myOfferingObject= namespace + "appleOfferingResource"
b.addClassAssertion(ontology, myOfferingObject, b.getOCCommerceEntityByName("Offering"))
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
b.connectAgentToBehavior("AppleProducer", "SmartContractMintBehavior")
b.connectAgentToBehavior("AppleProducer", "AppleOfferingBehavior")
b.connectAgentToBehavior("AppleProducer", "AppleProducerBehavior")


#User Bob
b.createAgent("Bob")
bobIdentity= namespace +"BobIdentity"
b.addObjPropAssertion(ontology, namespace+"Bob", b.getOCFoundEntityByName("hasDigitalIdentity"), bobIdentity)
bobObject= namespace + "bobOfferingResource"
b.addClassAssertion(ontology, bobObject, b.getOCCommerceEntityByName("Offering"))
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
b.addObjPropAssertion(ontology, namespace+"FedexCourier", b.getOCFoundEntityByName("hasDigitalIdentity"), fedexIdentity)
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
b.addObjPropAssertion(ontology, namespace+"PaypalMoneyTransfer", b.getOCFoundEntityByName("hasDigitalIdentity"), paypalIdentity)
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
b.addClassAssertion(ontology, appleOffering, b.getOCCommerceEntityByName("Offering"))
b.addObjPropAssertion(ontology,appleOffering, b.getOCCommerceEntityByName("isOfferingAbout"), appleBatch)
#put quantity and quality information
appleOfferingPriceDetActi = namespace + "appleGoodOfferingPriceDetActivity"
appleOfferingPrice = namespace + "appleGoodOfferingPrice"


#creating the supplychain related with the offering
suppChainmanagement = namespace+"goodOffSupplyChainMan"
suppChainRelease = namespace +"goodOffSupplyChainRelease"
suppChainDelivery = namespace+"goodOffSupplyChainDelivery"
suppChainPayment = namespace+"goodOffSupplyChainPayment"

b.addClassAssertion(ontology,suppChainmanagement, b.getOCFoundEntityByName("SupplyChainManagement"))
b.addObjPropAssertion(ontology,appleOffering, b.getOCFoundEntityByName("hasSupplyChainManagement"), suppChainmanagement)
b.addObjPropAssertion(ontology, suppChainmanagement, b.getOCFoundEntityByName("hasSupplyChainActivity"), suppChainRelease)
b.addObjPropAssertion(ontology, suppChainmanagement, b.getOCFoundEntityByName("hasSupplyChainActivity"), suppChainDelivery)
b.addObjPropAssertion(ontology, suppChainmanagement, b.getOCFoundEntityByName("hasSupplyChainActivity"), suppChainPayment)

b.addClassAssertion(ontology, suppChainRelease, b.getOCFoundEntityByName("SupplyChainReleaseActivity"))
b.addObjPropAssertion(ontology, suppChainRelease, b.getOCFoundEntityByName("supplyChainActivityImplementedBy"), namespace+"AppleProducerBehavior")
b.addClassAssertion(ontology, suppChainDelivery, b.getOCFoundEntityByName("SupplyChainDeliveryActivity"))
b.addObjPropAssertion(ontology, suppChainDelivery, b.getOCFoundEntityByName("supplyChainActivityImplementedBy"), namespace+"FedexShipBehavior")
b.addClassAssertion(ontology, suppChainPayment, b.getOCFoundEntityByName("SupplyChainPaymentActivity"))
b.addObjPropAssertion(ontology, suppChainPayment, b.getOCFoundEntityByName("supplyChainActivityImplementedBy"), namespace+"PaypalMTBehavior")

b.addClassAssertion(ontology, appleOfferingPrice, b.getOCCommerceEntityByName("Price"))
b.addClassAssertion(ontology, appleOfferingPriceDetActi, b.getOCCommerceEntityByName("PriceDeterminationActivity"))
b.addObjPropAssertion(ontology, appleOfferingPriceDetActi, b.getOCCommerceEntityByName("priceDeterminationPerformedOn"), appleOffering)
b.addObjPropAssertion(ontology, appleOfferingPriceDetActi, b.getOCCommerceEntityByName("hasPriceValue"), appleOfferingPrice)
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

b.addClassAssertion(ontology, appleOffering, b.getOCCommerceEntityByName("AcceptedOffering"))

#paying for the object
payTransferringOperation = namespace +"goodOfferingMoneyTransfer"
bobPaypalAccount = namespace +"bobPaypal"
producerPaypalAccount = namespace + "producerPaypal"
b.addDataPropAssertion(ontology, payTransferringOperation, b.getOCCommerceEntityByName("hasCurrencyValue"), "1000", XSD.float)
b.addClassAssertion(ontology, namespace+"payGoodOfferingInput2", b.getOCCommerceEntityByName("PaymentSource"))
b.addClassAssertion(ontology, namespace+"payGoodOfferingInput3", b.getOCCommerceEntityByName("PaymentDestination"))
b.addClassAssertion(ontology, namespace+"payGoodOfferingInput4", b.getOCCommerceEntityByName("PayedObject"))
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

#mint token
appleBlockNum = namespace+"appleTokenBlock"
appleBlockPay = namespace+"appleTokenPayload"
appleTransactNum = namespace+"appleTokenTransaction"
b.addClassAssertion(ontology, appleBlockNum, blondie+"EthereumBlock")
b.addClassAssertion(ontology, appleBlockPay, blondie+"EthereumPayload")
b.addClassAssertion(ontology, appleBlockNum, blondie+"MessageCallEthereumTransaction")
b.addObjPropAssertion(ontology, appleBlockNum, blondie+"hasEthereumPayloadBlock", appleBlockPay)
b.addObjPropAssertion(ontology, appleBlockPay, blondie+"hasEthereumTransactionPayload", appleBlockPay)
b.addDataPropAssertion(ontology,appleBlockNum, blondie+"heightBlock","12833283", XSD.string)
b.addDataPropAssertion(ontology,appleTransactNum, blondie+"recipientEthereumTransaction","0x48bb39274511b113b14a9417bdd75ddbcbfc0a70e063be9899d9c5852cba4c56", XSD.string)
b.addObjPropAssertion(ontology, appleTransactNum, b.getOCEthereumEntityByName("introduceintroducesEthereumSmartContractExecution"), namespace+"mintAppleBatchAction")


appleBatchToken = namespace+"appleBatchToken"
appleBatchTokenFeature = namespace+"appleBatchTokenFeature"
b.addClassAssertion(ontology, appleBatchToken, namespace+"AppleToken")
b.addClassAssertion(ontology, appleBatchTokenFeature, b.getOCEthereumEntityByName("EthereumWalletOwnerEndurantFeature"))
b.addObjPropAssertion(ontology, appleBatchToken, b.getOCEthereumEntityByName("hasEthereumTokenEndurantFeature"), appleBatchTokenFeature)
b.addDataPropAssertion(ontology, appleBatchToken, b.getOCEthereumEntityByName("hasTokenID"),  "12", XSD.integer)
b.addDataPropAssertion(ontology, appleBatchTokenFeature, b.getOCEthereumEntityByName("isInTheWalletOf"),  "0x52388888888888", XSD.string)
b.addObjPropAssertion(ontology, appleBatch, b.getOCEthereumEntityByName("isDescribedByEthereumToken"), appleBatchToken)

b.createAgentAction("AppleProducer", "mintAppleBatchAction", "mintAppleBatchGoal", "mintAppleBatchTask",
                         ["mintAppleBatchOperator", "mint"],
                         [],
                         [
                             ["mintAppleBatchObject", "refersExactlyTo", appleBatchToken]
                         ],
                         [],
                         [],
                         [
                            "SmartContractMintTask",
                        [
                            ["mintAppleBatchObject", "SmartContractMintObject"]
                        ],
                        [],
                        []
                    ])
#Query testing
#b.addClassAssertion(ontology, appleBatchTokenFeature, b.getOCEthereumEntityByName("DeprecatedEthereumTokenEndurantFeature"))
#b.addClassAssertion(ontology, appleBatchToken, b.getOCEthereumEntityByName("DestroyedEthereumToken"))
file = open("meeting-130721.owl", "w")
file.write(ontology.serialize(format='xml').decode())