import networkx as nx

def save_network(graph, path):
    nx.write_edgelist(graph, path, data=False)

def load_network(path):
    return nx.read_edgelist(path, nodetype=int)