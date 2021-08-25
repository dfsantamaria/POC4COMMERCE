from owlready2 import *
from OCCSE.QueryBuilderModule import *
import json

class OCCSE:
    def __init__(self, *args):
        self.prefix = [
                  ("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
                  ("owl", "http://www.w3.org/2002/07/owl#"),
                  ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
                  ("xsd", "http://www.w3.org/2001/XMLSchema#"),
                  ("oabox", "http://www.dmi.unict.it/oasis-abox.owl#"),
                  ("oasis", "http://www.dmi.unict.it/oasis.owl#"),
                  ("occom", "http://www.ngi.ontochain/ontologies/oc-commerce.owl#"),
                  ("ocfound", "http://www.ngi.ontochain/ontologies/oc-found.owl#"),
                  ("ocether", "http://www.ngi.ontochain/ontologies/oc-ethereum.owl#"),
                  ("gr", "http://purl.org/goodrelations/v1#"),
                  ("blon", "http://www.semanticblockchain.com/Blondie.owl#")]
        self.repositoryManager = None
        self.reasonerInterface = None
        self.world = None
        self.reasonerStatus=False
        self.repositoryStatus=False
        if len(args)==2:
            self.__construct2__(args[0], args[1])

    def __construct2__(self,repository, reasoner):
        self.repositoryManager=repository
        self.reasonerInterface=reasoner

    def loadRepository(self):
        self.world=World()
        for rep in self.repositoryManager.getRepository():
            self.world.get_ontology(rep).load()
        self.repositoryManager.resetChanged()
        self.__resetIsRepositoryLoaded__(True)
        self.__resetIsSyncReasoner__(False)

    def syncReasoner(self):
        if self.isRepositoryLoaded():
           self.reasonerInterface.runReasoner(self.world)
           self.__resetIsSyncReasoner__(True)

    def __checkRepository__(self):
        if self.repositoryManager.isRepositoryChanged():
            self.loadRepository()

    def __resetIsSyncReasoner__(self, value):
        self.reasonerStatus = value

    def __resetIsRepositoryLoaded__(self, value):
        self.repositoryStatus = value

    def isReasonerSyncronized(self):
        return self.reasonerStatus

    def isRepositoryLoaded(self):
        return self.repositoryStatus

    def __checkReasoner__(self):
        if self.isReasonerSyncronized() == False:
           self.syncReasoner()
           self.__resetIsSyncReasoner__(True)

    def addPrefixes(self, prefixes):
        for p in prefixes:
           self.prefix.append(p)

    def removePrefixes(self, prefixes):
        for p in prefixes:
            if p in self.prefix:
               self.prefix.remove(p)

    def getPrefixes(self):
        return self.prefix

    def buildPrefix(self):
        head = ""
        for p in self.prefix:
            head = head + "PREFIX " + p[0] + ": <" + p[1] + ">" + os.linesep
        return head

    def performQuery(self, query):
        query.addPrefix(self.getPrefixes())
        return self.__performQuery__(query)

    def __performQuery__(self, query):
        self.__checkRepository__()
        self.__checkReasoner__()
        return self.world.sparql(query.build())

    def getQuery(self, query):
        return self.buildPrefix()+ query.build()

    def toJson(self, result):
        result=list(result)
        jsonlist= []
        for i, val in enumerate(result):
            jsonlist.append(["r"+str(i)+":",  str(self.__toJsonResult__(result[i]))])
        return json.dumps(jsonlist)

    def __toJsonResult__(self, result):
        toreturn =[]
        for r in result:
            toreturn.append(str(r))
        return toreturn


    def performQueryQF1(self, prefixes):
        return self.__performQuery__(QueryQF1(self.getPrefixes()+prefixes))

    def performQueryQF2(self, prefixes):
        return self.__performQuery__(QueryQF2(self.getPrefixes()+ prefixes))

    def performQueryQF3(self, prefixes, param):
        return self.__performQuery__(QueryQF3(self.getPrefixes() + prefixes, [("?x",param)]))

    def performQueryQF4(self, prefixes, param):
        return self.__performQuery__(QueryQF4(self.getPrefixes() + prefixes, [("?x",param)]))

    def performQueryQF5(self, prefixes, param):
        return self.__performQuery__(QueryQF5(self.getPrefixes() + prefixes, [("?x",param)]))

    def performQueryQF6(self, prefixes,  param):
        return self.__performQuery__(QueryQF6(self.getPrefixes() + prefixes, [("?x",param)]))

    def performQueryQF7(self, prefixes ,param):
        return self.__performQuery__(QueryQF7(self.getPrefixes()+ prefixes, [("?x",param)]))

    def performQueryQC1(self, prefixes):
        return self.__performQuery__(QueryQC1(self.getPrefixes() + prefixes))

    def performQueryQC2(self, prefixes, param):
        return self.__performQuery__(QueryQC2(self.getPrefixes() + prefixes, [("?x",param)]))

    def performQueryQC3(self, prefixes):
        return self.__performQuery__(QueryQC3(self.getPrefixes()+ prefixes))

    def performQueryQE1(self, prefixes):
        return self.__performQuery__(QueryQE1(self.getPrefixes() + prefixes))

    def performQueryQE2(self, prefixes, param):
        return self.__performQuery__(QueryQE2(self.getPrefixes() + prefixes, [("?x",param)]))

    def performQueryQE3(self, prefixes, param):
        return self.__performQuery__(QueryQE3(self.getPrefixes() + prefixes, [("?x",param)]))

    def performQueryQE4(self, prefixes):
        return self.__performQuery__(QueryQE4(self.getPrefixes() + prefixes))