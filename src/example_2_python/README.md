# Example 2: Multi-Stage Pollutant Tank Simulation

## 📌 Problem Overview
This directory contains the numerical simulation for the second differential equation scenario, which models a 1000-gallon retention tank catching chemical wastewater. 

The process is divided into two stages due to changing physical conditions:
*   **Stage 1:** The tank initially holds 800 gallons of water with 2 oz of pollutants. Polluted water (5 oz/gal) enters at 3 gal/h, and the well-mixed solution leaves at 3 gal/h. This stage continues until the total pollutants reach a critical threshold of 500 oz.
*   **Stage 2:** Once the 500 oz limit is reached, the polluted inflow is shut off. Fresh water then enters at a reduced rate of 2 gal/h, while the outflow increases to 4 gal/h.

## 🧮 Mathematical Model
Because the flow parameters change drastically after a threshold is reached, a piece-wise differential equation is required to model the system.

**Stage 1 Equation:**
$$ \frac{dQ_1}{dt} = 15 - 3 \cdot \frac{Q_1(t)}{800} $$ 

**Stage 2 Equation (starting at $t_m$):**
$$ \frac{dQ_2}{dt} = -4 \cdot \frac{Q_2(t)}{800 - 2(t - t_m)} $$ 

## 📄 File Contents
*   **`pollutants_simulation.py`** - A Python script that utilizes `scipy.integrate.solve_ivp` to solve the piece-wise differential equations. It calculates the exact time ($t_m$) the 500 oz threshold is met and renders a dynamic, animated plot of the pollutant concentration over time using Matplotlib.

## 🚀 How to Run
To run the simulation and view the animation, execute the following command from the root of the repository:
```bash
python src/example_2_python/pollutants_simulation.py
```
* *(Requires numpy, scipy, and matplotlib)*
