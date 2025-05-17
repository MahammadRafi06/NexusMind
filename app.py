import os
from dotenv import load_dotenv
from typing import List, Dict, Any
from components.logger import main_logger, LoggerMixin

# Load environment variables
load_dotenv()

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.store.memory import InMemoryStore

from components.nodes import task_mAIstro, update_todos, update_profile, update_instructions
from components.conditional_edges import route_message, intermediate

class RecommendationSystem(LoggerMixin):
    """Main class for the AI ReAct Agents Recommendation System."""
    
    def __init__(self):
        """Initialize the recommendation system."""
        super().__init__()
        self.setup_environment()
        self.setup_graph()
        self.load_data()
    
    def setup_environment(self):
        """Setup environment variables and configuration."""
        try:
            required_vars = [
                "OPENAI_API_KEY",
                "LANGCHAIN_API_KEY",
                "LANGCHAIN_PROJECT"
            ]
            
            missing_vars = [var for var in required_vars if not os.getenv(var)]
            if missing_vars:
                raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
            os.environ["LANGCHAIN_TRACING_V2"] = "true"
            os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
            
            self.log_event("environment_setup", {"status": "completed"})
        except Exception as e:
            self.log_error("environment_setup_failed", str(e))
            raise
    
    def setup_graph(self):
        """Setup the LangGraph components."""
        try:
            builder = StateGraph(MessagesState)
            
            # Add nodes
            builder.add_node(task_mAIstro)
            builder.add_node(update_todos)
            builder.add_node(update_profile)
            builder.add_node(update_instructions)
            
            # Add edges
            builder.add_edge(START, "task_mAIstro")
            builder.add_conditional_edges("task_mAIstro", route_message, intermediate)
            builder.add_edge("update_todos", "task_mAIstro")
            builder.add_edge("update_profile", "task_mAIstro")
            builder.add_edge("update_instructions", "task_mAIstro")
            
            # Setup memory
            self.across_thread_memory = InMemoryStore()
            self.within_thread_memory = MemorySaver()
            
            # Compile graph
            self.graph = builder.compile(
                checkpointer=self.within_thread_memory,
                store=self.across_thread_memory
            )
            
            self.log_event("graph_setup", {"status": "completed"})
        except Exception as e:
            self.log_error("graph_setup_failed", str(e))
            raise
    
    def load_data(self):
        """Load and process input data."""
        try:
            import re
            with open("./data/fifa2026.txt", encoding="utf8") as f:
                fifa = f.readlines()
                fifa = [item.strip() for item in fifa if item != '\n']
                self.messages = []
                
                for i, text in enumerate(fifa):
                    match = re.search(r'\[@([^\s]+)', text)
                    if match:
                        rest, post = text.rsplit(sep="M]")
                        if post:
                            self.messages.append({
                                "user_id": match.group(1),
                                "message": post
                            })
                    else:
                        self.log_event("data_processing", {
                            "status": "skipped",
                            "line": i,
                            "reason": "no_match"
                        })
                
                self.log_event("data_loading", {
                    "status": "completed",
                    "messages_count": len(self.messages)
                })
        except Exception as e:
            self.log_error("data_loading_failed", str(e))
            raise
    
    def process_messages(self, start_idx: int = 0, batch_size: int = 5) -> List[Dict[str, Any]]:
        """Process a batch of messages through the recommendation system."""
        try:
            results = []
            end_idx = min(start_idx + batch_size, len(self.messages))
            
            for msg in self.messages[start_idx:end_idx]:
                config = {
                    "configurable": {
                        "thread_id": "1",
                        "user_id": msg["user_id"]
                    }
                }
                
                input_messages = [HumanMessage(content=msg["message"])]
                
                try:
                    result = self.graph.invoke({"messages": input_messages}, config)
                    results.append({
                        "user_id": msg["user_id"],
                        "status": "success",
                        "result": result
                    })
                    
                    self.log_event("message_processed", {
                        "user_id": msg["user_id"],
                        "status": "success"
                    })
                except Exception as e:
                    results.append({
                        "user_id": msg["user_id"],
                        "status": "error",
                        "error": str(e)
                    })
                    
                    self.log_error("message_processing_failed",
                                 str(e),
                                 {"user_id": msg["user_id"]})
            
            return results
        except Exception as e:
            self.log_error("batch_processing_failed", str(e))
            raise
    
    def get_user_memories(self, user_id: str) -> Dict[str, List[Any]]:
        """Retrieve all memories for a specific user."""
        try:
            memories = {}
            for memory_type in ['profile', 'todo', 'instructions']:
                namespace = (memory_type, user_id)
                memories[memory_type] = self.across_thread_memory.search(namespace)
            
            self.log_event("memories_retrieved", {
                "user_id": user_id,
                "memory_types": list(memories.keys())
            })
            
            return memories
        except Exception as e:
            self.log_error("memory_retrieval_failed",
                          str(e),
                          {"user_id": user_id})
            raise

def main():
    """Main entry point for the application."""
    try:
        main_logger.info("Starting recommendation system")
        system = RecommendationSystem()
        
        # Process first batch of messages
        results = system.process_messages(start_idx=0, batch_size=5)
        
        # Print results for demonstration
        for msg in system.messages[0:5]:
            memories = system.get_user_memories(msg["user_id"])
            print(f"\nUser: {msg['user_id']}")
            for memory_type, memory_data in memories.items():
                print(f"{memory_type}: {memory_data}")
            print("*" * 40)
        
        main_logger.info("Recommendation system completed successfully")
    except Exception as e:
        main_logger.error(f"Recommendation system failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
    
