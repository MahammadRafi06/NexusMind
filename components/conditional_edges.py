from langgraph.graph import StateGraph, MessagesState, END, START
from langchain_core.runnables import RunnableConfig
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore
from typing import Annotated, Sequence

# Conditional edge
def route_message(state: MessagesState, config: RunnableConfig, store: BaseStore) ->  Sequence[str]:

    """Reflect on the memories and chat history to decide whether to update the memory collection."""
    message = state['messages'][-1]
    if len(message.tool_calls) ==0:
        return [END]
    elif len(message.tool_calls) == 1:
        tool_call = message.tool_calls[0]
        if tool_call['args']['update_type'] == "user":
            return ["update_profile"]
        elif tool_call['args']['update_type'] == "todo":
            return ["update_todos"]
        elif tool_call['args']['update_type'] == "instructions":
            return ["update_instructions"]
        else:
            raise ValueError
    elif len(message.tool_calls) == 2:
        tool_call = message.tool_calls
        if (tool_call[0]['args']['update_type'] == "user" and tool_call[1]['args']['update_type'] == "todo") or tool_call[0]['args']['update_type'] == "todo" and tool_call[1]['args']['update_type'] == "user":
            return ["update_profile","update_todos"]
        if (tool_call[0]['args']['update_type'] == "user" and tool_call[1]['args']['update_type'] == "instructions") or tool_call[0]['args']['update_type'] == "instructions" and tool_call[1]['args']['update_type'] == "user":
            return ["update_profile","update_instructions"]
        if (tool_call[0]['args']['update_type'] == "instructions" and tool_call[1]['args']['update_type'] == "todo") or tool_call[0]['args']['update_type'] == "todo" and tool_call[1]['args']['update_type'] == "instructions":
            return ["update_instructions","update_todos"]
    else:
        return ["update_profile","update_todos","update_instructions"]
intermediate = ["update_profile","update_todos","update_instructions", END]