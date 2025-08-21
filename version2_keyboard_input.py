
# Predict temperature using keyboard-provided coefficients and time

def predict(a, b, c, t):
    return a * (t ** 2) + b * t + c

if __name__ == "__main__":
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    t = float(input("Enter time t (hour/day): "))
    T = predict(a, b, c, t)
    print(f"Predicted temperature at t={t}: {T:.2f}°C")
