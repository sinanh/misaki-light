#!/usr/bin/env python3
"""
Sample Python file to demonstrate misaki-light colorscheme syntax highlighting.

This module contains various Python constructs to showcase how different
syntax elements appear with the misaki-light color palette.
"""

import os
import sys
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    """A simple person class to demonstrate class definitions."""
    name: str
    age: int
    email: Optional[str] = None
    
    def __post_init__(self):
        """Validate person data after initialization."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
    
    def greet(self, greeting: str = "Hello") -> str:
        """Return a personalized greeting message."""
        return f"{greeting}, my name is {self.name}!"
    
    @property
    def is_adult(self) -> bool:
        """Check if person is an adult (18 or older)."""
        return self.age >= 18


class DataProcessor:
    """Demonstrates various Python features and syntax elements."""
    
    # Class variable
    DEFAULT_BATCH_SIZE = 100
    
    def __init__(self, data_source: str, batch_size: int = DEFAULT_BATCH_SIZE):
        self.data_source = data_source
        self.batch_size = batch_size
        self.processed_count = 0
        # Dictionary with mixed types
        self.config = {
            'enabled': True,
            'max_retries': 3,
            'timeout': 30.5,
            'endpoints': ['api.example.com', 'backup.example.com']
        }
    
    def process_data(self, items: List[Dict]) -> List[Dict]:
        """Process a batch of data items."""
        results = []
        
        for item in items:
            try:
                # String operations and f-strings
                processed_item = {
                    'id': item.get('id', f'auto_{self.processed_count}'),
                    'timestamp': datetime.now().isoformat(),
                    'status': 'processed'
                }
                
                # Conditional logic
                if 'priority' in item and item['priority'] > 5:
                    processed_item['urgent'] = True
                elif item.get('category') == 'important':
                    processed_item['flagged'] = True
                
                # List comprehension
                tags = [tag.strip().lower() for tag in item.get('tags', '').split(',') if tag.strip()]
                if tags:
                    processed_item['normalized_tags'] = tags
                
                results.append(processed_item)
                self.processed_count += 1
                
            except (KeyError, ValueError, TypeError) as e:
                # Error handling
                print(f"Error processing item {item}: {e}")
                continue
        
        return results
    
    @staticmethod
    def validate_config(config: Dict) -> bool:
        """Static method to validate configuration."""
        required_keys = ['enabled', 'max_retries', 'timeout']
        return all(key in config for key in required_keys)
    
    @classmethod
    def from_file(cls, filename: str) -> 'DataProcessor':
        """Class method to create processor from file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Configuration file not found: {filename}")
        return cls(filename)


def fibonacci(n: int) -> int:
    """Calculate fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def demonstrate_features():
    """Function showcasing various Python language features."""
    # Numbers and basic operations
    numbers = [1, 2, 3, 4, 5]
    pi = 3.14159
    is_enabled = True
    
    # String operations
    message = "Welcome to the misaki-light colorscheme demo!"
    formatted_msg = f"Current time: {datetime.now():%Y-%m-%d %H:%M:%S}"
    
    print(f"Numbers: {numbers}")
    print(f"Pi approximation: {pi}")
    print(f"Feature enabled: {is_enabled}")
    print(message)
    print(formatted_msg)
    
    # Dictionary and set operations
    word_count = {}
    unique_words = set()
    
    words = message.lower().split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        unique_words.add(word)
    
    # Generator expression
    even_squares = (x**2 for x in range(10) if x % 2 == 0)
    
    # Lambda function
    multiply = lambda x, y: x * y
    
    # Context manager usage
    try:
        with open('/tmp/demo.txt', 'w') as f:
            f.write("This is a demo file for syntax highlighting.\n")
            f.write(f"Word count: {word_count}\n")
    except IOError as e:
        print(f"File operation failed: {e}")
    
    return word_count, list(even_squares)


# Module-level constants
VERSION = "1.0.0"
AUTHOR = "Demo Author"
DEBUG = False

if __name__ == "__main__":
    # Main execution block
    print(f"Starting demo (version {VERSION})")
    
    # Create sample person
    person = Person("Alice", 25, "alice@example.com")
    print(person.greet("Hi there"))
    print(f"Is adult: {person.is_adult}")
    
    # Demonstrate data processing
    processor = DataProcessor("demo_data.json")
    sample_data = [
        {'id': 1, 'name': 'Item 1', 'priority': 8, 'tags': 'urgent, important'},
        {'id': 2, 'name': 'Item 2', 'category': 'important'},
        {'id': 3, 'name': 'Item 3', 'priority': 2}
    ]
    
    processed = processor.process_data(sample_data)
    print(f"Processed {len(processed)} items")
    
    # Calculate some fibonacci numbers
    fib_sequence = [fibonacci(i) for i in range(8)]
    print(f"Fibonacci sequence: {fib_sequence}")
    
    # Demonstrate other features
    word_stats, squares = demonstrate_features()
    print(f"Word statistics: {word_stats}")
    print(f"Even squares: {squares}")
    
    print("Demo completed successfully!")
