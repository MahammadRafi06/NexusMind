"""
Test cases for node components of the recommendation system.
"""
import pytest
from langchain_core.messages import HumanMessage, SystemMessage
from components.nodes import task_mAIstro, update_todos, update_profile, update_instructions

def test_task_maistro():
    """Test the task_mAIstro node functionality."""
    # Test input message
    input_messages = [HumanMessage(content="Add a todo: Complete project documentation")]
    state = {"messages": input_messages}
    config = {"configurable": {"thread_id": "test_thread", "user_id": "test_user"}}
    
    # Process message
    result = task_mAIstro(state, config)
    
    # Assertions
    assert result is not None
    assert isinstance(result, dict)
    assert "messages" in result

def test_update_todos():
    """Test the update_todos node functionality."""
    # Test input
    input_messages = [
        HumanMessage(content="Add todo: Test the system"),
        SystemMessage(content="Processing todo update")
    ]
    state = {"messages": input_messages}
    config = {"configurable": {"thread_id": "test_thread", "user_id": "test_user"}}
    
    # Process update
    result = update_todos(state, config)
    
    # Assertions
    assert result is not None
    assert isinstance(result, dict)
    assert "messages" in result

def test_update_profile():
    """Test the update_profile node functionality."""
    # Test input
    input_messages = [
        HumanMessage(content="Update profile: Add Python expertise"),
        SystemMessage(content="Processing profile update")
    ]
    state = {"messages": input_messages}
    config = {"configurable": {"thread_id": "test_thread", "user_id": "test_user"}}
    
    # Process update
    result = update_profile(state, config)
    
    # Assertions
    assert result is not None
    assert isinstance(result, dict)
    assert "messages" in result

def test_update_instructions():
    """Test the update_instructions node functionality."""
    # Test input
    input_messages = [
        HumanMessage(content="Add instruction: Follow PEP 8 guidelines"),
        SystemMessage(content="Processing instruction update")
    ]
    state = {"messages": input_messages}
    config = {"configurable": {"thread_id": "test_thread", "user_id": "test_user"}}
    
    # Process update
    result = update_instructions(state, config)
    
    # Assertions
    assert result is not None
    assert isinstance(result, dict)
    assert "messages" in result 