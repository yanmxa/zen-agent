# ZenAgent

![alt text](./asset/image.png)


**ZenAgent** empowers developers to create AI assistants, providing the capability to build sophisticated multi-agent systems. Its features include:

- Autonomy

  ZenAgent differ from those in systems like [AutoGen](https://microsoft.github.io/autogen/0.2/). With built-in tools, they operate independently, eliminating the need to rely on other agents for information. This allows them to iterate on a task before delivering results or involving another agent, reducing unnecessary interactions and agents.

- Tool Integration

  Unlike [LangChain](https://python.langchain.com/docs/how_to/custom_tools/) or [AutoGen](https://microsoft.github.io/autogen/0.2/docs/tutorial/tool-use/), which require following serval rules to register functions or tools, ZenAgent allows you to simply write a function and add a comment. The agent will automatically use the tool to solve tasks. See `sample/agent_tool.py` for a quick start.

- Governed Actions

  Actions performed by the ZenAgent are regulated by developers with three permission levels:  
  - **`auto`**: Requests permission only for actions that modify the system or environment; no permission is required for read actions.  
  - **`always`**: Requests permission for every action.  
  - **`none`**: Never requests permission.  

- Memory [Planning]  

  Enhances determinism and reduces redundant model invocations by adding memory capabilities.

- Event-Based Connection [Planning]

  Facilitates event-driven coordination for multi-agent interactions.