import os

class Query:
     def __init__(self, *args):
         self.prefix=[]
         self.query=None
         self.param=None
         self.columns=None
         if len(args) > 0:
             if args[0] is not None:
                for p in args[0]:
                    self.__addPrefix__(p)
             if len(args) > 1:
               self.query=args[1]
               if len(args) > 2:
                  self.param=args[2]


     def buildPrefix(self):
         head=""
         for p in self.prefix:
             head=head + "PREFIX "+ p[0] +": <"+p[1]+">" + os.linesep
         return head

     def __addPrefix__(self, _prefixMap):
         for p in self.prefix:
             if p[0] is _prefixMap[0] or p[1] is _prefixMap[1]:
                return
         self.prefix.append((_prefixMap[0],_prefixMap[1]))

     def addPrefix(self, _prefixMap):
         for p in _prefixMap:
             self.__addPrefix__(p)

     def build(self):
         return self.buildPrefix() + self.buildBody()

     def buildBody(self):
         if self.param is not None:
            toreturn=self.query
            for p in self.param:
               toreturn=toreturn.replace(p[0],p[1])
            return toreturn
         return self.query

     def getQuery(self):
         return self.query

     def getParameters(self):
         return self.param

     def setColumns(self, cols):
         self.colums=cols

     def getColumns(self):
         return self.colums

class QueryQF1(Query):
    def __init__(self, prefix):
        super().__init__(prefix, "SELECT DISTINCT ?agent ?identity ?operation ?operationOn WHERE { ?agent ocfound:hasDigitalIdentity ?identity. ?agent oasis:hasBehavior ?behavior."+
                                    " ?behavior oasis:consistsOfGoalDescription ?goal. ?goal oasis:consistsOfTaskDescription ?task. ?task oasis:hasTaskOperator ?operator. ?operator oasis:refersExactlyTo ?operation."+
                                    " ?task oasis:hasTaskObject ?object. ?object oasis:refersAsNewTo ?ob. ?ob a ?operationOn  FILTER( ?operationOn != owl:NamedIndividual) }")


class QueryQF2(Query):
    def __init__(self, prefix):
        super().__init__(prefix, "SELECT DISTINCT ?agent ?operation ?operationOn ?typeOf	WHERE { ?agent oasis:performs ?agentExe.  ?agentExe oasis:hasTaskObject ?taskExe.  ?agentExe oasis:hasTaskOperator ?operator."+
                   " ?operator oasis:refersExactlyTo ?operation. ?taskExe oasis:refersExactlyTo ?operationOn. ?operationOn a ?typeOf.  FILTER( ?typeOf != owl:NamedIndividual) }")

