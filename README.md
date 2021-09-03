# POC4COMMERCE

This Python API library consists of a stack of three ontologies and two modules. 

-  The first module <b>OCGEN</b> provides basic mechanisms for interacting with OASIS behavior ontologies adopted by the POC4COMMERCE project in the ONTOCHAIN ecosystem.
-  The second module <b>OCCSE</b> provides a search engine and a reasoning system for querying POC4COMMERCE knowledge bases.

## Requirements </br>
   - Python interpreter version 3.7 or greater.
   - RDFLib version 5.0.0. for OCGEN module
   - OWLReady 2 version 0.33 for OCCSE module. It is strongly suggested to also install the Cython parser module for better performances.

## Licensing information

POC4COMMERCE Python API and Ontologies
Copyright (C) 2021.  Giampaolo Bella, Domenico Cantone, Cristiano Longo, Marianna Nicolosi Asmundo, Daniele Francesco Santamaria. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version. This program is distributed in the hope that it will be useful,  but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.


# OCGEN Module
## Generating new agents and agent behaviors </br>
In order to generate new OASIS behaviors you should

A) Create a OCGEN object by typing: </br>
      
      b = OCGEN(ontology, namespace, ontologyURL, ontologyTemplate, namespaceTemplate, templateURL)
      
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
   - "MyTemplateTaskOperator" and "action" are, respectively, the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyTemplateOperatorArgument" and "actionArgument" are, respectively, the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of the form:
     - [MyTemplateTaskObject, taskObjectProperty, objectTemplate] </br>
       where: </br>
         - "MyTemplateTaskObject" is the entity name of the task object.
         - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
         - "objectTemplate" is the element associated to the task object.
   - A list of elements of the form:
     - [MyTemplateInput1, taskInputProperty, input1] </br>
       where: </br> 
        - "MyTemplateInput1" is the entity name of the input.
        - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
        - "input" is the element associated to the input element.   
   - A list of elements of the form:
     - [MyTemplateOutput1, taskOutputProperty, output1] </br>
       where: </br> 
       - "MyTemplateOutput1" is the entity name of the output.
       - "taskOutputProperty" is either "refersAsNewTo" or "refersExactlyTo".
       - "output" is the element associated with the output element.  
     
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
   - "MyAgentTaskOperator" and "action" are, respectively, the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyAgentOperatorArgument" and "actionArgument" are, respectively, the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of the form:
        - [MyAgentTaskObject, taskObjectProperty, agentobject1] </br>
           where: </br>
           - "MyAgentTaskObject" is the entity name of the task object.
           - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
           - "agentobject1" is the element associated to the task object.
   - A list of elements of the form:
        - [MyAgentInput1, taskInputProperty, agentinput1] </br>
          where: </br> 
          - "MyAgentInput1" is the entity name of the input.
          - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
          - "agentinput1" is the element associated to the input element.   
   - A list of elements of the form:
        - [MyAgentOutput1, taskOutputProperty, agentoutput1]</br>
          where: </br> 
          - "MyAgentOutput1" is the entity name of the output.
          - "taskOutputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
          - "agentoutput1" is the element associated to the output element. 
   - Eventually a list of elements mapping from the agent to the template:
       - "MyTemplateTask" is the task object of the behavior template.
       - A list of elements of the form:
            - ["MyAgentTaskObject", "MyTemplateTaskObject"] </br>
              where:</br>
                 -  "MyAgentTaskObject", "MyTemplateTaskObject" represent the entity name of the agent task object  and the entity of the task object template, respectively.
       - A list of elements of the form:  
            - ["MyAgentInput1", "MyTemplateInput1"] </br>
              where:</br>
                -  "MyAgentInput1", "MyTemplateInput1" represent the entity name of the agent input and the agent input template, respectively.
       - A list of elements of the form:  
           - ["MyAgentOutput1", "MyTemplateOutput1"] </br>
           where:</br>
               -  "MyAgentOutput1", "MyTemplateOutput1" represent the entity name of the agent output and the agent output template, respectively.
  - Connect the created behavior to its agent by typing:
     
        b.connectAgentToBehavior("MyAgent", "MyAgentBehavior")
    
    where: </br>
    - "MyAgent" and "MyAgentBehavior" are, respectively, the agent and the agent behavior.
    
       
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
  - A list of element of the form:
      - [executionOperator, action] </br>
        where:</br>
         - "executionOperator" is the name of the task operator.
         - "action" is name of the action as defined in OASIS-ABox.
      - [executionArgument, argument] </br>
        where:</br>
        - "executionArgument" is the name of the task argument.
        - "argument" is the name of the argument as defined in OASIS-ABox.
      - A list of element of the form:  
        - [executionObject, taskObjectProperty, executionobject1] </br>
          where: </br>
          - "executionObject" is the entity name of the task execution object.
          - "taskObjectProperty" is  either "refersAsNewTo" or "refersExactlyTo".
          - "executionobject1" is the element associated with the task execution object.     
      - A list of elements of the form:
        - [executionInput1, inputProp, executioninput1] </br>
          where: </br>
             - "executionInput1" is the entity name of task input.
             - "inputProp" is either "refersAsNewTo" or "refersExactlyTo".
             - "executioninput1" is the element associated with the task input.
       - A list of elements of the form:
         - [executionOutput1, outputProp, executionOutput1] </br>
           where: </br>
             - "executionOutput1" is the entity name of task output.
             - "outputProp" is either "refersAsNewTo" or "refersExactlyTo".
             - "executionOutput1" is the element associated with the task output.
       - A list of elements mapping from the agent action to the agent behavior:
          - "MyAgentTask" is the task  of the agent behavior.
       - A list of elements of the form:
          - [executionObject, MyAgentTaskObject] </br>
            where: </br>
              - "executionObject", "MyAgentTaskObject" represent the entity name of the  task execution  and the entity name of the task object of the agent behavior, respectively.
       - A list of elements of the form:  
         - [executionInput1, MyAgentInput1] </br>
           where:</br>
              - "executionInput1", "MyAgentInput1" represent the entity name of the action input and the agent behavior input , respectively.
        - A list of elements of the form:  
          - [executionOutput1, MyAgentOutput1] </br>
            where:</br>
              -  "executionOutput1", "MyAgentOutput1" represent the entity name of the action output and the agent behavior output, respectively.



