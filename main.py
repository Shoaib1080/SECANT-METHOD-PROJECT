import matplotlib.pyplot as plt
import numpy as np

def secantmethod(func_str, x0, x1, n):
    def f(x):
        return eval(func_str, {"x": x, "pow": pow, "sin": __import__('math').sin, "cos": __import__('math').cos, "exp": __import__('math').exp})

    x_points = []
    y_points = []

    print(f"{'Iteration':>9} | {'x0':>10} | {'x1':>10} | {'xi (new)':>12}")
    print("-" * 46)

    for intercept in range(1, n + 1):
        fx0 = f(x0)
        fx1 = f(x1)

        if (fx0 - fx1) == 0:
            print(f"Zero division error at iteration {intercept}. Stopping early.")
            break

        xi = x0 - (fx0 * (x0 - x1)) / (fx0 - fx1)

        print(f"{intercept:9} | {x0:10.6f} | {x1:10.6f} | {xi:12.6f}")

        # Store points for plotting
        x_points.append(x1)
        y_points.append(f(x1))

        x0 = x1
        x1 = xi

    print(f"\nThe root was found to be approximately {xi} after {intercept} iterations!")

    # Plotting
    x_range = np.linspace(min(x_points)-1, max(x_points)+1, 400)
    y_range = [eval(func_str, {"x": x, "pow": pow, "sin": __import__('math').sin, "cos": __import__('math').cos, "exp": __import__('math').exp}) for x in x_range]

    plt.figure(figsize=(10,6))
    plt.plot(x_range, y_range, label=f'f(x) = {func_str}')
    plt.axhline(0, color='gray', linestyle='--')

    plt.scatter(x_points, y_points, color='red', label='Iteration Points')
    plt.plot(x_points, y_points, linestyle='--', color='green', label='Secant Lines')

    plt.title('Secant Method Iterations')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
secantmethod("sin(x) - x/2", 1, 3, 7)
