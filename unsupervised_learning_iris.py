import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. Carregar e explorar dados
iris = load_iris()
X, y = iris.data, iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
print("Dataset shape:", X.shape)

# 2. K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# 3. Hierarchical Clustering 
plt.figure(figsize=(10, 5))
Z = linkage(X, method='ward')
dendrogram(Z)
plt.title('Dendrograma - Hierarchical Clustering')
plt.show()

hierarchical = AgglomerativeClustering(n_clusters=3)
hierarchical_labels = hierarchical.fit_predict(X)

# 4. PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(f"Variância explicada: {pca.explained_variance_ratio_.sum():.2%}")

# 5. Visualização comparativa
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Dados originais
axes[0,0].scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
axes[0,0].set_title('Dados Originais (Rótulos Verdadeiros)')

# K-Means
axes[0,1].scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='Set1')
axes[0,1].set_title('K-Means Clustering')

# Hierarchical
axes[1,0].scatter(X[:, 0], X[:, 1], c=hierarchical_labels, cmap='Set2')  
axes[1,0].set_title('Hierarchical Clustering')

# PCA
axes[1,1].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
axes[1,1].set_title('PCA - Projeção 2D')

plt.tight_layout()
plt.show()

print("✅ Análise completa: Clustering + PCA realizados com sucesso!")