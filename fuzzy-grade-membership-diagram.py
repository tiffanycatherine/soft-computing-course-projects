
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz


def trapezoidal_membership(x, a, b, c, d):
    return np.maximum(0, np.minimum(
        (x - a) / (b - a) if b > a else 1.0,  # Rising edge
        np.minimum(
            1.0,  # Plateau~
            (d - x) / (d - c) if d > c else 1.0  # Falling edge
        )
    ))


def create_fuzzy_diagram():    
    # Define score range
    scores = np.linspace(0, 100, 1000)
    
    # Define trapezoidal parameters for each grade
    grade_c_params = (50, 50, 60, 66)
    
    grade_b_params = (60, 66, 75, 86)
    
    grade_a_params = (75, 86, 100, 100)
    
    # Calculate membership values using scikit-fuzzy
    membership_c = fuzz.trapmf(scores, grade_c_params)
    membership_b = fuzz.trapmf(scores, grade_b_params)
    membership_a = fuzz.trapmf(scores, grade_a_params)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot membership functions
    ax.plot(scores, membership_c, 'b-', linewidth=2.5, label='Grade C (50-60)')
    ax.plot(scores, membership_b, 'g-', linewidth=2.5, label='Grade B (66-75)')
    ax.plot(scores, membership_a, 'r-', linewidth=2.5, label='Grade A (86-100)')
    
    # Fill the areas under the curves for better visualization
    ax.fill_between(scores, membership_c, alpha=0.2, color='blue')
    ax.fill_between(scores, membership_b, alpha=0.2, color='green')
    ax.fill_between(scores, membership_a, alpha=0.2, color='red')
    
    # Customize the plot
    ax.set_xlabel('Score', fontsize=12, fontweight='bold')
    ax.set_ylabel('Membership Degree', fontsize=12, fontweight='bold')
    ax.set_title('Fuzzy Grade Membership Diagram', fontsize=14, fontweight='bold')
    
    # Set axis limits and labels
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.1)
    ax.set_xticks(np.arange(0, 101, 5))
    ax.set_yticks(np.arange(0, 1.1, 0.25))
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Add legend
    ax.legend(loc='upper left', fontsize=11, framealpha=0.95)
    
    # Add annotations for grade boundaries
    ax.axvline(x=50, color='blue', linestyle=':', alpha=0.5)
    ax.axvline(x=66, color='green', linestyle=':', alpha=0.5)
    ax.axvline(x=86, color='red', linestyle=':', alpha=0.5)
    
    # Tight layout for better spacing
    plt.tight_layout()
    
    # Display the plot
    plt.show()


if __name__ == "__main__":
    # Create and display the fuzzy membership diagram
    create_fuzzy_diagram()