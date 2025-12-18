# Python FastAPI Project

## Project Description
This is a Python project built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.14+ based on standard Python type hints.

## Features
- RESTful API endpoints
- Dependency injection
- Automatic interactive API documentation with Swagger UI
- Asynchronous request handling

## Project Structure
```
python-fashapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── api/
│       ├── routes.py
│       └── __pycache__/
├── tests/
│   ├── test_main.py
│   └── __pycache__/
├── pyproject.toml
├── pytest.ini
└── .gitignore
```

## Requirements
- Python 3.14+
- Poetry (for dependency management)

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:xiaotaozi1127/python-fastAPI.git
   cd python-fashapi
   ```

2. Install Poetry:
   Follow the instructions at [Poetry's official documentation](https://python-poetry.org/docs/#installation) to install Poetry.

3. Configure Poetry to create the virtual environment inside the project:
   ```bash
   poetry config virtualenvs.in-project true
   ```

4. Install dependencies:
   ```bash
   poetry install
   ```

## Running the Application
To start the FastAPI application, run:
```bash
poetry run uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Running Tests
To run the test suite, use:
```bash
poetry run pytest ./tests
```

## Running the Games

### Mastermind Game
To play the Mastermind game, run:
```bash
python mastermind.py
```

### Yes/No Guessing Game
To play the Yes/No Guessing game, run:
```bash
python yes_no_game.py
```

## API Documentation
FastAPI automatically generates interactive API documentation. Once the application is running, you can access it at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## License
This project is licensed under the MIT License. See the LICENSE file for details.