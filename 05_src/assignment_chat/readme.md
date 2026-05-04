# Assignment 2: A Sample Response



## Services

This implementation is based on LangGraph's tools. 

The file main.py contains the llm model calls that controls the chat. Tools are in the files service_

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
