# CS50-Introduction-to-Computer-Science
My journey into CS50 course.

# 🚀 My Computer Science & Python Journey (CS50)

Hi there! This repository serves as a personal archive for my progress, notes, and small projects as I navigate my way through computer science, building upon Harvard's **CS50** curriculum and my independent learning of **Python**.

## 📁 Repository Structure

* `propina.py`: A dynamic tip calculator that evaluates customer satisfaction and splits the final bill evenly among dinner guests.

---

## 🛠️ Featured Projects

### 📐 Efficient Tip Calculator (`propina.py`)
This is one of my first independent scripts written in Python. It helped me solidify the transition from the low-level, structured syntax of C to a high-level language.

**Key Features:**
* **Data Type Casting:** Handling user inputs by converting text (`input`) into floats (`float`) and integers (`int`) for precise mathematical calculations.
* **Conditional Logic:** Using `if`, `elif`, and `else` structures efficiently to determine the tip percentage based on the service quality ("good", "regular", "bad").
* **String Formatting:** Implementing optimized *f-strings* to display the final result with a clean, two-decimal place format (`:.2f`), accurately mimicking real currency.

### 🔎 Linear Inventory Search (`buscador.py`)
A script that emulates a linear search algorithm ($O(n)$). The program iterates through an item list step-by-step to determine if the requested element exists, returning its exact index position.

**Key Features:**
* **Loop Control Structures:** Utilizing a `for` loop combined with ranges based on the dynamic length of the list (`len()`).
* **Algorithm Optimization:** Implementation of the `break` statement to immediately halt execution once the target is found, preventing unnecessary computational overhead.

* ### 📊 Student Grades Tracker (`calificaciones.py`)
A script demonstrating the implementation of a Python dictionary to manage student records. This project highlights the transition from sequential array lookups to constant-time data retrieval using key-value pairs.

**Key Features:**
* **Constant Time Complexity ($O(1)$):** Leveraging hash tables (dictionaries) to instantly verify existence and retrieve student grades without iterative loops.
* **Dynamic Data Insertion:** Modifying and expanding the data structure at runtime by assigning user inputs directly to new keys.
* **Type Casting & String Formatting:** Ensuring mathematical data consistency by parsing inputs into floats and utilizing advanced string interpolation with `.format()`.

* ### 📝 Guest List Logger (`registro.py`)
A Python script that implements persistent data storage by reading and writing to external text files (`.txt`). This project marks the transition from volatile runtime memory (RAM) to persistent disk storage, simulating a real-world digital check-in system.

**Key Features:**
* **Persistent File I/O:** Using the modern `with open()` context manager to safely open, stream data, and automatically close files, preventing resource leaks or data corruption.
* **Append vs. Read Modes:** Utilizing the `"a"` (append) mode to write user inputs sequentially with newline characters (`\n`) without erasing historical logs, and the `"r"` (read) mode to fetch full contents.
* **File Automation:** Demonstrating Python's capability to autonomously detect and generate external `.txt` files at runtime if they do not already exist.
---

## 🧠 Technologies & Concepts Learned

* **Languages:** Python 3 (built upon a foundational understanding of C).
* **Low-Level Concepts:** Memory management, control flow, and the power of abstraction when moving to high-level languages.
* **Tools:** Version control using Git and GitHub.

---
*Documentation is constantly updated as I progress through the course. 💻*
