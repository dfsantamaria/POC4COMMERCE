class RepositoryManager:
    def __init__(self, repositoryList):
        self.repositorySet = []
        self.isChanged = False
        if repositoryList is not None:
            for r in repositoryList:
                self.repositorySet.append(r)
            self.isChanged = True

    def addRepositories(self, repository):
        size=len(self.repositorySet)
        for rep in repository:
            if rep not in self.repositorySet:
                self.repositorySet.append(rep)
        if len(self.repositorySet)>size:
           self.isChanged=True


    def removeRepositories(self, repository):
        size = len(self.repositorySet)
        for rep in repository:
           if rep in self.repositorySet:
              self.repositorySet.remove(rep)
        if len(self.repositorySet) < size:
            self.isChanged = True

    def getRepository(self):
        return self.repositorySet

    def getChanged(self):
        return self.isChanged

    def resetChanged(self):
        self.isChanged = False

    def isRepositoryChanged(self):
        return self.isChanged

