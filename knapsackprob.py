import random
import matplotlib.pyplot as plt
from collections import deque

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

########################################## Monte Carlo Search ##########################################
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
#########################################################################################################


############################################ Hill Climbing Search #######################################

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


#########################################################################################################

################################## Hill Climbing Search with Learning ###################################

def hill_climbing_search_with_learning(items, capacity, iterations=1000, seed=42):
    random.seed(seed)
    n = len(items)

    # Start with a random candidate
    current_candidate = [random.randint(0, 1) for _ in range(n)]
    current_fitness = calculate_fitness(current_candidate, items, capacity)

    best_candidate = current_candidate[:]
    best_fitness = current_fitness

    history = []

    for _ in range(iterations):
        neighbor = current_candidate[:]
        flip_index = random.randint(0, n - 1)
        neighbor[flip_index] = 1 - neighbor[flip_index]

        neighbor_fitness = calculate_fitness(neighbor, items, capacity)

        # Learn by adopting neighbor if better
        if neighbor_fitness > current_fitness:
            current_candidate = neighbor
            current_fitness = neighbor_fitness

        if current_fitness > best_fitness:
            best_candidate = current_candidate[:]
            best_fitness = current_fitness

        # Record fitness at each iteration
        history.append(best_fitness)

    return best_candidate, best_fitness, history
#########################################################################################################

############################################# Tabu Search ###############################################

def tabu_search_knapsack(items, capacity, iterations=1000, tabu_size=30, seed=42):
    n = len(items)
    random.seed(seed)

    # Initialize a random solution
    current = [0] * n
    current_weight = 0
    order = list(range(n))
    random.shuffle(order)
    for i in order:
        w, v = items[i]
        if current_weight + w <= capacity:
            current[i] = 1
            current_weight += w

    current_value = calculate_fitness(current, items, capacity)
    best = current.copy()
    best_value = current_value

    tabu_list = deque(maxlen=tabu_size)
    history = [best_value]

    for _ in range(iterations):
        candidate_moves = []
        for i in range(n):
            neighbor = current.copy()
            neighbor[i] = 1 - neighbor[i]
            neighbor_value = calculate_fitness(neighbor, items, capacity)

            # Skip invalid or tabu-worsening moves
            if neighbor_value == 0:
                continue
            if i in tabu_list and neighbor_value <= best_value:
                continue

            candidate_moves.append((neighbor, i, neighbor_value))

        if candidate_moves:
            neighbor, move_idx, neighbor_value = max(candidate_moves, key=lambda x: x[2])
            current = neighbor
            current_value = neighbor_value
            tabu_list.append(move_idx)

            if current_value > best_value:
                best = current.copy()
                best_value = current_value

        # Record best fitness so far on each iteration
        history.append(best_value)

    # Calculate final weight of best solution
    best_weight = sum([w for bit, (w, _) in zip(best, items) if bit == 1])

    return best, best_value, best_weight, history

#########################################################################################################

def main():
    # Adjustable parameters
    num_items = 20
    capacity = 150
    iterations = 1000
    seed = 42

    items, capacity = generate_random_knapsack(num_items=num_items, max_weight=15, max_value=30, capacity=capacity)

    print("Capacity: ", capacity)
    # Monte Carlo Optimization
    mc_candidate, mc_value, mc_history = monte_carlo_search(items, capacity, iterations=iterations, seed=seed)
    print(f"Monte Carlo best value: {mc_value}")
    print("Monte Carlo best candidate: ", mc_candidate)

    # Hill Climbing Optimization
    hc_candidate, hc_value, hc_history = hill_climbing_search(items, capacity, iterations=iterations, seed=seed)
    print(f"Hill Climbing best value: {hc_value}")
    print("Hill Climbing best candidate: ", hc_candidate)

    ics_candidate, ics_value, ics_history = hill_climbing_search_with_learning(items, capacity, iterations=iterations, seed=seed)
    print(f"Hill Climbing with Learning best value: {ics_value}")
    print("Hill Climbing with Learning best candidate: ", ics_candidate)

    # Tabu Search Optimization
    tb_candidate, tb_value, tb_weight, tb_history = tabu_search_knapsack(items, capacity, iterations=iterations, seed=seed)
    print(f"Tabu Search best value: {tb_value}")
    print("Tabu Search best candidate: ", tb_candidate)

    # Plot the results
    plt.plot(mc_history, label="Monte Carlo")
    plt.plot(hc_history, label="Hill Climbing")
    plt.plot(ics_history, label="Hill Climbing with Learning")
    plt.plot(tb_history, label="Tabu Search")
    plt.xlabel("Iteration")
    plt.ylabel("Best Value So Far")
    plt.title("Knapsack Optimization Comparison")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
