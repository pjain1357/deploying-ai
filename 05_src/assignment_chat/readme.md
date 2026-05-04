# Assignment 2: 
The goal of this assignment is to design and implement an AI system with a conversational interface.
In this assignment 3 tools have been introduced 
1) Currency converter : Convert the entered amount from one currency to another.
2) Metropolitan Museum of Art facts : Get the facts of european , american or africal art. LLM model will provide all the facts from the museum website
3) Art Institute of Chicago facts : Get the facts realted to asthetic art pieces 
Whenever the above type of inputs will be provided to chatbot it will route the information as input fed and generate the output by deciding which tool should be called.

## Services

This implementation is based on LangGraph's tools. 

The file main.py contains the llm model calls that controls the chat. Tools are in the files service_api.py and service_functioncall.py
The file app.py contains the gradio integration interacting with the llm model.

### Service 1: API Calls

+ There are a few API calls that we implemented throughout the course. 
+ The tools are added in *service_api.py* files.
+ Each tool is imported to main and included in the list `tools`.
+ The tools node uses LangGraph's `ToolNode` class and `tools_condition` is the standard tool stopping criteria.
+ All restrictions and tone requirements are in the instructions prompt which can be found in  prompts.py.

### Service 2: Semantic Query


### Service 3: Function call

+ It has been implemented to call the currency convertor tool in *service_functionCall.py* file. User will input the currency to be converted from and to in order to get the conversion.

## User Interface

+ Added conversational style.
+ Implemented in Gradio

---

## Guardrails and Other Limitations

* Include guardrails that prevent users from:

  * Accessing or revealing the system prompt.
  * Modifying the system prompt directly.

* The model must not respond to questions on certain restricted topics:

  * Cats or dogs
  * Horoscopes or Zodiac Signs
  * Taylor Swift
