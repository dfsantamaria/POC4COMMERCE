from owlready2 import *

class ReasonerInterface:
      def __init__(self, reasonerName):
         self.selectedReasoner = -1
         if reasonerName.casefold() == "hermit":
            self.selectedReasoner = 0
         elif reasonerName.casefold() == "pellet":
            self.selectedReasoner = 1

      def getSelectedReasoner(self):
          return self.selectedReasoner

      def runReasoner(self, the_world):
          if self.selectedReasoner==0:
             sync_reasoner_hermit(the_world)
          elif self.selectedReasoner==1:
             sync_reasoner_pellet(the_world)