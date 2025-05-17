# NexusMind

An intelligent recommendation system where AI agents work together like a neural network, learning and adapting to user preferences in real-time. Built with LangChain and LangGraph to create a system that remembers past interactions and understands context, making each recommendation more personalized than the last.

## 🌟 Features

- **Intelligent Task Management**: AI-powered task orchestration and prioritization
- **User Profiling**: Dynamic user profile creation and updates
- **Smart Recommendations**: Context-aware recommendation generation
- **Memory Management**: Both in-memory and persistent storage for user interactions
- **Reactive Architecture**: Event-driven system using LangGraph for workflow management

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key
- LangChain API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MahammadRafi06/NexusMind.git
cd NexusMind
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## 🏗️ Project Structure

```
.
├── app.py                 # Main application entry point
├── components/           # Core components of the system
│   ├── nodes.py         # Agent nodes implementation
│   ├── conditional_edges.py  # Routing logic
│   ├── helper.py        # Utility functions
│   ├── prompts.py       # System prompts
│   └── data_loader.py   # Data processing utilities
├── data/                # Data storage
└── tests/              # Test suite
```

## 🔧 Architecture

The system uses a graph-based architecture with the following key components:

1. **Task MAIstro**: Central orchestrator for task management
2. **Profile Manager**: Handles user profile creation and updates
3. **Todo Manager**: Manages user tasks and priorities
4. **Instruction Handler**: Processes and manages system instructions

### Workflow

1. User input is received and processed by the Task MAIstro
2. The input is routed to appropriate handlers based on content
3. Handlers process the input and update relevant states
4. System maintains memory across sessions for consistent interactions

## 🛠️ Usage

```python
from app import graph

# Initialize the graph with configuration
config = {
    "configurable": {
        "thread_id": "1",
        "user_id": "user123"
    }
}

# Process user input
input_messages = [HumanMessage(content="Your message here")]
response = graph.invoke({"messages": input_messages}, config)
```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

## 📊 Monitoring

The system integrates with LangSmith for monitoring and tracking:
- Performance metrics
- Agent interactions
- Memory usage
- Response quality

## 🔐 Security

- All API keys should be stored in environment variables
- User data is handled securely
- Memory storage is isolated per user

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For questions and support, please open an issue in the GitHub repository.