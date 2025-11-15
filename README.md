# Parametric Curve Optimization Using Differential Evolution

## 🧩 Overview
This project performs **parametric curve fitting** on a dataset (`xy_data.csv`) by estimating three unknown parameters of a nonlinear parametric model:

- **θ** — rotation angle  
- **M** — exponential scaling factor  
- **X** — horizontal shift  

The goal is to minimize the **L1 error** between the model-generated curve and the observed data points.

---

## 📐 Mathematical Model

The parametric curve is defined as:

\[
x(t) = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
\]

\[
y(t) = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
\]

---

## 🎯 Optimization Objective

The objective is to find parameters \(\theta\), \(M\), and \(X\) that minimize:

\[
L = \sum_i \left( |x_i - \hat{x}_i| + |y_i - \hat{y}_i| \right)
\]

where \((x_i, y_i)\) are observed data points and \((\hat{x}_i, \hat{y}_i)\) are model predictions.

---

## 🚀 Approach

The optimization is performed using **Differential Evolution (DE)**, a global optimization algorithm suited for nonlinear, non-convex problems.  
The script:

1. Loads dataset  
2. Generates model predictions  
3. Computes L1 loss  
4. Runs Differential Evolution  
5. Outputs optimal parameters  
6. Saves fitted curve plot  

---

## 📁 Project Structure

```
project/
 ├── optimize_curve.py
 ├── xy_data.csv
 ├── plots/
 │    └── fitted_curve.png
 └── README.md
```

---

## ▶ How to Run

### Install dependencies
```bash
pip install numpy pandas scipy matplotlib
```

### Execute the script
```bash
python optimize_curve.py
```

---

## 🏆 Final Optimization Results

```
Optimal angle (θ): 0.4910 radians ≈ 28.14°
Optimal M value: 0.0213
Optimal X shift: 54.9236
Total L1 error: 37865.168202
```

---

## 📌 LaTeX Expression for Report

\[
\left(
t\cos(0.4910)
- e^{0.0213|t|}\sin(0.3t)\sin(0.4910)
+ 54.9236,\;
42 + t\sin(0.4910)
+ e^{0.0213|t|}\sin(0.3t)\cos(0.4910)
\right)
\]

---

## 📊 Plot

A visualization of the observed data and the optimized curve is saved here:

```
plots/fitted_curve.png
```

---

## ✔ Academic Integrity

All explanations, descriptions, and documentation in this README are original and written specifically for this project.

