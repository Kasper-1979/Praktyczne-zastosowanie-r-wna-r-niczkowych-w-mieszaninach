# Practical Application of Differential Equations in Mixtures

## 📌 Project Overview
This repository explores the practical application of differential equations to model the mixing of substances in liquids. It contains mathematical derivations, programmatic simulations, and visualizations to solve practical engineering scenarios, such as tracking salt concentration or impurity levels in tanks over time as solutions flow in and out. 

Because of the varying complexity of the problems, two different environments were used: **wxMaxima** for continuous analytical solutions and **Python** for complex, multi-stage numerical simulations.

## 📂 Repository Structure
The project is structured to maintain a clean separation between source code, documentation, and execution results.

*   `src/` - Contains the source code and mathematical files for the scenarios.
    *   **`example1_brine_tank.wxmx`** - A wxMaxima session solving **Example 1**: A 1500-gallon tank receiving a brine solution with a trigonometric concentration curve over time. It features a fully analytical solution.
    *   **`example2_pollutants.py`** - A Python script using `scipy.integrate.solve_ivp` to solve **Example 2**: A two-stage chemical pollutant retention tank problem. Python was chosen here due to the complexity of the piece-wise differential equation where the flow parameters drastically change after a threshold is reached.
*   `docs/` - Contains project documentation.
    *   `project_report.pdf` (or .docx) - The main theoretical document and report detailing the mathematical models and the context of the solved examples.
    *   `presentation.pptx` - A presentation summarizing the project's findings.
*   `results/` - Contains the output data.
    *   `results.txt` - Console output and error logs generated during the Python script execution.

## ⚙️ Setup & Installation
To run the Python multi-stage simulation, you need to install the required dependencies.

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Kasper-1979/Praktyczne-zastosowanie-r-wna-r-niczkowych-w-mieszaninach.git](https://github.com/Kasper-1979/Praktyczne-zastosowanie-r-wna-r-niczkowych-w-mieszaninach.git)
    cd Praktyczne-zastosowanie-r-wna-r-niczkowych-w-mieszaninach
    ```
2.  Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `numpy`, `scipy`, `matplotlib`, and `pillow` are required).*

## 🚀 Usage

### 1. Multi-Stage Tank Simulation (Python)
To run the numerical simulation for Example 2 and view the animated piece-wise graph of the pollutant concentration:
```bash
python src/example2_pollutants.py
```

### 2. Analytical Brine Tank Solution (wxMaxima)
To view the symbolic math derivation for Example 1:

1. Ensure you have wxMaxima installed.

2. Open the file src/example1_brine_tank.wxmx using the wxMaxima application to see the formulas and the generated plot.

## 👥 Authors
Kacper Lis
