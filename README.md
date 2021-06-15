# POC4COMMERCE

This Python API library provides basic mechanisms for interacting with OASIS behavior ontologies adopted by the POC4COMMERCE project in the ONTOCHAIN ecosystem.



Generating new behaviors </br>
   To generate new OASIS behaviors you should

A) Create a Behavior object by typing: </br>
      
      b = Behavior(ontology, namespace, ontologyTemplate, namespaceTemplate)
      
   where  </br>
   - "ontology" is the ontology containing the agent behavior.
   - "namespace" is namespace of "ontology". You can use "None" if "xml:base" is already defined in the ontology.
   - "ontologyTemplate" is the namespace of the ontology containing the behavior template.
   - "namespaceTemplate" is namespace of "ontologyTemplate". You can use "None" if "xml:base" is already defined in the ontology.
   
B) (Optional) Create a new behavior template </br>
   Type 
   
      b.createAgentTemplate(agentTemplateName)
      
   where 
         -"ontologyTemplateName" is the name of the agent template name. </br>
   Create a new agent template behavior by typing: </br>


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
       -"MyTemplateBehavior" is the entity name of the behavior template. 
       -"MyTemplateGoal" is the entity name of the goal template.
       -"MyTemplateTask" is the entity name of the task template.
       -"MyTemplateTaskOperator" and "action" are the entity name of the task operator  and the operator action as defined in OASIS-ABox.
       -"MyTemplateOperatorArgument" and "actionArgument" are the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
       - A list of elements of type:
           [MyTemplateTaskObject, taskObjectProperty, objectTemplate]
           where:
                 -"MyTemplateTaskObject" is the entity name of the task object.
                 -"taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
                 -"objectTemplate" is the element associated to the task object.
       - A list of elements of type:
           [MyTemplateInput1, taskInputProperty, input1]
           where: 
                 -"MyTemplateInput1" is the entity name of the input.
                 -"taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
                 -"input" is the element associated to the input element.   
        - A list of elements of type:
           [MyTemplateOutput1, taskOutputProperty, output1]
           where: 
                 -"MyTemplateOutput1" is the entity name of the output.
                 -"taskOutputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
                 -"output" is the element associated to the output element.  
           
           
       
       

