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
        thequery= query.build()
        preparedquery = self.world.prepare_sparql(thequery)
        query.setColumns(preparedquery.column_names)
        return self.__toJson__(query, self.world.sparql(thequery))

    def getQuery(self, query):
        return self.buildPrefix()+ query.build()

    def __toJson__(self, query, result):
        result=list(result)
        jsonlist= []
        for i, val in enumerate(result):
            jsonlist.append(["r"+str(i)+":",  str(self.__toJsonResult__(query, result[i]))])
        return json.dumps(jsonlist)

    def __toJsonResult__(self, query, result):
        toreturn =[]
        for i, val in enumerate(result):
            toreturn.append([query.getColumns()[i], val])
        return toreturn


    def performQueryQF1(self, prefixes):
        q = QueryQF1(self.getPrefixes() + prefixes)
        res = self.__performQuery__(q)
        return self.__toJson__(q,res)

    def performQueryQF2(self, prefixes):
        q= QueryQF2(self.getPrefixes()+ prefixes)
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQF3(self, prefixes, param):
        q = QueryQF3(self.getPrefixes() + prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQF4(self, prefixes, param):
        q = QueryQF4(self.getPrefixes() + prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQF5(self, prefixes, param):
        q = QueryQF5(self.getPrefixes() + prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQF6(self, prefixes,  param):
        q = QueryQF6(self.getPrefixes() + prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQF7(self, prefixes ,param):
        q = QueryQF7(self.getPrefixes()+ prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQC1(self, prefixes):
        q = QueryQC1(self.getPrefixes() + prefixes)
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQC2(self, prefixes, param):
        q = QueryQC2(self.getPrefixes() + prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQC3(self, prefixes):
        q = QueryQC3(self.getPrefixes()+ prefixes)
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQE1(self, prefixes):
        q = QueryQE1(self.getPrefixes() + prefixes)
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQE2(self, prefixes, param):
        q = QueryQE2(self.getPrefixes() + prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQE3(self, prefixes, param):
        q= QueryQE3(self.getPrefixes() + prefixes, [("?x",param)])
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)

    def performQueryQE4(self, prefixes):
        q = QueryQE4(self.getPrefixes() + prefixes)
        res = self.__performQuery__(q)
        return self.__toJson__(q, res)