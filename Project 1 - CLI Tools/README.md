# 🧮📦 CLI Tools Project — Calculator with History & Expense Tracker

*A Python learning project to master core syntax, OOP, scripting, and clean code practices through two powerful CLI tools.*



## 🎯 Goal  
Master **Python fundamentals** including functions, file I/O, error handling, type hints, basic OOP, and command-line scripting.  
Build **two reusable CLI tools**:  
- A **Calculator with History**  
- An **Expense Tracker**

All code follows **PEP8**, includes **docstrings**, and is tested using **pytest**.



## 📁 Project Structure

```
cli-tools/
│
├── calculator/               # A. Calculator with History
│   ├── operations.py         # Math functions (add, subtract, etc.)
│   ├── history.py            # Save/load calculation history
│   ├── main.py               # CLI interface for calculator
│   ├── utils.py              # Utility functions
│   └── test_calculator.py    # pytest tests
│
├── expense_tracker/          # B. Expense Tracker
│   ├── models.py             # Expense class definition
│   ├── tracker.py            # Core logic: add/search/export expenses
│   ├── cli.py                # Command-line interface
│   ├── storage.py            # JSON-based data persistence
│   ├── export.py             # Export to CSV
│   └── test_expense_tracker.py # pytest tests
│
├── README.md                 # You are here!
└── requirements.txt          # Project dependencies
```



## 🔧 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

### `requirements.txt`:
```
pytest>=7.0
black>=23.0  # For code formatting
isort>=5.0   # For import sorting
```



## 🧪 Running the Projects

### Run Calculator CLI:
```bash
cd calculator
python main.py
```

### Run Expense Tracker CLI:
```bash
cd expense_tracker
python cli.py --help
```

Example commands:
```bash
python cli.py add "Groceries" 45.99 food 2025-04-01
python cli.py search --category food
python cli.py export expenses.csv
```



## ✅ Unit Testing

Run tests using `pytest`:

### Test Calculator:
```bash
cd calculator
pytest test_calculator.py -v
```

### Test Expense Tracker:
```bash
cd expense_tracker
pytest test_expense_tracker.py -v
```



## 📝 Clean Code Practices Used

| Feature        | Description |
|----------------|-------------|
| **Type Hints** | Improve readability and help IDEs detect errors early. |
| **Docstrings** | Each function/class has a clear explanation of purpose and usage. |
| **Modular Functions** | Logic separated into reusable modules (`operations.py`, `storage.py`, etc.) |
| **PEP8 Compliant** | Consistent indentation, line length < 80 chars, proper naming. |
| **Error Handling** | Graceful handling of invalid input, division by zero, missing files, etc. |
| **Testing** | Every feature is backed by unit tests using `pytest`. |



## 💡 Tips for Learning

1. **Start small**: Implement one operation or feature at a time.
2. **Refactor often**: After building functionality, improve structure and readability.
3. **Write tests first** (TDD): Think about expected behavior before coding.
4. **Use linters/formatters**: Use `black` and `isort` to auto-format your code:
   ```bash
   black .
   isort .
   ```
5. **Read PEP8**: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)



## 🚀 What's Next?

After completing this project, you'll be ready to move on to [**Django basics**](https://github.com/onyxwizard/django-roadmap/tree/main?tab=readme-ov-file#%EF%B8%8F-phase-2-django-basics--full-stack-foundations) and start building full-stack web apps!


