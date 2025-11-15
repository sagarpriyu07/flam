import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
import os

# --- Folder Setup ---
os.makedirs("plots", exist_ok=True)
os.makedirs("results", exist_ok=True)

# --- Parametric Model Definitions ---
def param_x(t, angle, mag, shift):
    return t * np.cos(angle) - np.exp(mag * np.abs(t)) * np.sin(0.3 * t) * np.sin(angle) + shift

def param_y(t, angle, mag, shift):
    return 42 + t * np.sin(angle) + np.exp(mag * np.abs(t)) * np.sin(0.3 * t) * np.cos(angle)

# --- Load Data ---
dataset = pd.read_csv("xy_data.csv")
x_data = dataset["x"].to_numpy()
y_data = dataset["y"].to_numpy()
t_values = np.linspace(6, 60, len(x_data))

# --- L1 Loss Function ---
def loss_function(params):
    angle, mag, shift = params
    x_pred = param_x(t_values, angle, mag, shift)
    y_pred = param_y(t_values, angle, mag, shift)
    diff = np.abs(x_data - x_pred) + np.abs(y_data - y_pred)
    return np.sum(diff)

# --- Differential Evolution Optimization ---
param_bounds = [(0, 0.8727), (-0.05, 0.05), (0, 100)]
opt_result = differential_evolution(loss_function, bounds=param_bounds, maxiter=300, polish=True)
angle_opt, mag_opt, shift_opt = opt_result.x

# --- Values to Save ---
deg_angle = np.degrees(angle_opt)
L1_error = opt_result.fun

latex_expr = (
    f"( t·cos({angle_opt:.4f}) - e^({mag_opt:.4f}|t|)·sin(0.3t)·sin({angle_opt:.4f}) + {shift_opt:.4f}, "
    f"42 + t·sin({angle_opt:.4f}) + e^({mag_opt:.4f}|t|)·sin(0.3t)·cos({angle_opt:.4f}) )"
)

# --- Save Output to File ---
output_text = f"""
PARAMETRIC CURVE FITTING RESULTS
================================

Optimal Parameters:
-------------------
Angle (θ): {angle_opt:.6f} radians  ≈ {deg_angle:.3f}°
Magnitude (M): {mag_opt:.6f}
Horizontal shift (X): {shift_opt:.6f}

Total L1 Error:
---------------
{L1_error:.6f}

LaTeX Expression:
-----------------
{latex_expr}

Differential Evolution Status:
------------------------------
Success: {opt_result.success}
Message: {opt_result.message}
Iterations: {opt_result.nit}
Function Evaluations: {opt_result.nfev}
"""

with open("results/output.txt", "w", encoding="utf-8") as f:

    f.write(output_text)

print("✔ All results saved to: results/output.txt")

# --- Plotting ---
t_smooth = np.linspace(6, 60, 1000)
x_fit = param_x(t_smooth, angle_opt, mag_opt, shift_opt)
y_fit = param_y(t_smooth, angle_opt, mag_opt, shift_opt)

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, color='crimson', s=10, label='Observed Points')
plt.plot(x_fit, y_fit, color='navy', linewidth=1.8, label='Model Fit')
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.title("Curve Fitting using Parametric Model")
plt.legend()
plt.grid(True)

# Save plot
plot_path = "plots/fitted_curve.png"
plt.savefig(plot_path, dpi=300, bbox_inches='tight')
print(f"✔ Plot saved at: {plot_path}")

plt.show()
