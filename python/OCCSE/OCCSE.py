from OCCSE.QueryBuilderModule import *
import json

class OCCSE:
    # Instantiate a OCCSE object. Use:
    # args[0] is a repository manager specifying all the POC4COMMERCE ontologies and the ontologies you want to query
    # args[1] is the reasoner interface specifying the reasoner you want to use
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

    #load into the triple-store the repositories specified in the constructor
    def loadRepository(self):
        self.world=World()
        for rep in self.repositoryManager.getRepository():
            self.world.get_ontology(rep).load()
        self.repositoryManager.resetChanged()
        self.__resetIsRepositoryLoaded__(True)
        self.__resetIsSyncReasoner__(False)

    #syncronize the reasoner specified in the constructor
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

    #check whether the repository is syncronized
    def isReasonerSyncronized(self):
        return self.reasonerStatus

    #check whether the repository is loaded in the triple-store
    def isRepositoryLoaded(self):
        return self.repositoryStatus

    def __checkReasoner__(self):
        if self.isReasonerSyncronized() == False:
           self.syncReasoner()
           self.__resetIsSyncReasoner__(True)

    #add a new set of prefexis
    def addPrefixes(self, prefixes):
        for p in prefixes:
           self.prefix.append(p)

    #remove a set of prefixes
    def removePrefixes(self, prefixes):
        for p in prefixes:
            if p in self.prefix:
               self.prefix.remove(p)

    #returns the prefixes
    def getPrefixes(self):
        return self.prefix

    #build the header of the query containing the declaration of prefixes
    def buildPrefix(self):
        head = ""
        for p in self.prefix:
            head = head + "PREFIX " + p[0] + ": <" + p[1] + ">" + os.linesep
        return head

    #performs the query passed as parameter
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

    #return a string representing the query passed as parameter
    def getQuery(self, query):
        return self.buildPrefix()+ query.build()

    def __toJson__(self, query, _result):
        result=list(_result)
        jsonlist= []
        for i, val in enumerate(result):
            jsonlist.append(["r"+str(i)+":",  str(self.__toJsonResult__(query, result[i]))])
        return json.dumps(jsonlist)

    def __toJsonResult__(self, query, result):
        toreturn =[]
        for i, val in enumerate(result):
            toreturn.append([query.getColumns()[i], str(val)])
        return toreturn

    # perform the query QF1 with the additional prefixes passed as parameters
    def performQueryQF1(self, prefixes):
        q = QueryQF1(self.getPrefixes() + prefixes)
        return self.__performQuery__(q)


    # perform the query QF2 with the additional prefixes passed as parameters
    def performQueryQF2(self, prefixes):
        q= QueryQF2(self.getPrefixes()+ prefixes)
        return self.__performQuery__(q)


    # perform the query QF3 with the additional prefixes passed as parameters
    def performQueryQF3(self, prefixes, param):
        q = QueryQF3(self.getPrefixes() + prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QF4 with the additional prefixes and parameter passed as parameters
    def performQueryQF4(self, prefixes, param):
        q = QueryQF4(self.getPrefixes() + prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QF5 with the additional prefixes and parameter passed as parameters
    def performQueryQF5(self, prefixes, param):
        q = QueryQF5(self.getPrefixes() + prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QF6 with the additional prefixes and parameter passed as parameters
    def performQueryQF6(self, prefixes,  param):
        q = QueryQF6(self.getPrefixes() + prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QF7 with the additional prefixes and parameter passed as parameters
    def performQueryQF7(self, prefixes ,param):
        q = QueryQF7(self.getPrefixes()+ prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QC1 with the additional prefixes passed as parameters
    def performQueryQC1(self, prefixes):
        q = QueryQC1(self.getPrefixes() + prefixes)
        return self.__performQuery__(q)


    # perform the query QC2 with the additional prefixes and parameter passed as parameters
    def performQueryQC2(self, prefixes, param):
        q = QueryQC2(self.getPrefixes() + prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QC3 with the additional prefixes  passed as parameters
    def performQueryQC3(self, prefixes):
        q = QueryQC3(self.getPrefixes()+ prefixes)
        return self.__performQuery__(q)


    # perform the query QE1 with the additional prefixes passed as parameters
    def performQueryQE1(self, prefixes):
        q = QueryQE1(self.getPrefixes() + prefixes)
        return self.__performQuery__(q)


    # perform the query QE2 with the additional prefixes passed as parameters
    def performQueryQE2(self, prefixes, param):
        q = QueryQE2(self.getPrefixes() + prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QE3 with the additional prefixes  passed as parameters
    def performQueryQE3(self, prefixes, param):
        q= QueryQE3(self.getPrefixes() + prefixes, [("?x",param)])
        return self.__performQuery__(q)


    # perform the query QE4 with the additional prefixes and parameter passed as parameters
    def performQueryQE4(self, prefixes):
        q = QueryQE4(self.getPrefixes() + prefixes)
        return self.__performQuery__(q)
