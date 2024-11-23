'''
class HashTable:
    hill climbing
    simulated annealing
    nelder mead
    
main would be random adding values, running hc sa and nm and calculating collisions
nelder mead, hash table, inital a, initial b
'''
import random  # Import random module for generating random integers
import math    # Import math module for mathematical operations
from scipy.optimize import minimize # Import minimize for Nelder-Mead optimization

# Define a HashTable class to handle insertions, hashing, and rehashing
class HashTable:
    def __init__(self, initial_size=10, load_factor_threshold=0.75):
        # Initialize the hash table size and the load factor threshold for rehashing
        self.size = initial_size  # Set initial table size
        self.rehash_count = 0
        self.load_factor = 0
        self.load_factor_threshold = load_factor_threshold  # Set load factor threshold
        self.table = [None] * self.size  # Initialize table with None to store key-value pairs
        self.num_elements = 0  # Initialize the count of elements in the table

    def hash_function(self, x, a, b, m):
        # Calculate hash index using parameters a, b, and modulo m
        return (a * x + b) % m

    def insert(self, key, value, a, b):
        # Inserting key-value pairs
        index = self.hash_function(key, a, b, self.size)
        start_index = index
        # Handling collisions
        while self.table[index] is not None:
            # Update value if the key already exists
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            # Check if table is full when index loops back
            if index == start_index:
                raise Exception("Table is full.")
        # Insert value pair, update count and update load factor
        self.table[index] = (key, value)
        self.num_elements += 1
        self.load_factor = self.num_elements / self.size
        # Rehash parameter
        if self.load_factor > self.load_factor_threshold:
            self.rehash(a, b)
      
    def rehash(self, a, b):
        # Backing up table and resizing new one
        old_table = self.table
        old_size = self.size
        # Double the hash table size and reset element count
        self.size *= 2
        self.table = self.size * [None]
        self.num_elements = 0
        # Reinsert the elements into new table
        for element in old_table:
            if element is not None:
                key, value = element
                self.insert(key, value, a, b)
      
    def calculate_collisions(self, a, b):
        collision_count = 0
        seen_indices = set()
        for item in self.table:
            if item:
                index = self.hash_function(item[0], a, b, self.size)
                if index in seen_indices:
                    collision_count += 1
                seen_indices.add(index)
        
        return collision_count

# Define the hill climbing optimization function for tuning hash parameters
def hill_climbing(hash_table, initial_a, initial_b, iterations=1000):
    a, b = initial_a, initial_b
    best_cost = hash_table.calculate_collisions(a, b)
    
    for _ in range(iterations):
        new_a = a + random.choice([-1, 1])
        new_b = b + random.choice([-1, 1])
        new_cost = hash_table.calculate_collisions(new_a, new_b)
        # Update if better
        if new_cost < best_cost:
            a, b = new_a, new_b
            best_cost = new_cost
            
    return a, b, best_cost
    
# Define simulated annealing optimization function for tuning hash parameters
def simulated_annealing(hash_table, initial_a, initial_b, initial_temperature=1000, cooling_rate=0.003):
    a, b = initial_a, initial_b
    best_cost = hash_table.calculate_collisions(a, b)
    temperature = initial_temperature
    
    while temperature > 1:
        new_a = max(1, a + random.choice([-1, 1]))
        new_b = max(1, b + random.choice([-1, 1]))
        
        new_cost = hash_table.calculate_collisions(new_a, new_b)
        
        if new_cost < best_cost or math.exp((best_cost - new_cost) / temperature) > random.random():
            a, b = new_a, new_b
            best_cost = new_cost
            
        temperature *= 1 - cooling_rate
    
    return a, b, best_cost
        
# Define Nelder-Mead optimization function using Scipy for tuning hash parameters
def nelder_mead(hash_table, initial_a, initial_b):
    def objective(params):
        a, b = int(params[0]), int(params[1])
        return hash_table.calculate_collisions(int(a), int(b))
    
    initial_guess = [initial_a, initial_b]
    result = minimize(objective, initial_guess, method='Nelder-Mead')
    best_a, best_b = map(int, result.x)
    best_cost = hash_table.calculate_collisions(best_a, best_b)
    
    return best_a, best_b, best_cost


# Main block to test each optimization method on the hash table
if __name__ == "__main__":
    # Create an instance of HashTable with initial size of 20 and a threshold load factor
    hash_table = HashTable(initial_size=20)

    # Insert random keys into the hash table for testing
    for i in range(50):
        hash_table.insert(random.randint(0, 1000), i, a=1, b=1)  # Insert with default parameters

    # Initial parameters for hash function
    initial_a = 1
    initial_b = 1

    # Run Hill Climbing optimization and print results
    hc_a, hc_b, hc_collisions = hill_climbing(hash_table, initial_a, initial_b)
    print(f"Hill Climbing: a={hc_a}, b={hc_b}, collisions={hc_collisions}")

    # Run Simulated Annealing optimization and print results
    sa_a, sa_b, sa_collisions = simulated_annealing(hash_table, initial_a, initial_b)
    print(f"Simulated Annealing: a={sa_a}, b={sa_b}, collisions={sa_collisions}")

    # Run Nelder-Mead optimization and print results
    nm_a, nm_b, nm_collisions = nelder_mead(hash_table, initial_a, initial_b)
    print(f"Nelder-Mead: a={nm_a}, b={nm_b}, collisions={nm_collisions}")