import pandas as pd
import matplotlib.pyplot as plt

# Load analysis results
df = pd.read_csv("outputs/analysis_results.csv")

# Histogram of node degrees
plt.figure()
plt.hist(df["degree"], bins=20, alpha=0.7, label="Node Degree")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Histogram of Node Degrees")
plt.savefig("outputs/visualizations/degree_histogram.png")

# Scatter plot of degree vs. average neighbor degree
plt.figure()
plt.scatter(df["degree"], df["avg_neighbor_degree"], alpha=0.6)
plt.xlabel("Node Degree")
plt.ylabel("Average Neighbor Degree")
plt.title("Node Degree vs. Average Neighbor Degree")
plt.savefig("outputs/visualizations/degree_vs_avg_neighbor.png")

# Bar chart of paradox prevalence
paradox_percentage = df["paradox_holds"].mean() * 100
plt.figure()
plt.bar(["Paradox Holds", "Paradox Does Not Hold"], [paradox_percentage, 100 - paradox_percentage])
plt.ylabel("Percentage")
plt.title("Friendship Paradox Prevalence")
plt.savefig("outputs/visualizations/paradox_prevalence.png")

print("Visualizations saved to outputs/visualizations/")