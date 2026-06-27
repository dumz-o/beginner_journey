# Electrical Engineering Foundation: Python Journey

I am an aspiring Electrical Engineer using Python to build practical engineering utilities, circuit calculators, and physics models. This repository serves as a live log of my programming foundations and technical growth, specifically targeting future applications in power electronics and renewable systems.

---

## 🚀 Foundational Utilities Portfolio

### 1. Multivariable Resistor Circuit Calculator (`resistor_calc.py`)
* **Function:** Computes total resistance for 2, 3, or 4 resistors in both series and parallel configurations.
* **Engineering Focus:** Implements strict user input validation and error handling (`try`/`except` blocks) to prevent system crashes from incorrect data entry, ensuring reliable physical calculations.

### 2. Ohm's Law Calculator (`ohms_law.py`)
* **Function:** Calculates an unknown electrical property (Voltage, Current, or Resistance) dynamically based on two known user-provided variables.
* **Engineering Focus:** Focuses on clean control flow routing, mapping standard $V = I \times R$ equations to programmatic logic.

### 3. Temperature Scale Converter (`temp_converter.py`)
* **Function:** Dynamically converts values between Celsius, Fahrenheit, and Kelvin based on user selection.
* **Engineering Focus:** Handles data type casting (string to float) and utilizes multi-variable matching logic to route specific physics formulas based on input units.

### 4. Century Milestone Tracker (`age_to_100.py`)
* **Function:** Computes the exact years remaining until a user turns 100 and outputs a context-aware message based on their current life stage.
* **Engineering Focus:** Implements defensive data type validation by attempting string-to-float conversions to systematically isolate and flag numerical entry errors in text fields.

### 5. Academic Score Grader (`score_grader.py`)
* **Function:** Accepts decimal scores between 0.0 and 1.0 to assign standardized academic letter grades (A through F).
* **Engineering Focus:** Utilizes strict range validation ($0.0 \le \text{score} \le 1.0$) as a boundary constraint to catch and filter out logical data entry anomalies before processing.

### 6. Product-or-Sum Threshold Evaluator (`product_or_sum.py`)
* **Function:** Evaluates the product of two integers, dynamically defaulting to their sum if the product crosses a set threshold of 1000.
* **Engineering Focus:** Establishes the baseline entry of this portfolio, verifying fundamental variable management, casting, and conditional binary branching mechanics.

---

## 🛠️ Core Technical Competencies Demonstrated

* **Defensive Programming:** Active implementation of error handling (`try`/`except` blocks) to manage unpredictable data inputs safely without runtime failure.
* **Data Sanitization:** Converting raw console inputs into structural numeric formats (`float`/`int`) to maintain mathematical calculation integrity.
* **Deterministic Control Flow:** Constructing clean conditional routing pipelines designed to map onto physical calculations, algebraic equations, and engineering constraints.
