import ast
import inspect


def extract_function_info(func):
    module = inspect.getmodule(func)
    module_name = module.__name__
    source = inspect.getsource(func)
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            parameters = [arg.arg for arg in node.args.args]
            docstring = ast.get_docstring(node)
            return module_name, func_name, parameters, docstring


def add_agent_info(agent_file, name, system, tools) -> str:
    with open(agent_file, "r") as f:
        agent_info = f.read()
    agent_info = agent_info.replace("{{name}}", name)
    agent_info = agent_info.replace("{{system}}", system)

    tools_info = ["## Tools available:\n"]
    for tool in tools:
        module_name, func_name, params, doc = extract_function_info(tool)
        tool_md = f"### {func_name}\n"
        tool_md += f"**Parameters**: {', '.join(params)}\n\n"
        tool_md += f"**Description**:\n\n{doc}\n"
        tools_info.append(tool_md)
    if len(tools) == 0:
        tools_info.append("### No tools are available")
    agent_info = agent_info + "\n".join(tools_info)
    return agent_info
