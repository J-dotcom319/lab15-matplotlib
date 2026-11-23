"""
Program Name: Lab15_jeffr-2.py
Author: Jeffrey Antwi
Purpose: Plot the cubes of the first 5 values (hard-coded) and the first
         5000 values (generated), saving each to its own PNG file, produced
         in accordance with "Try It Yourself 15-1" in Python Crash Course.
Starter Code: No starter code. Approach follows Python Crash Course (3rd ed.),
              Ch. 15, pp. 321-324.
Date: 11/23/2026
"""

import matplotlib.pyplot as plt


def plot_cubes(values, cubes, title, filename):
    """Plot cubes against their values and save the figure to a PNG file."""
    fig, ax = plt.subplots()
    ax.plot(values, cubes, linewidth=3)
    ax.set_title(title, fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cube of Value", fontsize=14)
    ax.tick_params(axis="both", labelsize=12)
    fig.savefig(filename, bbox_inches="tight")
    plt.close(fig)


def plot_subplots():
    """Show both plots side by side in one figure."""
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    axs[0].plot([1, 2, 3, 4, 5], [1, 8, 27, 64, 125], linewidth=3)
    axs[0].set_title("First 5 Cubes", fontsize=18)
    axs[0].set_xlabel("Value")
    axs[0].set_ylabel("Cube of Value")

    x_values = list(range(1, 5001))
    axs[1].plot(x_values, [x ** 3 for x in x_values], linewidth=3)
    axs[1].set_title("First 5000 Cubes", fontsize=18)
    axs[1].set_xlabel("Value")
    axs[1].set_ylabel("Cube of Value")

    fig.tight_layout()
    fig.savefig("cubes_subplots.png", bbox_inches="tight")
    plt.close(fig)


def main():
    """Run both parts of the exercise."""
    # Part 1: the first 5 cubes, hand-coded.
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 8, 27, 64, 125]
    plot_cubes(x_values, y_values, "First 5 Cubes", "cubes_5.png")

    # Part 2: the first 5000 cubes, generated.
    x_values = list(range(1, 5001))
    y_values = [x ** 3 for x in x_values]
    plot_cubes(x_values, y_values, "First 5000 Cubes", "cubes_5000.png")

    plot_subplots()


if __name__ == "__main__":
    main()