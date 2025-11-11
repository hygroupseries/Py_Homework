# Py_Homework
SXU Python Homework Repository

## Overview
This repository contains Python homework assignments and examples for SXU students.

## Structure
```
Py_Homework/
├── homework/          # Homework assignments go here
│   ├── __init__.py
│   └── example.py    # Example homework file
├── tests/            # Test files for homework
│   ├── __init__.py
│   └── test_example.py
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation
1. Clone this repository
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Running Examples
To run the example homework:
```bash
python homework/example.py
```

## Running Tests
To run tests manually:
```bash
python tests/test_example.py
```

Or using pytest (if installed):
```bash
pip install pytest
pytest tests/
```

## Adding New Homework
1. Create a new Python file in the `homework/` directory
2. Write your code with proper documentation
3. Create corresponding tests in the `tests/` directory
4. Run and verify your code works correctly

## Best Practices
- Write clean, readable code
- Add docstrings to functions and classes
- Test your code before submission
- Follow PEP 8 style guidelines

## License
See LICENSE file for details.
