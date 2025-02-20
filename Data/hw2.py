import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data_file = "leaf_measurements.csv"
df = pd.read_csv(data_file)

# Set the style for the plots
sns.set_style("whitegrid")

# 1. Histograms of Leaf Length
plt.figure(figsize=(14, 10))

# Histogram for all plants (length)
plt.subplot(2, 2, 1)
plt.hist(df['Leaf Length (cm)'], bins=10, alpha=0.7, color='blue')
plt.title("Histogram of Leaf Length for All Plants", fontsize=14)
plt.xlabel("Leaf Length (cm)", fontsize=12)
plt.ylabel("Count", fontsize=12)

# Histograms for each plant (length)
plants = df['Plant Name'].unique()
for i, plant in enumerate(plants, start=2):
    plt.subplot(2, 2, i)
    subset = df[df['Plant Name'] == plant]
    plt.hist(subset['Leaf Length (cm)'], bins=10, alpha=0.7, color='green')
    plt.title(f"Histogram of Leaf Length for {plant}", fontsize=14)
    plt.xlabel("Leaf Length (cm)", fontsize=12)
    plt.ylabel("Count", fontsize=12)

plt.tight_layout()
plt.show()

# 2. Histograms of Leaf Width
plt.figure(figsize=(14, 10))

# Histogram for all plants (width)
plt.subplot(2, 2, 1)
plt.hist(df['Leaf Width (cm)'], bins=10, alpha=0.7, color='orange')
plt.title("Histogram of Leaf Width for All Plants", fontsize=14)
plt.xlabel("Leaf Width (cm)", fontsize=12)
plt.ylabel("Count", fontsize=12)

# Histograms for each plant (width)
for i, plant in enumerate(plants, start=2):
    plt.subplot(2, 2, i)
    subset = df[df['Plant Name'] == plant]
    plt.hist(subset['Leaf Width (cm)'], bins=10, alpha=0.7, color='purple')
    plt.title(f"Histogram of Leaf Width for {plant}", fontsize=14)
    plt.xlabel("Leaf Width (cm)", fontsize=12)
    plt.ylabel("Count", fontsize=12)

plt.tight_layout()
plt.show()

# 3. Boxplots of Leaf Width and Length by Plant Type
plt.figure(figsize=(12, 6))
sns.boxplot(x="Plant Name", y="Leaf Length (cm)", data=df, palette="Set2")
plt.title("Boxplot of Leaf Length by Plant Type", fontsize=14)
plt.xlabel("Plant Type", fontsize=12)
plt.ylabel("Leaf Length (cm)", fontsize=12)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x="Plant Name", y="Leaf Width (cm)", data=df, palette="Set2")
plt.title("Boxplot of Leaf Width by Plant Type", fontsize=14)
plt.xlabel("Plant Type", fontsize=12)
plt.ylabel("Leaf Width (cm)", fontsize=12)
plt.show()

# 4. Scatter Plot of Data with Each Subset in Different Colors
plt.figure(figsize=(12, 6))
colors = {"Eastern Hemlock (Tsuga canadensis)": "blue",
          "Northern White Cedar (Thuja occidentalis)": "green",
          "Inkberry Holly (Ilex glabra)": "red"}

for plant, color in colors.items():
    subset = df[df['Plant Name'] == plant]
    plt.scatter(subset['Leaf Width (cm)'], subset['Leaf Length (cm)'], color=color, label=plant, alpha=0.7)

plt.title("Scatter Plot of Leaf Width vs. Length by Plant Type", fontsize=14)
plt.xlabel("Leaf Width (cm)", fontsize=12)
plt.ylabel("Leaf Length (cm)", fontsize=12)
plt.legend(fontsize=10, title="Plant Type")
plt.show()

data_combined = df.copy()
data_combined["Plant Name"] = "All Plants"

# Combine original data with the new "All Plants" categorys
data_with_combined = pd.concat([df, data_combined], ignore_index=True)

# Create boxplots for leaf width and length with the "All Plants" category
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.boxplot(ax=axes[0], x="Plant Name", y="Leaf Width (cm)", data=data_with_combined)
axes[0].set_title("Boxplot of Leaf Width by Plant Type (Including All Plants)")
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45, ha="right")

sns.boxplot(ax=axes[1], x="Plant Name", y="Leaf Length (cm)", data=data_with_combined)
axes[1].set_title("Boxplot of Leaf Length by Plant Type (Including All Plants)")
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha="right")

plt.tight_layout()
plt.show()