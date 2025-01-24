import networkx as nx
import json
from utils import save_network

# Load parameters from config.json
with open("config.json") as f:
    config = json.load(f)

num_nodes = config["num_nodes"]
probability = config["edge_probability"]
network_type = config["network_type"]

# Generate network
if network_type == "erdos_renyi":
    G = nx.erdos_renyi_graph(num_nodes, probability)
elif network_type == "barabasi_albert":
    m = config["m_parameter"]
    G = nx.barabasi_albert_graph(num_nodes, m)
else:
    raise ValueError(f"Unsupported network type: {network_type}")

# Save network
save_network(G, "outputs/networks/network.edgelist")
print(f"Generated {network_type} network with {len(G.nodes)} nodes and {len(G.edges)} edges.")