import random
import matplotlib.pyplot as plt
def generate_random_knapsack(num_items=10, max_weight=10, max_value=20, capacity=50):
    items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(num_items)]
    return items, capacity

def calculate_fitness(candidate, items, capacity):
    total_weight = 0
    total_value = 0
    for bit, (w, v) in zip(candidate, items):
        if bit == 1:
            total_weight += w
            total_value += v
    return total_value if total_weight <= capacity else 0

def monte_carlo_search(items, capacity, iterations=1000, seed=42):
    """
    Monte Carlo Search algorithm for the knapsack problem.
    Randomly generates solutions, keeping track of the best one.
    """
    random.seed(seed)
    best_candidate = None
    best_fitness = 0
    fitness_history = []

    for _ in range(iterations):
        candidate = [random.randint(0, 1) for _ in range(len(items))]
        fitness = calculate_fitness(candidate, items, capacity)
        if fitness > best_fitness:
            best_fitness = fitness
            best_candidate = candidate
        fitness_history.append(best_fitness)

    return best_candidate, best_fitness, fitness_history

def hill_climbing_search(items, capacity, iterations=1000, seed=42):
    random.seed(seed)
    current_candidate = [random.randint(0, 1) for _ in range(len(items))]
    current_fitness = calculate_fitness(current_candidate, items, capacity)
    best_candidate = current_candidate[:]
    best_fitness = current_fitness
    fitness_history = []

    for _ in range(iterations):
        # Flip one bit at random
        neighbor = current_candidate[:]
        flip_index = random.randint(0, len(items) - 1)
        neighbor[flip_index] = 1 - neighbor[flip_index]
        neighbor_fitness = calculate_fitness(neighbor, items, capacity)

        # If better, adopt neighbor
        if neighbor_fitness > current_fitness:
            current_candidate = neighbor
            current_fitness = neighbor_fitness

        # Track the best overall solution
        if current_fitness > best_fitness:
            best_candidate = current_candidate[:]
            best_fitness = current_fitness

        fitness_history.append(best_fitness)

    return best_candidate, best_fitness, fitness_history

def main():
    # Adjustable parameters
    num_items = 20
    capacity = 150
    iterations = 500

    items, capacity = generate_random_knapsack(num_items=num_items, max_weight=15, max_value=30, capacity=capacity)

    # Monte Carlo Optimization
    mc_candidate, mc_value, mc_history = monte_carlo_search(items, capacity, iterations=iterations)
    print(f"Monte Carlo best value: {mc_value}")

    # Hill Climbing Optimization
    hc_candidate, hc_value, hc_history = hill_climbing_search(items, capacity, iterations=iterations)
    print(f"Hill Climbing best value: {hc_value}")

    # Plot the results
    plt.plot(mc_history, label="Monte Carlo")
    plt.plot(hc_history, label="Hill Climbing")
    plt.xlabel("Iteration")
    plt.ylabel("Best Value So Far")
    plt.title("Knapsack Optimization Comparison")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()