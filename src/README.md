# Source Code (`src`)

This directory contains the computational implementations of the mathematical models discussed in the project. The scenarios are divided into two distinct examples, each solved using the environment best suited for its mathematical complexity.

## 📁 Directory Structure

### `example_1_maxima/`
Contains the analytical solution for the first problem.
*   **File:** `brine_tank.wxmx`
*   **Description:** A wxMaxima session solving the brine tank scenario (Example 1). It symbolically integrates the differential equation featuring a trigonometric concentration curve to find the exact amount of salt at the moment of tank overflow.

### `example_2_python/`
Contains the numerical simulation for the second problem.
*   **File:** `pollutants_simulation.py`
*   **Description:** A Python script solving the multi-stage pollutant retention tank scenario (Example 2). Due to the piecewise nature of the differential equation (flow parameters change after a specific pollutant threshold is reached), this script uses `scipy.integrate.solve_ivp` to compute the numerical solution and generates an animated plot of the concentration over time.

## 🚀 Execution Guide

*   **Python (Example 2):** To run the numerical simulation, navigate to the root of the repository and execute:
    ```bash
    python src/example_2_python/pollutants_simulation.py
    ```
    *(Ensure you have installed the dependencies from the root `requirements.txt` file first).*

*   **Maxima (Example 1):** To view the analytical derivation, simply open `src/example_1_maxima/brine_tank.wxmx` directly in the [wxMaxima](https://wxmaxima-developers.github.io/wxmaxima/) desktop application.