class QueryQF3(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT ?supplychain WHERE { ?x ocfound:hasSupplyChainManagement ?supplychain .}", param)



class QueryQF4(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT ?supplychainActivity WHERE { ?x ocfound:hasSupplyChainManagement ?supplychain. ?supplychain ocfound:hasSupplyChainActivity ?supplychainActivity. }", param)


class QueryQF5(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT ?agent ?supplychainActivity WHERE { ?x ocfound:hasSupplyChainManagement ?supplychain. ?supplychain ocfound:hasSupplyChainActivity ?supplychainActivity. ?supplychainActivity ocfound:supplyChainActivityImplementedBy ?behavior."+
                                   " ?behavior a oasis:Behavior. ?agent oasis:hasBehavior ?behavior.}", param)


class QueryQF6(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT DISTINCT ?agent ?score WHERE { ?agent oasis:performs ?agentExe. ?agentExe oasis:hasTaskObject ?taskExe. ?agentExe oasis:hasTaskOperator ?operator. ?operator oasis:refersExactlyTo oabox:perform."+
                                   " ?taskExe oasis:refersExactlyTo ?qualityValuation. ?qualityValuation a ocfound:QualityValuationActivity. ?qualityValuation ocfound:hasQualityValuationResult ?result. ?qualityValuation ocfound:qualityValuationPerformedOn ?x ."+
                                   " ?result ocfound:hasValuationValue ?score.}", param)


class QueryQF7(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT (AVG(?score) AS ?AverageScore) (COUNT(?agent) AS ?numberOfValuation) WHERE { ?agent oasis:performs ?agentExe. ?agentExe oasis:hasTaskObject ?taskExe. ?agentExe oasis:hasTaskOperator ?operator."+
                                  " ?operator oasis:refersExactlyTo oabox:perform. ?taskExe oasis:refersExactlyTo ?qualityValuation. ?qualityValuation a ocfound:QualityValuationActivity. ?qualityValuation ocfound:hasQualityValuationResult ?result."+
                                  " ?qualityValuation ocfound:qualityValuationPerformedOn ?x . ?result ocfound:hasValuationValue ?score.}", param)


class QueryQC1(Query):
    def __init__(self, prefix):
        super().__init__(prefix, "SELECT DISTINCT ?offering ?type ?value ?currency  WHERE { ?taskExec a oasis:TaskExecution. ?taskExec oasis:hasTaskObject ?taskob.  ?taskob oasis:refersExactlyTo ?offering."+
                                " ?offering a ?offer.  FILTER(?offer = occom:Offering)   FILTER NOT EXISTS { ?offering a occom:DeprecatedOffering.}   FILTER NOT EXISTS { ?offering a occom:ClosedOffering.}"+
                                " FILTER NOT EXISTS { ?offering a occom:RetractedOffering.} ?offering occom:isOfferingAbout ?product.  ?product a ?type.   FILTER( ?type != owl:NamedIndividual)"+
                                " ?priceDetActivity occom:priceDeterminationPerformedOn ?offering.  ?priceDetActivity occom:hasPriceValue ?price.   ?price gr:hasCurrencyValue ?value. ?price gr:hasCurrency ?currency.  }")


class QueryQC2(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT DISTINCT ?chainActivity ?type ?agent WHERE { ?x "+
                                  " ocfound:hasSupplyChainManagement ?chainManagement. ?chainManagement ocfound:hasSupplyChainActivity ?chainActivity. ?chainActivity a ?type."+
                                  " FILTER( ?type != owl:NamedIndividual) ?chainActivity ocfound:supplyChainActivityImplementedBy ?behavior. ?agent oasis:hasBehavior ?behavior.}", param)


class QueryQC3(Query):
    def __init__(self,prefix):
        super().__init__(prefix, "SELECT ?agent ?offering ?accepted WHERE { ?agent oasis:performs ?agentExe. ?agentExe oasis:hasTaskObject ?taskExe. ?agentExe oasis:hasTaskOperator ?operator."+
                                " ?operator oasis:refersExactlyTo oabox:accept. ?taskExe oasis:refersExactlyTo ?offering. ?offering a ?accepted. FILTER( ?accepted = occom:AcceptedOffering)}")


class QueryQE1(Query):
    def __init__(self,prefix):
        super().__init__(prefix, "SELECT  ?agent ?token ?tokentype ?asset ?owner WHERE { ?agent oasis:performs ?agentExe. ?agentExe oasis:hasTaskObject ?taskExe. ?agentExe oasis:hasTaskOperator ?operator."+
                                " ?operator oasis:refersExactlyTo oabox:mint. ?taskExe oasis:refersExactlyTo ?token.  ?operationOn a ?tokentype.  ?tokenType rdfs:subClassOf ocether:EthereumTokenERC721."+
                                " FILTER( ?tokentype != owl:NamedIndividual)  FILTER NOT EXISTS { ?operationOn a ocether:BurnedEthereumToken}  ?asset ocether:isDescribedByEthereumToken ?operationOn."+
                                " ?token ocether:hasEthereumTokenEndurantFeature ?feature.  ?feature a ?ownerFeature.  FILTER(?ownerFeature = ocether:EthereumWalletOwnerEndurantFeature)"+
                                " FILTER NOT EXISTS {?feature a ocether:DeprecatedEthereumTokenEndurantFeature.}  ?feature ocether:isInTheWalletOf ?owner.  }")


class QueryQE2(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT ?blockNumber ?hash WHERE { ?block blon:heightBlock ?blockNumber. ?block blon:hasEthereumPayloadBlock ?payload. ?payload blon:hasEthereumTransactionPayload ?transaction."+
                                  " ?transaction blon:recipientEthereumTransaction ?hash. ?transaction ocether:introducesEthereumSmartContractExecution ?action. ?action oasis:consistsOfGoalExecution ?goal."+
                                  " ?goal oasis:consistsOfTaskExecution ?agentExe. ?agent oasis:performs ?agentExe. ?agentExe oasis:hasTaskObject ?taskExe. ?agentExe oasis:hasTaskOperator ?operator."+
                                  " ?operator oasis:refersExactlyTo oabox:mint. ?taskExe oasis:refersExactlyTo ?x .}", param)


class QueryQE3(Query):
    def __init__(self, prefix, param):
        super().__init__(prefix, "SELECT DISTINCT ?agent ?hash ?address WHERE { ?agent oasis:performs ?agentExe. ?agentExe oasis:hasTaskObject ?taskExe."+
                                  " ?agentExe oasis:hasTaskOperator ?operator. ?operator oasis:refersExactlyTo oabox:mint. ?taskExe oasis:refersExactlyTo ?token."+
                                  " ?asset ocether:isDescribedByEthereumToken ?token. ?asset a ?x. ?block blon:heightBlock ?blockNumber. ?block blon:hasEthereumPayloadBlock ?payload."+
                                  " ?payload blon:hasEthereumTransactionPayload ?transaction. ?transaction blon:recipientEthereumTransaction ?hash. ?transaction ocether:introducesEthereumSmartContractAgent ?agent."+
                                  " ?transaction blon:to ?address.}", param)



class QueryQE4(Query):
    def __init__(self,prefix):
        super().__init__(prefix, "SELECT   ?owner (COUNT(?operationOn) as ?tokenCounter) ?assetType   WHERE { ?asset a ?assetType. FILTER(?assetType != owl:NamedIndividual)."+
                                "?asset ocether:isDescribedByEthereumToken ?operationOn. ?token ocether:hasEthereumTokenEndurantFeature ?feature. ?feature a ?ownerFeature."+
                                "FILTER(?ownerFeature = ocether:EthereumWalletOwnerEndurantFeature)  FILTER NOT EXISTS {?feature a ocether:DeprecatedEthereumTokenEndurantFeature.}"+
                                "?feature ocether:isInTheWalletOf ?owner.   }  GROUP BY ?assetType ?owner")

