# statistical-simulation-friendship-paradox

## Project Overview
This project explores the **Friendship Paradox**, which states that in a social network, your friends are likely to have more friends than you, on average. This paradox arises due to the way degrees (number of connections) are distributed in networks: nodes with high degrees (highly connected individuals) are overrepresented in their neighbors' degree averages.

### Mathematical Explanation
The Friendship Paradox can be explained using basic properties of graph theory and statistics. In a network, nodes represent individuals, and edges represent connections (friendships). The degree of a node is the number of edges connected to it, i.e., the number of friends that individual has.

#### Key Concepts:
1. **Node Degree ($d_i$):** The degree of a node $i$, denoted as $d_i$, is the number of direct connections (friends) that node has in the network.

2. **Average Neighbor Degree (AND):** For a given node $i$, the average degree of its neighbors is calculated as:
   
   $$\text{AND}(i) = \frac{1}{d_i} \sum_{j \in N(i)} d_j$$

   Here, $N(i)$ represents the set of neighbors of node $i$, and $d_j$ is the degree of a neighbor $j$. This formula essentially takes the average of the degrees of all nodes connected to $i$.

3. **Global Average Degree:** Across the entire network, the average degree can be computed as:
   
   $$\text{Average Degree} = \frac{2E}{N}$$

   where $E$ is the number of edges in the network and $N$ is the number of nodes.

#### Deriving the Paradox:
The Friendship Paradox arises when:
   
   $$\text{AND}(i) > d_i$$
   
   This inequality suggests that the mean degree of a node's neighbors exceeds the degree of the node itself. This phenomenon can be attributed to the fact that nodes with higher degrees are more likely to appear in their neighbors' networks, skewing the average.

#### Statistical Basis:
In statistical terms, the paradox is a result of sampling bias. A high-degree node (one with many friends) appears in many neighborhoods, contributing disproportionately to the calculation of average neighbor degrees. Mathematically, the probability that a node is sampled as a neighbor is proportional to its degree, creating a bias toward high-degree nodes.

#### Example Calculation:
Consider a small network where:
- Node A has 2 friends (Node B and Node C).
- Node B has 4 friends (Node A, Node C, Node D, Node E).
- Node C has 3 friends (Node A, Node B, Node F).

For Node A:
- Degree: $d_A = 2$
- Neighbors: Node B ($d_B = 4$), Node C ($d_C = 3$)
- $$\text{AND}(A) = \frac{d_B + d_C}{2} = \frac{4 + 3}{2} = 3.5$$

Here, Node A's AND (3.5) is greater than its own degree (2), illustrating the Friendship Paradox.

#### General Observations:
- The paradox is more pronounced in networks with skewed degree distributions, such as scale-free networks (e.g., Barabási-Albert model).
- In uniformly distributed random graphs (e.g., Erdős-Rényi), the paradox still exists but is less significant.

### Goals
The simulation uses random graph models to:
- Generate synthetic networks (e.g., Erdős-Rényi, Barabási-Albert).
- Analyze the paradox by calculating each node's degree and the average degree of its neighbors.
- Visualize results to understand the prevalence of the paradox across different network types.

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_generate_network.py       # Generate random networks
│   ├── 02_analyze_paradox.py        # Analyze the friendship paradox
│   ├── 03_visualize_results.py      # Create visualizations
│   └── utils.py                     # Utility functions
├── outputs/
│   ├── networks/                    # Store generated network data
│   ├── analysis_results.csv         # Analysis results
│   └── visualizations/              # Visualizations of results
├── config.json                      # Configuration file for simulation parameters
├── requirements.txt                 # Required Python libraries
└── README.md                        # Project documentation
```

## Usage

### 1. Setup the Project:
1. Clone the repository.
2. Ensure you have Python installed.
3. Install required dependencies using the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Generate a Network:
Run the network generation script to create a synthetic network.
```bash
python scripts/01_generate_network.py
```
This will generate a network file in `outputs/networks/`.

### 3. Analyze the Friendship Paradox:
Run the analysis script to calculate the friendship paradox metrics.
```bash
python scripts/02_analyze_paradox.py
```
This will produce `outputs/analysis_results.csv` with results for each node.

### 4. Visualize the Results:
Generate visualizations to understand the results.
```bash
python scripts/03_visualize_results.py
```
Plots will be saved in `outputs/visualizations/`.

## Requirements
The project requires the following Python libraries:
- networkx
- pandas
- matplotlib

Install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```