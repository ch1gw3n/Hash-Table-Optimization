# Hash-Table-Optimization

## Overview
This object utilizes a hash table with dynamic resizing and parameter optimization techniques to minimize collisions and reduce the number of rehashes. The hash function parameters are optimized using 3 techniques: Hill Climbing, Simulated Annealing, and Nelder-Mead. 

## Hash Function
The hash function used:
    $h(x) = (a*x + b) % m$

Where:
    *a* and *b* are adjustable parameters
    *x* is the key to be hashed
    *m* is the table size

## Requirements
This uses the Python modules and library:
- `math`: For mathematical operations
- `random`: For generating random integers
- `scipy`: Uses NumPy to assist with Nelder-Mead Optimization method in this program

## Comparison of Optimization Results
Running the program wih the main function below:
```python
if __name__ == "__main__":
    # Create an instance of HashTable with initial size of 20 and a threshold load factor
    hash_table = HashTable(initial_size=20)

    # Insert random keys into the hash table for testing
    for i in range(50):
        hash_table.insert(random.randint(0, 1000), i, a=1, b=1)  # Insert with default parameters

    # Initial parameters for hash function
    initial_a = 1
    initial_b = 1
```
will result in:
| Metric         | Hill Climbing | Simulated Annealing | Nelder-Mead |
|:---------------|--------------:|:-------------------:|------------:|
| **a**          | 1             | 21                  | 1           |
| **b**          | 1             | 40                  | 1           |
| **Collisions** | 13            | 13                  | 13          |

**Hill Climbing:**
- Greedy algorithm, always accepts the best local move.
- Easily stuck in local minima.
- For quick and simple approximations, this is sufficient.
  
**Simulated Annealing:**
- Probabilistic approach, can escape local minima by accepting worse moves sometimes.
- Temperature reduces randomness over time to focus on local refinement.
- If the landscape is more complex, this will result in better solutions.

**Nelder-Mead:**
- Geometric, works with multiple points at once to reshape simplex to converge on the best solution.
- Particularly useful for optimizing functions with more than one variable.
- The most precise optimization, this is often the best choice, but will require a higher runtime.

## Contact Information
**Author:** Chi Nguyen

**Email:** nguyenct1@g.cofc.edu
