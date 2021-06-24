# POC4COMMERCE

This Python API library provides basic mechanisms for interacting with OASIS behavior ontologies adopted by the POC4COMMERCE project in the ONTOCHAIN ecosystem.

## Requirements </br>
   - Python interpreter version 3.7 or greater.
   - RDFLib version 5.0.0.

## Generating new agent and new agent behaviors </br>
In order to generate new OASIS behaviors you should

A) Create a Behavior object by typing: </br>
      
      b = BehaviorManager(ontology, namespace, ontologyTemplate, namespaceTemplate)
      
   where  </br>
   - "ontology" is the ontology containing the agent behavior.
   - "namespace" is namespace of "ontology". You can use "None" if "xml:base" is already defined in the ontology.
   - "ontologyTemplate" is the namespace of the ontology containing the behavior template.
   - "namespaceTemplate" is namespace of "ontologyTemplate". You can use "None" if "xml:base" is already defined in the ontology.
   
B) (Optional) Create a new behavior template by typing </br>
      
      b.createAgentTemplate(agentTemplateName)
      
   where  </br>   
   - "ontologyTemplateName" is the name of the agent template name. </br>
   
   Then, create a new agent template behavior by typing: </br>


      b.createAgentBehaviorTemplate(MyTemplateBehavior, MyTemplateGoal, MyTemplateTask,
                                     [MyTemplateTaskOperator, action], 
                                     [MyTemplateOperatorArgument, actionArgument],
                                     [
                                        [MyTemplateTaskObject, taskObjectProperty, objectTemplate]
                                     ], 
                                     [ 
                                        [MyTemplateInput1, taskInputProperty, input1]
                                     ], 
                                     [ 
                                        ["MyTemplateOutput1", taskOutputProperty, output1]
                                     ])

        
   where
   - "MyTemplateBehavior" is the entity name of the behavior template. 
   - "MyTemplateGoal" is the entity name of the goal template.
   - "MyTemplateTask" is the entity name of the task template.
   - "MyTemplateTaskOperator" and "action" are the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyTemplateOperatorArgument" and "actionArgument" are the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of type:
     - [MyTemplateTaskObject, taskObjectProperty, objectTemplate]
           where: </br>
           - "MyTemplateTaskObject" is the entity name of the task object.
           - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
           - "objectTemplate" is the element associated to the task object.
   - A list of elements of type:
     - [MyTemplateInput1, taskInputProperty, input1]
     where: </br> 
     - "MyTemplateInput1" is the entity name of the input.
     - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
     - "input" is the element associated to the input element.   
   - A list of elements of type:
     - [MyTemplateOutput1, taskOutputProperty, output1]
     where: </br> 
     - "MyTemplateOutput1" is the entity name of the output.
     - "taskOutputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
     - "output" is the element associated to the output element.  
     
 - Connect the behavior with the related template
 
       b.connectAgentTemplateToBehavior(MyAgentBehaviorTemplate, MyTemplateBehavior)
       
   where
   - "MyAgentBehaviorTemplate" is the the behavior template created as described above.
   - "MyTemplateBehavior" is the behavior created as above.

C) Create a new agent and a new behavior eventually related with a behavior template.
   
   Create a new agent by typing:
              
      b.createAgent("MyAgent")
   where
   - "MyAgent" is the entity name of the agent.
   
   Create a new agent behavior and eventually connect it to its template by typing
   
      b.createAgentBehavior(MyAgentBehavior, MyAgentGoal, MyAgentTask,
                            [MyAgentTaskOperator, action],
                            [MyAgentOperatorArgument, actionArgument],
                         [
                            [MyAgentTaskObject, taskObjectProperty, agentobject1]
                         ],
                         [
                             [MyAgentInput1, taskInputProperty, agentinput1]
                         ],
                         [
                             [MyAgentOutput1, taskInputProperty, agentoutput1]
                         ],
                         [
                           MyTemplateTask,
                          [
                              [MyAgentTaskObject, MyTemplateTaskObject]
                          ],
                          [
                              [MyAgentInput1, MyTemplateInput1]
                          ],
                          [
                              [MyAgentOutput1, MyTemplateOutput1]
                          ]
                         ])

   where
   - "MyAgentBehavior" is the entity name of the behavior. 
   - "MyAgentGoal" is the entity name of the goal.
   - "MyAgentTask" is the entity name of the task.
   - "MyAgentTaskOperator" and "action" are the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyAgentOperatorArgument" and "actionArgument" are the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of type:
     - [MyAgentTaskObject, taskObjectProperty, agentobject1]
           where: </br>
           - "MyAgentTaskObject" is the entity name of the task object.
           - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
           - "agentobject1" is the element associated to the task object.
   - A list of elements of type:
     - [MyAgentInput1, taskInputProperty, agentinput1]
     where: </br> 
     - "MyAgentInput1" is the entity name of the input.
     - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
     - "agentinput1" is the element associated to the input element.   
   - A list of elements of type:
     - [MyAgentOutput1, taskOutputProperty, agentoutput1]
     where: </br> 
     - "MyAgentOutput1" is the entity name of the output.
     - "taskOutputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
     - "agentoutput1" is the element associated to the output element. 
   - Eventually a list of elements mapping from the agent to the template:
     - "MyTemplateTask" is the task object of the behavior template.
     - A list of elements of type:
        - "MyAgentTaskObject", "MyTemplateTaskObject"
        where:</br>
        -  "MyAgentTaskObject", "MyTemplateTaskObject" represent the entity name of the agent task object  and the entity of the task object template, respectively.
     - A list of elements of type:  
        - "MyAgentInput1", "MyTemplateInput1"
        where:</br>
        -  "MyAgentInput1", "MyTemplateInput1" represent the entity name of the agent input and the agent input template, respectively.
     - A list of elements of type:  
        - "MyAgentOutput1", "MyTemplateOutput1"
        where:</br>
        -  "MyAgentOutput1", "MyTemplateOutput1" represent the entity name of the agent output and the agent output template, respectively.
  - Connect the created behavior to its agent by typing:
     
        b.connectAgentToBehavior("MyAgent", "MyAgentBehavior")
    
    where </br>
    - "MyAgent" and "MyAgentBehavior" are the agent and the agent behavior respectively.
    
       
       

