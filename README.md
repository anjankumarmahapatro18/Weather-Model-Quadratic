
# Weather Modeling (Quadratic) — SE Exp-1

This project implements a simple *weather/temperature prediction* using a quadratic model:

> **T(t) = a·t² + b·t + c**

You will build it in four stages and also see how the same logic can be demonstrated with Waterfall, Iterative and Agile development modes.

## Folder Layout
```
weather_model_quadratic/
├── version1_hardcoded.py
├── version2_keyboard_input.py
├── version3_file_input_single.py
├── version4_file_input_multiple.py
├── inputs_single.txt
├── inputs_multiple.txt
├── main_modes_demo.py
└── README.md
```

## Quick Start
- Ensure you have Python 3.8+ installed.
- Open a terminal in this folder and run one of the versions below.

### 1) Hard-coded values
```
python version1_hardcoded.py
```

### 2) Keyboard input
```
python version2_keyboard_input.py
```

### 3) File input (single set)
```
python version3_file_input_single.py
```

### 4) File input (multiple sets)
```
python version4_file_input_multiple.py
```

### Modes demo (Waterfall / Iterative / Agile)
```
python main_modes_demo.py
```

## GitHub (suggested workflow)
1. Create a GitHub account (if you don’t have one).
2. Create a new public repository named `weather_model_quadratic`.
3. Initialize locally:
   ```bash
   git init
   git add .
   git commit -m "SE Exp-1: quadratic weather model (4 versions + modes demo)"
   git branch -M main
   git remote add origin https://github.com/<your-username>/weather_model_quadratic.git
   git push -u origin main
   ```
4. Continue to commit small changes as you debug and extend.
