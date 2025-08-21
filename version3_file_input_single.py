def quadratic_temperature(a, b, c, t):
    return a*(t**2) + b*t + c

try:
    with open("input.txt", "r") as f:
        values = f.read().split()

    if len(values) != 4:
        print("❌ Error: input.txt must contain exactly 4 numbers (a b c t)")
    else:
        a, b, c, t = map(float, values)
        temp = quadratic_temperature(a, b, c, t)
        print(f"T({t}) = {temp}")

except FileNotFoundError:
    print("❌ input.txt not found. Please place it in the same folder.")
