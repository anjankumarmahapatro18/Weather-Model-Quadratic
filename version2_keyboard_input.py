import matplotlib.pyplot as plt
import numpy as np

# Quadratic function
def quadratic_temperature(a, b, c, t):
    return a*(t**2) + b*t + c

# Days range (0 to 30)
days = np.linspace(0, 30, 31)

# --- 1) Basic Weather Model ---
a, b, c = -0.2, 1.5, 24
temps = quadratic_temperature(a, b, c, days)

plt.figure(figsize=(6,4))
plt.plot(days, temps, "bo-", label=f"T = {a}t² + {b}t + {c}")
plt.title("Weather Modeling (Quadratic Model)")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()


# --- 2) Iterative Model (fewer, bigger changes) ---
plt.figure(figsize=(6,4))
for i, (a, b, c) in enumerate([(-0.2, 1.5, 24),
                               (-0.25, 1.4, 26),
                               (-0.3, 1.6, 25)], start=1):
    temps = quadratic_temperature(a, b, c, days)
    plt.plot(days, temps, label=f"Iteration {i}")
plt.title("Iterative Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()


# --- 3) Agile Model (smaller, frequent updates) ---
plt.figure(figsize=(6,4))
for i, (a, b, c) in enumerate([(-0.2, 1.5, 24),
                               (-0.22, 1.52, 24.5),
                               (-0.23, 1.55, 25),
                               (-0.24, 1.57, 25.2)], start=1):
    temps = quadratic_temperature(a, b, c, days)
    plt.plot(days, temps, label=f"Sprint {i}")
plt.title("Agile Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
