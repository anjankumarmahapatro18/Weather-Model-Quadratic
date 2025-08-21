
# Demonstrate the same quadratic model through Waterfall, Iterative and Agile "modes"
# Coefficients for quadratic model
a = -0.2
b = 1.5
c = 24.0

def quadratic_weather_model(time):
    return a * (time ** 2) + b * time + c

if __name__ == "__main__":
    # ===== WATERFALL MODE =====
    print("=== WATERFALL MODE ===")
    for hour in range(0, 25, 6):  # every 6 hours
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

    # ===== ITERATIVE MODE =====
    print("\n=== ITERATIVE MODE ===")
    for iteration in range(1, 4):
        print(f"Iteration {iteration}:")
        for hour in range(0, 25, 12):  # every 12 hours
            temp = quadratic_weather_model(hour)
            print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
        print("---")

    # ===== AGILE MODE =====
    print("\n=== AGILE MODE ===")
    times_to_check = [0, 6, 12, 18, 24]
    for sprint in range(1, 3):
        print(f"Sprint {sprint}:")
        for t in times_to_check:
            temp = quadratic_weather_model(t)
            print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
        print("---")
