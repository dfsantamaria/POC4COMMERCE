from rdflib import *

class BehaviorManager:
    def __init__(self, ontologyGraph, ontologyNamespace, ontologyTemplateGraph, ontologyTemplateNamespace, ): # INPUT: the user ontology, the user ontology namespace
        self.oasisURL = "https://www.dmi.unict.it/santamaria/projects/oasis/sources/oasis.owl"  # OASIS ontology URL
        self.oasisABoxURL = "https://www.dmi.unict.it/santamaria/projects/oasis/sources/oasis-abox.owl"  # OASIS-ABox ontology URL

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
        self.addImportAxioms(self.baseOntology, self.baseNamespace, [self.baseTemplateNamespace])
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
        self.addImportAxioms(ontology, namespace, [self.oasisURL, self.oasisABoxURL])
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


    #connect a agent template  with a behavior
    def connectAgentTemplateToBehavior(self, agentName, behaviorName):
        self.__connectAgentToGeneralBehavior__(self.baseTemplateOntology, self.baseTemplateNamespace, agentName, behaviorName)

    # connect a agent  with a behavior
    def connectAgentToBehavior(self, agentName, behaviorName):
        self.__connectAgentToGeneralBehavior__( self.baseOntology, self.baseNamespace, agentName, behaviorName)

    def __connectAgentToGeneralBehavior__(self, ontology, namespace, agentName, behaviorName):
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName("hasBehavior"))
        self.addObjPropAssertion(ontology, namespace + agentName,  self.getOASISEntityByName("hasBehavior"), namespace + behaviorName)


    #add a goal to a selected behavior given the behavior IRI and goal name
    def addGoalToBehavior(self, ontology, namespace, behavior, goalName):
        goal = namespace + goalName
        self.addClassAssertion(ontology, goal, self.getOASISEntityByName("GoalDescription"))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName("consistsOfGoalDescription"))
        self.addObjPropAssertion(ontology, behavior, self.getOASISEntityByName("consistsOfGoalDescription"), goal)
        return goal

    #add a task to a selected goal given the goal IRI and the task name
    def addTaskToGoal(self, ontology, namespace, goal, taskName):
        task = namespace + taskName
        self.addClassAssertion(ontology, task, self.getOASISEntityByName("TaskDescription"))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName("consistsOfTaskDescription"))
        self.addObjPropAssertion(ontology, goal, self.getOASISEntityByName("consistsOfTaskDescription"), task)
        return task

    #add a task operator to the selected task given the task IRI, the operator name and the operator entity name
    def addTaskOperatorToTask(self, ontology, namespace, task, operatorName, operatorEntity):
        taskOperator = namespace + operatorName
        self.addClassAssertion(ontology, taskOperator, self.getOASISEntityByName("TaskOperator"))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName("hasTaskOperator"))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName("refersExactlyTo"))  # the action property
        self.addObjPropAssertion(ontology, task, self.getOASISEntityByName("hasTaskOperator"), taskOperator)
        self.addObjPropAssertion(ontology, taskOperator, self.getOASISEntityByName("refersExactlyTo"),
                                 self.getOASISABoxEntityByName(operatorEntity))  # the action
        return taskOperator

    #add a task operator argument to selected task given the task IRI, the operator argument name and the operator argument entity name
    def addTaskOperatorArgumentToTask(self, ontology, namespace, task, taskOpArgumentName, taskOpEntityName):
        taskOperatorArgument = namespace + taskOpArgumentName
        self.addClassAssertion(ontology, taskOperatorArgument, self.getOASISEntityByName("TaskOperatorArgument"))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName("hasTaskOperatorArgument"))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName("refersExactlyTo"))  # the action property
        self.addObjPropAssertion(ontology, task, self.getOASISEntityByName("hasTaskOperatorArgument"),
                                 taskOperatorArgument)
        self.addObjPropAssertion(ontology, taskOperatorArgument, self.getOASISEntityByName("refersExactlyTo"),
                                 self.getOASISABoxEntityByName(taskOpEntityName))  # the action
        return taskOperatorArgument

    def __createBehaviorPath__(self, ontology, namespace, behaviorName, goalName, taskName, operators, operatorsArguments):
        behavior = namespace + behaviorName
        self.addClassAssertion(ontology, behavior, self.getOASISEntityByName("Behavior"))

        # create, add, and connect the goal
        goal = self.addGoalToBehavior(ontology, namespace, behavior, goalName)

        # create, add, and connect the task
        task = self.addTaskToGoal(ontology, namespace, goal, taskName)

        # create, add, and connect the task operator
        taskOperator = self.addTaskOperatorToTask(ontology, namespace, task, operators[0], operators[1]);

        # create, add, and connect the task operator argument
        if operatorsArguments:
            taskOperatorArgument = self.addTaskOperatorArgumentToTask(ontology, namespace, task, operatorsArguments[0], operatorsArguments[1])

        return behavior, goal, task, taskOperator, taskOperatorArgument

    # add task object to the selected task given the object name,  the task obj entity property, and the task object entity
    def addTaskObjectToTask(self, task, objectName, taskobpropentity, taskobentity):
        return self.__addTaskElementToTask__(self.baseOntology, self.baseNamespace, task, objectName,  "TaskObject", "hasTaskObject", taskobpropentity, taskobentity)

    # add task object template to the selected task given the object name,  the task obj entity property, and the task object entity
    def addTaskObjectTemplateToTask(self, task, objectName,  taskobpropentity, taskobentity):
       return  self.__addTaskElementToTask__(self.baseTemplateOntology, self.baseTemplateNamespace, task, objectName, "TaskObjectTemplate", "hasTaskObjectTemplate", taskobpropentity, taskobentity)

    # add task input to the selected task given the input name, the input entity property,  and the input entity
    def addTaskInputToTask(self, task, input, inputPropEntity, inputEntity):
        return self.__addTaskElementToTask__(self.baseOntology, self.baseNamespace, task, input, "TaskFormalInputParameter", "hasTaskFormalInputParameter", inputPropEntity, inputEntity)

    # add task input to the selected task given the input name, the input entity property,  and the input entity
    def addTaskInputTemplateToTask(self, task, input, inputPropEntity, inputEntity):
        return self.__addTaskElementToTask__(self.baseTemplateOntology, self.baseTemplateNamespace, task, input, "TaskInputParameterTemplate", "hasTaskInputParameterTemplate", inputPropEntity, inputEntity)

    # add task output to the selected task given the output name, the output entity property,  and the output entity
    def addTaskOutputToTask(self, task, output, outputPropEntity, outputEntity):
        return self.__addTaskElementToTask__(self.baseOntology, self.baseNamespace, task, output,  "TaskFormalOutputParameter", "hasTaskFormalOutputParameter", outputPropEntity,
                                             outputEntity)

    # add task input to the selected task given the input name, the input entity property,  and the input entity
    def addTaskOutputTemplateToTask(self, task, output, outputPropEntity, outputEntity):
        return self.__addTaskElementToTask__(self.baseTemplateOntology, self.baseTemplateNamespace, task, output,  "TaskOutputParameterTemplate", "hasTaskOutputParameterTemplate",
                                             outputPropEntity, outputEntity)

    # add task element to the selected task given the  name, the  class, the elementt property, the element entity property,  and the element entity
    def __addTaskElementToTask__(self, ontology, namespace, task, elementName, elementclass, elemobprop, elempropentity, elementity):
        object = namespace + elementName
        self.addClassAssertion(ontology, object, self.getOASISEntityByName(elementclass))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName(elemobprop))
        self.addOWLObjectProperty(ontology, self.getOASISEntityByName(elempropentity))  # the task-object property
        self.addObjPropAssertion(ontology, task, self.getOASISEntityByName(elemobprop), object)
        self.addObjPropAssertion(ontology, object, self.getOASISEntityByName(elempropentity),
                                 elementity)  # the object
        return object

    #create a behavior template given an agent template IRI
    def createAgentBehaviorTemplate(self, behaviorName, goalName, taskName, operators, operatorsArguments, objects, inputs, outputs):
        #create  and add the behavior
        behavior, goal, task, taskOperator, taskOperatorArgument = self.__createBehaviorPath__(self.baseTemplateOntology, self.baseTemplateNamespace, behaviorName, goalName, taskName, operators, operatorsArguments)
        #create, add, and connect the task object
        if objects:
           for object in objects:
               objectName = self.addTaskObjectTemplateToTask(task, object[0], object[1], object[2])

        # create, add, and connect the task input parameters
        if inputs:
            for input in inputs:
                inputName = self.addTaskInputTemplateToTask(task, input[0], input[1], input[2])


        # create, add, and connect the task input parameters
        if outputs:
           for output in outputs:
               outputName = self.addTaskOutputTemplateToTask(task, output[0], output[1], output[2])

    def createAgentBehavior(self, behaviorName, goalName, taskName, operators, operatorsArguments, objects, inputs,  outputs, mapping):
        # create  and add the behavior
        behavior, goal, task, taskOperator, taskOperatorArgument  = self.__createBehaviorPath__(self.baseOntology,  self.baseNamespace, behaviorName, goalName, taskName, operators, operatorsArguments)
        # create, add, and connect the task object
        if objects:
            for object in objects:
                objectName = self.addTaskObjectToTask(task, object[0], object[1], object[2])


        # create, add, and connect the task input parameters
        if inputs:
           for input in inputs:
               inputName = self.addTaskInputToTask(task, input[0], input[1], input[2])


        # create, add, and connect the task input parameters
        if outputs:
           for output in outputs:
               outputName = self.addTaskOutputToTask(task, output[0], output[1], output[2])

        #linking agent behavior with the corresponding behavior template
        if mapping:
            #mapping the task
            task_op= URIRef(self.baseTemplateNamespace+mapping[0])
            self.addOWLObjectProperty(self.baseOntology, self.getOASISEntityByName("overloads"))
            self.addObjPropAssertion(self.baseOntology, task, self.getOASISEntityByName("overloads"), task_op)  # the action

            # mapping the task operator (automatically)
            for object in self.baseTemplateOntology.objects(task_op, self.getOASISEntityByName("hasTaskOperator")):
                self.addObjPropAssertion(self.baseOntology, taskOperator, self.getOASISEntityByName("overloads"), object)
                break
            # mapping the task operator argument (automatically) #
            for object in self.baseTemplateOntology.objects(task_op, self.getOASISEntityByName("hasTaskOperatorArgument")):
                self.addObjPropAssertion(self.baseOntology, taskOperatorArgument, self.getOASISEntityByName("overloads"), object)
                break
            # mapping the task object, input, and output
            for elem in mapping[1:]:
               for map in elem:
                  self.addObjPropAssertion(self.baseOntology, URIRef(self.baseNamespace+map[0]), self.getOASISEntityByName("overloads"), URIRef(self.baseTemplateNamespace+map[1]))

