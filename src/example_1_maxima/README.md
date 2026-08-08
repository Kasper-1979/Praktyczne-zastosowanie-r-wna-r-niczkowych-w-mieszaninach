# Example 1: Analytical Brine Tank Solution

## 📌 Problem Overview
This directory contains the mathematical derivation and solution for the first differential equation scenario. 

The problem models a 1500-gallon tank initially holding 600 gallons of water with 5 lbs of dissolved salt. Brine flows into the tank at a rate of 9 gal/h, with a fluctuating salt concentration given by the trigonometric function $c_{in}(t) = \frac{1}{5}(1+\cos(t))$ lbs/gal. The well-mixed solution leaves the tank at 6 gal/h. The objective is to determine the exact amount of salt in the tank at the moment it overflows (at $t = 300$ hours).

## 🧮 Mathematical Model
The mixing process is modeled by the following linear differential equation:

$$ \frac{dQ}{dt} = F_{in} \cdot c_{in}(t) - \frac{Q(t)}{V(t)} \cdot F_{out} $$

Where:
*   $Q(t)$ is the amount of salt in the tank at time $t$.
*   $V(t) = 600 + (9 - 6)t$ is the volume of the mixture at time $t$.
*   $F_{in}$ and $F_{out}$ represent the inflow and outflow rates, respectively.

## 📄 File Contents
*   **`brine_tank.wxmx`** - A wxMaxima session containing the full analytical integration of the differential equation, the initial condition setup, and the generation of an animated plot showing the salt quantity over time.

## 🚀 How to Run
1. Download and install [wxMaxima](https://wxmaxima-developers.github.io/wxmaxima/).
2. Open `brine_tank.wxmx` in the application.
3. Evaluate all cells to view the step-by-step symbolic integration and the final numerical output (approx. 279.797 lbs).
