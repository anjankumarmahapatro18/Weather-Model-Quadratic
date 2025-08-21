
# Predict temperature using hardcoded coefficients and time
# T(t) = a*t^2 + b*t + c

def predict(a, b, c, t):
    return a * (t ** 2) + b * t + c

if __name__ == "__main__":
    a = 0.5
    b = -3.0
    c = 28.0
    t = 5  # e.g., 5th hour or day
    T = predict(a, b, c, t)
    print(f"Predicted temperature at t={t}: {T:.2f}°C")