Check the files
- test/behaviorGenTest/test_behavior_gen.py
- test/ocgen-test/ocgen-test.py

for some examples of using the OCGEN module.

# OCCSE Module
## Create a Query
To use the OCCSE engine you need at least a query. You can either 
   - use one of the default queries contained in the file QueryBuilderModule.py or
   - create a new one.

You can create two types of queries, namely <b> standard queries </b> and <b> parametric queries </b>.
To create a standard query, instantiate the class Query in QueryBuilderModule.py by typing
                     
    Query([(prefix, prefixIRI),...], query)

where: </br>
- [(prefix,prefixIRI)] is a list of tuples of strings formed by (prefix, prefiIRI), with "prefix" the prefix name and "prefixIRI" the IRI to be prefixed, which must be added to the list of         prefix in the query header.
- query is a string representing the query to be performed.
  
   
  
To create a parametric query, instantiate the class Query in QueryBuilderModule.py by typing
    
       Query([(prefix, prefixIRI),...], query, [(var1, parameter1), (var2, parameter2), ...])

where: </br>
- [(prefix,prefixIRI)] is a list of tuples of  strings of the form (prefix, prefiIRI), with "prefix" the prefix name and "prefixIRI" the IRI to be prefixed, which must be added to the list of         prefix in the query header.
- query is a string representing the query to be performed.
- [(var1, parameter1), (var2, parameter2), ...] is list of tuples of strings of the form "var1", "parameter1", where "var1" is the string  that must be replaced with "parameter1" in the query. 


You can also inherit the class QueryBuilderModule.py to create simplified queries.
The method 

      buildBody()
  
 returns the final body of the query possibly applying the defined substitutions, without the header containing the prefix definitions. Use the method
  
         self.getParameters()
         
  to return a list containing the parameters given in the constructor, and
         
         self.getQuery()
         
  to return the query, possibly without applying the given substitutions.

## Create a RepositoryManager

To create a repository manager type:

        repositoryMan=RepositoryManager([repository1, repository2, ...])
where:

- [repository1, repository2, ...] is a list of IRIs representing the repository to load.

You can add  repositories to an existing repository manager by typing:
     
        repositoryMan.addRepositories([repository1, repository2, ...])

You can remove repositories from an existing repository manager by typing:

         repositoryMan.addRepositories([repository1, repository2, ...]) 

## Create a ReasonerInterface

A reasoner interface can be created by typing

        reasonerInterface=ReasonerInterface("reasoner_name")

where "reasoner_name" is one of "HermiT" or "Pellet", the two currently supported reasoners.

## Perform queries

To perform a query, create an object of type CSE by typing:
       
          occse = OCCSE(repositoryManager, reasonerInterface)
         
where "repositoryManager" and "reasonerInterface" are the repository manager and the reasoner interface, respectively, as created before.

Then, load the repository by typing:

          occse.loadRepository()

Syncronized the reasoner by typing:

          occse.syncReasoner()

Add all the required prefixes in addition to the standard ones defined by POC4COMMERCE by typing

          occse.addPrefixes([(prefix, IRI), ...])
         
where:<\br>
- [(prefix, IRI), ...] is a list of tuples of strings representing the prefix and the prefixed IRI.
        
Finally, you can perform 
- either one of the standard queries by calling one of the methods "performQuery-CodeQuery-", where "-CodeQuery-" is the code of the standard query, or
- a custom query by typing 

      occse.performQuery(query)

where "query" is an object of type "Query" as created before, whose prefixes are neither one of the standard prefixes nor one of the prefixes added with the method "occse.addPrefixes". The output of "performQuery" can be formatted as desired.

Check the file
- test/occse-test/testQueryBuilder.py 

for some examples of using the QueryBuilder (change local path of ontologies) and

- test/occse-test/test_occse.py

for some examples of using the OCCSE module.
