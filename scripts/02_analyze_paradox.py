import pandas as pd
import networkx as nx
from utils import load_network

# Load network
G = load_network("outputs/networks/network.edgelist")

results = []
for node in G.nodes:
    degree = G.degree[node]
    neighbor_degrees = [G.degree[neighbor] for neighbor in G.neighbors(node)]
    avg_neighbor_degree = sum(neighbor_degrees) / len(neighbor_degrees) if neighbor_degrees else 0

    # Record whether the paradox holds
    paradox_holds = avg_neighbor_degree > degree
    results.append({"node": node, "degree": degree, "avg_neighbor_degree": avg_neighbor_degree, "paradox_holds": paradox_holds})

# Save results
df = pd.DataFrame(results)
df.to_csv("outputs/analysis_results.csv", index=False)
print("Analysis complete. Results saved to outputs/analysis_results.csv.")