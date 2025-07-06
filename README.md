# NexusMind: Intelligent AI Agent Ecosystem

An advanced recommendation system where AI agents collaborate like a neural network, learning and adapting to user preferences in real-time. Built with LangChain and LangGraph for context-aware, personalized interactions.

## Overview

NexusMind represents a breakthrough in AI-driven recommendation systems. Unlike traditional static recommendation engines, NexusMind creates an ecosystem of intelligent agents that learn, adapt, and evolve based on user interactions. The system maintains persistent memory across sessions, understands context, and provides increasingly personalized recommendations over time.

## Key Features

- **Adaptive AI Agents**: Dynamic agents that learn from every interaction
- **Persistent Memory**: Both in-memory and cross-session storage for consistent experiences
- **Context Awareness**: Deep understanding of user preferences and behavior patterns
- **Real-time Learning**: Continuous adaptation without retraining
- **Scalable Architecture**: Event-driven system using LangGraph workflows
- **Multi-user Support**: Isolated memory and preferences per user
- **Comprehensive Monitoring**: LangSmith integration for performance tracking

## System Architecture

The system employs a graph-based architecture with intelligent routing:

```
User Input → Task MAIstro → Router → [Profile Manager | Todo Manager | Instruction Handler] → Memory Store → Response
```

### Core Components

1. **Task MAIstro**: Central orchestrator for all user interactions
2. **Profile Manager**: Maintains and updates user profiles dynamically
3. **Todo Manager**: Handles task creation, updates, and prioritization
4. **Instruction Handler**: Processes user preferences and system instructions
5. **Memory Store**: Persistent storage for user data and preferences

## Project Structure

```
NexusMind/
├── components/
│   ├── nodes.py             # Agent node implementations
│   ├── conditional_edges.py # Intelligent routing logic
│   ├── helper.py            # Utility functions
│   ├── prompts.py           # System prompts and templates
│   ├── data_loader.py       # Data processing utilities
│   ├── logger.py            # Logging configuration
│   └── cls.py               # Data classes and models
├── data/                    # Sample data and templates
│   ├── fifa2026.txt         # Sample user interactions
│   └── quantum.txt          # Sample conversation data
├── tests/                   # Comprehensive test suite
├── app.py                   # Main application entry point
├── config.py                # Configuration management
├── requirements.txt         # Dependencies
└── Jenkinsfile             # CI/CD pipeline
```

## Installation

### Prerequisites

- Python 3.9+
- OpenAI API key
- LangChain API key
- LangSmith account (for monitoring)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MahammadRafi06/NexusMind.git
   cd NexusMind
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

   Required environment variables:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_project_name
   LANGCHAIN_TRACING_V2=true
   ```

## Usage

### Basic Usage

```python
from app import RecommendationSystem

# Initialize the system
system = RecommendationSystem()

# Process user messages
config = {
    "configurable": {
        "thread_id": "user_session_1",
        "user_id": "user123"
    }
}

# Send a message
messages = [HumanMessage(content="I need help organizing my tasks")]
response = system.graph.invoke({"messages": messages}, config)
```

### Advanced Configuration

```python
# Custom configuration
system = RecommendationSystem()
system.setup_custom_config({
    "memory_type": "persistent",
    "learning_rate": 0.1,
    "context_window": 10
})

# Batch processing
results = system.process_messages(start_idx=0, batch_size=10)
```

## Memory Management

NexusMind employs a sophisticated memory system:

### Memory Types

1. **User Profile**: Personal information and preferences
2. **Todo List**: Tasks, priorities, and completion status
3. **Instructions**: Custom user preferences for system behavior

### Memory Operations

- **Automatic Updates**: System learns from every interaction
- **Context Retention**: Maintains conversation history
- **Cross-session Persistence**: Remembers users across sessions
- **Intelligent Retrieval**: Contextual memory access

## Agent Workflow

### 1. Input Processing
- User input is received by Task MAIstro
- Intent classification and context extraction
- Routing to appropriate handler

### 2. Memory Retrieval
- Fetch relevant user profile information
- Load current todo list and preferences
- Retrieve conversation history

### 3. Processing
- Specialized agents process the request
- Memory updates based on new information
- Response generation with context

### 4. Response Delivery
- Formatted response to user
- Memory persistence
- Metrics logging

## Configuration

The system uses multiple configuration layers:

### Model Configuration
```yaml
MODEL_CONFIG:
  name: "gpt-4"
  temperature: 0.7
  max_tokens: 2000
```

### Memory Configuration
```yaml
MEMORY_CONFIG:
  store_type: "in_memory"
  max_items: 1000
  ttl: 3600
```

### Agent Configuration
```yaml
AGENT_CONFIG:
  max_steps: 10
  max_iterations: 3
  stop_on_error: true
```

## Monitoring and Analytics

### LangSmith Integration

- **Performance Metrics**: Response times, success rates
- **Agent Interactions**: Detailed workflow analysis
- **Memory Usage**: Storage optimization insights
- **Quality Metrics**: Response quality assessment

### Custom Metrics

```python
# Track custom metrics
system.log_event("user_interaction", {
    "user_id": "user123",
    "action": "task_creation",
    "success": True
})
```

## Testing

### Run Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_nodes.py -v

# Run with coverage
pytest tests/ --cov=components --cov-report=html
```

### Test Categories

- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end workflow testing
- **Performance Tests**: Load and stress testing
- **Memory Tests**: Memory leak and efficiency testing

## Deployment

### Local Development

```bash
python app.py
```

### Production Deployment

```bash
# Using Docker
docker build -t nexusmind .
docker run -p 8000:8000 nexusmind

# Using Kubernetes
kubectl apply -f k8s/
```

## API Reference

### Core Methods

```python
# Process messages
system.process_messages(start_idx=0, batch_size=5)

# Get user memories
memories = system.get_user_memories("user123")

# Update configuration
system.update_config(new_config)
```

## Performance Optimization

### Memory Optimization

- Efficient data structures for fast retrieval
- Automatic memory cleanup and archival
- Configurable memory limits

### Processing Optimization

- Parallel agent execution
- Intelligent caching
- Batch processing capabilities

## Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Write tests** for new functionality
4. **Ensure code quality** (run linters and tests)
5. **Commit changes** (`git commit -m 'Add amazing feature'`)
6. **Push to branch** (`git push origin feature/amazing-feature`)
7. **Open Pull Request**

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run pre-commit hooks
pre-commit install

# Run linters
flake8 components/
black components/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**MahammadRafi**
- GitHub: [@MahammadRafi06](https://github.com/MahammadRafi06)
- Email: mrafi@uw.edu

## Acknowledgments

- LangChain team for the agent framework
- OpenAI for language models
- LangSmith for monitoring and analytics
- Open source AI community for inspiration and tools

## Support

For questions and support:
- Open an issue on GitHub
- Check the documentation
- Join our community discussions

## Roadmap

- [ ] Enhanced memory algorithms
- [ ] Multi-modal input support
- [ ] Advanced analytics dashboard
- [ ] Plugin architecture
- [ ] Mobile application support