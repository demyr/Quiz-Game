# Quiz Game

A simple command-line quiz application built with Python. This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" course. It demonstrates object-oriented programming (OOP) principles by using classes to model questions and manage the game logic.

## Features

- **Dynamic Question Bank**: Loads questions and answers from a data source.
- **Score Tracking**: Keeps track of the user's current and final score.
- **Interactive Interface**: Prompts the user with questions and provides immediate feedback.
- **Object-Oriented Design**: Cleanly separated concerns using `Question` and `QuizBrain` classes.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd day-17-start/quiz-game-start
   ```

### Running the App

Run the `main.py` script to start the quiz:

```bash
python3 main.py
```

## How it Works

- **`main.py`**: The entry point of the application. It initializes the question bank and starts the quiz loop.
- **`data.py`**: Contains the list of question data (text and answers).
- **`question_model.py`**: Defines the `Question` class with `text` and `answer` attributes.
- **`quiz_brain.py`**: Contains the `QuizBrain` class, which manages the quiz logic, including navigation between questions, checking answers, and scorekeeping.

## File Structure

```text
quiz-game-start/
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
└── __pycache__/
```

## Acknowledgments

- Inspired by the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu.
