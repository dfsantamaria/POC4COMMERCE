# POC4COMMERCE

This Python API library provides basic mechanisms for interacting with OASIS behavior ontologies adopted by the POC4COMMERCE project in the ONTOCHAIN ecosystem.

## Requirements </br>
   - Python interpreter version 3.7 or greater.
   - RDFLib version 5.0.0.

## Generating new agent and new agent behaviors </br>
In order to generate new OASIS behaviors you should

A) Create a FacilityManager object by typing: </br>
      
      b = FacilityManager(ontology, namespace, ontologyURL, ontologyTemplate, namespaceTemplate, templateURL)
      
   where:  </br>
   - "ontology" is the ontology containing the agent behavior.
   - "namespace" is namespace of "ontology". You can use "None" if "xml:base" is already defined in the ontology.
   - "ontologyURL" is the URL of the ontology.
   - "ontologyTemplate" is the namespace of the ontology containing the behavior template.
   - "namespaceTemplate" is namespace of "ontologyTemplate". You can use "None" if "xml:base" is already defined in the ontology.
   - "templateURL" is the URL of the ontology containing the behavior template.
   
B) (Optional) Create a new behavior template by typing </br>
      
      b.createAgentTemplate(agentTemplateName)
      
   where:  </br>   
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

        
   where:
   - "MyTemplateBehavior" is the entity name of the behavior template. 
   - "MyTemplateGoal" is the entity name of the goal template.
   - "MyTemplateTask" is the entity name of the task template.
   - "MyTemplateTaskOperator" and "action" are the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyTemplateOperatorArgument" and "actionArgument" are the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of type:
     - [MyTemplateTaskObject, taskObjectProperty, objectTemplate] </br>
       where: </br>
         - "MyTemplateTaskObject" is the entity name of the task object.
         - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
         - "objectTemplate" is the element associated to the task object.
   - A list of elements of type:
     - [MyTemplateInput1, taskInputProperty, input1] </br>
       where: </br> 
        - "MyTemplateInput1" is the entity name of the input.
        - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
        - "input" is the element associated to the input element.   
   - A list of elements of type:
     - [MyTemplateOutput1, taskOutputProperty, output1] </br>
       where: </br> 
       - "MyTemplateOutput1" is the entity name of the output.
       - "taskOutputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
       - "output" is the element associated to the output element.  
     
 - Connect the behavior with the related template
 
       b.connectAgentTemplateToBehavior(MyAgentBehaviorTemplate, MyTemplateBehavior)
       
   where: </br>
   - "MyAgentBehaviorTemplate" is the the behavior template created as described above.
   - "MyTemplateBehavior" is the behavior created as above.

