from rdflib import *

class Behavior:
    def __init__(self, ontologyGraph, ontologyNamespace, ontologyTemplateGraph, ontologyTemplateNamespace, ): # INPUT: the user ontology, the user ontology namespace
        self.oasisURL = "https://www.dmi.unict.it/santamaria/projects/oasis/sources/rdf/oasis-rdf.owl"  # OASIS ontology URL
        self.oasisABoxURL = "https://www.dmi.unict.it/santamaria/projects/oasis/sources/rdf/oasis-abox-rdf.owl"  # OASIS-ABox ontology URL

        #
        #oasis ontology data
        #
        self.oasisOnt = self.loadOntology(self.oasisURL)  # OASIS ontology object
        self.oasisABoxOnt = self.loadOntology(self.oasisABoxURL)  # OASIS-ABox ontology object
        self.owlobj = URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")
        self.owldat = URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")
        self.oasisNamespace=self.getNamespace(self.oasisOnt)  # OASIS ontology namespace
        self.oasisABoxNamespace=self.getNamespace(self.oasisABoxOnt)  # OASIS-ABox ontology namespace

        #
        #user ontology data
        #
        self.baseOntology = ontologyGraph  # User ontology
        if ontologyNamespace == None: #Computing user ontology namespace
           self.baseNamespace = self.getNamespace(self.baseOntology)
        else:
           self.baseNamespace = ontologyNamespace
        self.baseAgent = None  # User agent name

        #
        #user agent template ontology data
        #
        self.baseTemplateOntology = ontologyTemplateGraph  # User template ontology
        if ontologyTemplateNamespace == None:  # Computing user template ontology namespace
            self.baseTemplateNamespace = self.getNamespace(self.baseTemplateOntology)
        else:
            self.baseTemplateNamespace = ontologyTemplateNamespace

        return

    #create an ontology object from a given URL
    def loadOntology(self, ontoURL):
        g=Graph()
        g.load(ontoURL)
        return g

    # Get the base namespace of an ontology given the ontology object
    def getNamespace(self, ontology):
        namespace = ""
        for ns_prefix, ns_namespace in ontology.namespaces():
            if ns_prefix == "":
               namespace=ns_namespace
        if not namespace.endswith('#'):
            return namespace+"#"
        return namespace

    # Get the IRI of OASIS entities given their entity name
    def getOASISEntityByName(self, name):
        return self.oasisNamespace + name

    # Get the IRI of OASIS-Abox entities given their entity name
    def getOASISABoxEntityByName(self, name):
        return self.oasisABoxNamespace + name

    def addObjPropAssertion(self, ontology, subject, property, object):
        ontology.add((URIRef(subject), URIRef(property), URIRef(object)))

    def addClassAssertion(self, ontology, instance, owlclass):
        ontology.add((URIRef(instance), RDF.type, URIRef(owlclass)))

    def addOWLObjectProperty(self, ontology, property):
        self.addClassAssertion(ontology, property, self.owlobj)

    def addOWLDataProperty(self, ontology, property):
        self.addClassAssertion(ontology, property, self.owldat)

    # Add to ontology with the selected namespace an owl:imports axiom for each passed IRI.
    #INPUT the ontology and the ontology IRI that will include the owl:imports axiom, a list of IRI to be included in the ontology
    def addImportAxioms(self, ontology, ontologyNS, namespaceToImport):
        for s in namespaceToImport:
            self.addObjPropAssertion(ontology, URIRef(ontologyNS), OWL.imports, URIRef(s))


    def getNoAnchorNamespace(self, namespace):
        if namespace.endswith('#'):
           return namespace[:-1]
        return namespace

    #import OASIS and OASIS-Abox in the current ontology
    def addImportOASIS(self, ontology, namespace):
        self.addImportAxioms(ontology, namespace, [ self.getNoAnchorNamespace(self.oasisNamespace), self.getNoAnchorNamespace(self.oasisABoxNamespace)])
        ontology.bind("oasis", self.oasisNamespace)
        ontology.bind("oabox", self.oasisABoxNamespace)

        # Create an user agent given the agent entity name

    def createAgent(self, agentName):
        self.baseAgent = self.baseNamespace + agentName
        self.addClassAssertion(self.baseOntology, self.baseAgent, self.getOASISEntityByName("Agent"))
        return self.baseAgent

    #create an OASIS agent template given its name
    def createAgentTemplate(self, agentName):
        baseTemplateAgent = self.baseTemplateNamespace + agentName
        self.addClassAssertion(self.baseTemplateOntology, baseTemplateAgent, self.getOASISEntityByName("AgentBehaviorTemplate"))
        # print(self.baseNamespace, self.oasisNamespace, self.oasisABoxNamespace)
        return baseTemplateAgent


    #connect a agent template with a behavior template
    def connectAgentToBehaviorTemplate(self, agentName, behaviorName):
        self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("hasBehavior"))
        self.addObjPropAssertion(self.baseTemplateOntology, self.baseTemplateNamespace+agentName,
                                 self.getOASISEntityByName("hasBehavior"), self.baseTemplateNamespace+behaviorName)
      #  self.baseTemplateNamespace + behaviorName
      #  baseTemplateAgent = self.baseTemplateNamespace + agentName

    #create a behavior template given an agent template IRI
    def createBehaviorTemplate(self, behaviorName, goalName, taskName, operators, operatorsArguments, inputs, outputs):
        #create  and add the behavior
        behavior = self.baseTemplateNamespace+behaviorName
        self.addClassAssertion(self.baseTemplateOntology, behavior, self.getOASISEntityByName("Behavior"))

        #create, add, and connect the goal
        goal = self.baseTemplateNamespace+goalName
        self.addClassAssertion(self.baseTemplateOntology, goal, self.getOASISEntityByName("GoalDescription"))
        self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("consistsOfGoalDescription"))
        self.addObjPropAssertion(self.baseTemplateOntology, behavior, self.getOASISEntityByName("consistsOfGoalDescription"), goal)

        # create, add, and connect the task
        task = self.baseTemplateNamespace + taskName
        self.addClassAssertion(self.baseTemplateOntology,task, self.getOASISEntityByName("TaskDescription"))
        self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("consistsOfTaskDescription"))
        self.addObjPropAssertion(self.baseTemplateOntology, goal, self.getOASISEntityByName("consistsOfTaskDescription"), task)

        #create, add, and connect the task operator
        taskOperator = self.baseTemplateNamespace + operators[0]
        self.addClassAssertion(self.baseTemplateOntology, taskOperator, self.getOASISEntityByName("TaskOperator"))
        self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("hasTaskOperator"))
        self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("refersExactlyTo")) #the action property
        self.addObjPropAssertion(self.baseTemplateOntology, task, self.getOASISEntityByName("hasTaskOperator"), taskOperator)
        self.addObjPropAssertion(self.baseTemplateOntology, taskOperator, self.getOASISEntityByName("refersExactlyTo"), self.getOASISABoxEntityByName(operators[1])) #the action

        # create, add, and connect the task operator argument
        if operatorsArguments:
           taskOperatorArgument = self.baseTemplateNamespace + operatorsArguments[0]
           self.addClassAssertion(self.baseTemplateOntology, taskOperatorArgument, self.getOASISEntityByName("TaskOperatorArgument"))
           self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("hasTaskOperatorArgument"))
           self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("refersExactlyTo"))  # the action property
           self.addObjPropAssertion(self.baseTemplateOntology, task, self.getOASISEntityByName("hasTaskOperatorArgument"), taskOperatorArgument)
           self.addObjPropAssertion(self.baseTemplateOntology, taskOperatorArgument, self.getOASISEntityByName("refersExactlyTo"), self.getOASISABoxEntityByName(operatorsArguments[1]))  # the action

        # create, add, and connect the task input parameters
        if inputs:
            for input in inputs:
                inputName = self.baseTemplateNamespace + input[0]
                self.addClassAssertion(self.baseTemplateOntology, inputName, self.getOASISEntityByName("TaskInputParameterTemplate"))
                self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("hasTaskInputParameterTemplate"))
                self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName(input[1]))  # the input property
                self.addObjPropAssertion(self.baseTemplateOntology, task, self.getOASISEntityByName("hasTaskInputParameterTemplate"), inputName)
                self.addObjPropAssertion(self.baseTemplateOntology, inputName, self.getOASISEntityByName(input[1]),  input[2])  # the action

        # create, add, and connect the task input parameters
        if outputs:
           for output in outputs:
               outputName = self.baseTemplateNamespace + output[0]
               self.addClassAssertion(self.baseTemplateOntology, outputName, self.getOASISEntityByName("TaskOutputParameterTemplate"))
               self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName("hasTaskOutputParameterTemplate"))
               self.addOWLObjectProperty(self.baseTemplateOntology, self.getOASISEntityByName(output[1]))  # the input property
               self.addObjPropAssertion(self.baseTemplateOntology, task, self.getOASISEntityByName("hasTaskOutputParameterTemplate"), outputName)
               self.addObjPropAssertion(self.baseTemplateOntology, outputName, self.getOASISEntityByName(output[1]), output[2])  # the action