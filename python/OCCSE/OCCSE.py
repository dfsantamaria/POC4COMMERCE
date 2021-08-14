from owlready2 import *

class OCCSE:
    def __init__(self, *args):
        self.repositoryManager = None
        self.reasonerInterface = None
        self.world = World()
        self.reasonerStatus=False
        self.repositoryStatus=False
        if len(args)==2:
            self.__construct2__(args[0], args[1])

    def __construct2__(self,repository, reasoner):
        self.repositoryManager=repository
        self.reasonerInterface=reasoner

    def loadRepository(self):
        for rep in self.repositoryManager.getRepository():
            self.world.get_ontology(rep).load()
        self.repositoryManager.resetChanged()
        self.__resetIsRepositoryLoaded__(True)
        self.__resetIsSyncReasoner__(False)

    def syncReasoner(self):
        if self.isRepositoryLoaded():
           self.reasonerInterface.runReasoner(self.world)
           self.__resetIsSyncReasoner__(True)

    def performQuery(self, query):
        self.__checkRepository__()
        self.__checkReasoner__()
        return self.world.sparql(query.build())

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