C) Create a new agent and a new behavior eventually related with a behavior template.
   
   Create a new agent by typing:
              
      b.createAgent("MyAgent")
   where:
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

   where:
   - "MyAgentBehavior" is the entity name of the behavior. 
   - "MyAgentGoal" is the entity name of the goal.
   - "MyAgentTask" is the entity name of the task.
   - "MyAgentTaskOperator" and "action" are the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyAgentOperatorArgument" and "actionArgument" are the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of type:
        - [MyAgentTaskObject, taskObjectProperty, agentobject1] </br>
           where: </br>
           - "MyAgentTaskObject" is the entity name of the task object.
           - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
           - "agentobject1" is the element associated to the task object.
   - A list of elements of type:
        - [MyAgentInput1, taskInputProperty, agentinput1] </br>
          where: </br> 
          - "MyAgentInput1" is the entity name of the input.
          - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
          - "agentinput1" is the element associated to the input element.   
   - A list of elements of type:
        - [MyAgentOutput1, taskOutputProperty, agentoutput1]</br>
          where: </br> 
          - "MyAgentOutput1" is the entity name of the output.
          - "taskOutputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
          - "agentoutput1" is the element associated to the output element. 
   - Eventually a list of elements mapping from the agent to the template:
       - "MyTemplateTask" is the task object of the behavior template.
       - A list of elements of type:
            - ["MyAgentTaskObject", "MyTemplateTaskObject"] </br>
              where:</br>
                 -  "MyAgentTaskObject", "MyTemplateTaskObject" represent the entity name of the agent task object  and the entity of the task object template, respectively.
       - A list of elements of type:  
            - ["MyAgentInput1", "MyTemplateInput1"] </br>
              where:</br>
                -  "MyAgentInput1", "MyTemplateInput1" represent the entity name of the agent input and the agent input template, respectively.
       - A list of elements of type:  
           - ["MyAgentOutput1", "MyTemplateOutput1"] </br>
           where:</br>
               -  "MyAgentOutput1", "MyTemplateOutput1" represent the entity name of the agent output and the agent output template, respectively.
  - Connect the created behavior to its agent by typing:
     
        b.connectAgentToBehavior("MyAgent", "MyAgentBehavior")
    
    where: </br>
    - "MyAgent" and "MyAgentBehavior" are the agent and the agent behavior respectively.
    
       
 D) Generate a new action and connect it to the related behavior by typing
 
       b.createAgentAction(MyAgent, planExecution, executionGoal, executionTask,
                         [executionOperator, action],
                         [executionArgument, argument],
                         [
                             [executionObject, taskObjectProperty, executionobject1]
                         ],
                         [
                             [executionInput1, inputProp, executioninput1]
                         ],
                         [
                             [executionOutput1, outputProp, executionOutput1]
                         ],
                         [
                           MyAgentTask,
                          [
                              [executionObject, MyAgentTaskObject]
                          ],
                          [
                              [executionInput1, MyAgentInput1]
                          ],
                          [
                              [executionOutput1, MyAgentOutput1]
                          ]
                         ])
                         
  where:</br>
  - "MyAgent" is the entity name of the agent responsible for the execution of the action.
  - "planExecution" is the entity name of the plan execution.
  - "executionGoal" is the entity name of the goal execution.
  - "executionTask" is the entity name of the task execution.
  - A list of element of type:
      - [executionOperator, action] </br>
        where:</br>
         - "executionOperator" is the name of the task operator.
         - "action" is name of the action as defined in OASIS-ABox.
      - [executionArgument, argument] </br>
        where:</br>
        - "executionArgument" is the name of the task argument.
        - "argument" is the name of the argument as defined in OASIS-ABox.
      - A list of element of type:  
        - [executionObject, taskObjectProperty, executionobject1] </br>
          where: </br>
          - "executionObject" is the entity name of the task execution object.
          - "taskObjectProperty" is  either "refersAsNewTo" or "refersExactlyTo".
          - "executionobject1" is the element associated with the task execution object.     
      - A list of elements of type:
        - [executionInput1, inputProp, executioninput1] </br>
          where: </br>
             - "executionInput1" is the entity name of task input.
             - "inputProp" is either "refersAsNewTo" or "refersExactlyTo".
             - "executioninput1" is the element associated with the task input.
       - A list of elements of type:
         - [executionOutput1, outputProp, executionOutput1] </br>
           where: </br>
             - "executionOutput1" is the entity name of task output.
             - "outputProp" is either "refersAsNewTo" or "refersExactlyTo".
             - "executionOutput1" is the element associated with the task output.
       - A list of elements mapping from the agent action to the agent behavior:
          - "MyAgentTask" is the task  of the agent behavior.
       - A list of elements of type:
          - [executionObject, MyAgentTaskObject] </br>
            where: </br>
              - "executionObject", "MyAgentTaskObject" represent the entity name of the  task execution  and the entity name of the task object of the agent behavior, respectively.
       - A list of elements of type:  
         - [executionInput1, MyAgentInput1] </br>
           where:</br>
              - "executionInput1", "MyAgentInput1" represent the entity name of the action input and the agent behavior input , respectively.
        - A list of elements of type:  
          - [executionOutput1, MyAgentOutput1] </br>
            where:</br>
              -  "executionOutput1", "MyAgentOutput1" represent the entity name of the action output and the agent behavior output, respectively.
