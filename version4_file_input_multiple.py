
# Predict temperatures reading multiple sets (a, b, c, t) from inputs_multiple.txt

def predict(a, b, c, t):
    return a * (t ** 2) + b * t + c

if __name__ == "__main__":
    with open("inputs_multiple.txt", "r") as f:
        for line in f:
            if not line.strip():
                continue
            a, b, c, t = map(float, line.split())
            T = predict(a, b, c, t)
            print(f"a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")
