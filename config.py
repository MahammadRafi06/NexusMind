"""
Configuration settings for the AI ReAct Agents Recommendation System.
"""
from typing import Dict, Any

# Model Configuration
MODEL_CONFIG: Dict[str, Any] = {
    "name": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2000,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

# Memory Configuration
MEMORY_CONFIG: Dict[str, Any] = {
    "store_type": "in_memory",  # Options: in_memory, redis, sqlite
    "max_items": 1000,
    "ttl": 3600  # Time to live in seconds
}

# Logging Configuration
LOGGING_CONFIG: Dict[str, Any] = {
    "level": "INFO",
    "format": "%(asctime)s %(levelname)s [%(name)s] %(message)s",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "file_size_limit": 10000000,  # 10MB
    "backup_count": 5
}

# Application Configuration
APP_CONFIG: Dict[str, Any] = {
    "batch_size": 5,
    "max_retries": 3,
    "retry_delay": 1.0,  # seconds
    "timeout": 30.0  # seconds
}

# Agent Configuration
AGENT_CONFIG: Dict[str, Any] = {
    "max_steps": 10,
    "max_iterations": 3,
    "stop_on_error": True
}

# Data Processing Configuration
DATA_CONFIG: Dict[str, Any] = {
    "input_encoding": "utf8",
    "max_message_length": 1000,
    "min_message_length": 1
}

# Monitoring Configuration
MONITORING_CONFIG: Dict[str, Any] = {
    "enabled": True,
    "interval": 60,  # seconds
    "metrics": [
        "message_count",
        "error_rate",
        "response_time",
        "memory_usage"
    ]
} 