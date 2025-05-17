"""
Logging configuration for the AI ReAct Agents Recommendation System.
"""
import logging
import os
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure logging
def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a custom logger."""
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s [%(name)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    handler = RotatingFileHandler(
        log_file,
        maxBytes=10000000,  # 10MB
        backupCount=5
    )
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    # Also log to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

# Create different loggers for different components
main_logger = setup_logger('main', 'logs/main.log')
agent_logger = setup_logger('agent', 'logs/agent.log')
memory_logger = setup_logger('memory', 'logs/memory.log')

class LoggerMixin:
    """Mixin to add logging capabilities to classes."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def log_event(self, event_type, data):
        """Log an event with structured data."""
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'data': data
        }
        self.logger.info(json.dumps(log_entry))
    
    def log_error(self, error_type, error_message, details=None):
        """Log an error with details."""
        error_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'error_type': error_type,
            'error_message': error_message,
            'details': details or {}
        }
        self.logger.error(json.dumps(error_entry))

# Example usage:
# from components.logger import LoggerMixin, main_logger
#
# class MyComponent(LoggerMixin):
#     def process_data(self, data):
#         self.log_event('processing_started', {'input_data': data})
#         try:
#             # Process data
#             result = do_something(data)
#             self.log_event('processing_completed', {'result': result})
#         except Exception as e:
#             self.log_error('processing_failed', str(e), {'input_data': data}) 