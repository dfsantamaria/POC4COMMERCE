class RepositoryManager:
    def __init__(self, repositoryList):
        self.repositorySet= []
        if repositoryList is not None:
            for r in repositoryList:
                self.repositorySet.append(r)

    def addRepositories(self, repository):
        for rep in repository:
            if rep not in self.repositorySet:
                self.repositorySet.append(rep)

    def removeRepositories(self, repository):
        for rep in repository:
           if rep in self.repositorySet:
              self.repositorySet.remove(rep)

    def getRepository(self):
        return self.repositorySet

