# Unsupervised-Learning-Clustering-Dimensionality-Reduction-
## 📚 Sobre o Projeto

Este projeto aborda técnicas fundamentais de aprendizado não supervisionado, incluindo clusterização (K-Means, Hierarchical Clustering) e redução de dimensionalidade (PCA). O foco é identificar estruturas ocultas nos dados sem o uso de rótulos prévios.

**Objetivo Principal**: Demonstrar como algoritmos não supervisionados podem revelar padrões e agrupamentos naturais em dados não rotulados.

## 🧩 Técnicas Implementadas

### 🔷 Clusterização (Clustering)
- **K-Means**: Agrupamento particional com número pré-definido de clusters
- **Hierarchical Clustering**: Agrupamento hierárquico com dendrogramas
- **DBSCAN**: Detecção de clusters de densidade variável

### 📉 Redução de Dimensionalidade
- **PCA (Principal Component Analysis)**: Redução linear de dimensionalidade
- **Análise de Variância**: Interpretação dos componentes principais
- **Visualização em 2D/3D**: Projeção de dados multidimensionais

## 📊 Dataset

**Fonte**: `sklearn.datasets.load_iris`

**Características**:
- 150 amostras de flores Iris
- 4 features numéricas:
  - Comprimento da sépala
  - Largura da sépala
  - Comprimento da pétala

## 📈 Resultados e Análises
### 1. K-Means Clustering
- Agrupamento eficiente em 3 clusters
- Identificação de padrões naturais nos dados
- Visualização da separação entre espécies

### 2. Hierarchical Clustering
- Dendrograma mostrando estrutura hierárquica
- Identificação do número ideal de clusters
- Comparação com resultados do K-Means

### 3. PCA - Análise de Componentes Principais
- Redução de 4D → 2D preservando ~95% da variância
- Visualização eficiente em duas dimensões
- Identificação dos componentes mais importantes

## 💡 Insights e Aprendizados
### Clusterização
- K-Means: Eficiente para clusters esféricos e bem separados
- Hierarchical Clustering: Ideal quando a estrutura hierárquica é importante
- Escolha do Número de Clusters: Método do cotovelo e dendrogramas são cruciais

### Redução de Dimensionalidade
- PCA: Mantém a variância global mas pode perder estruturas locais
- Interpretabilidade: Componentes principais podem ter significado físico
- Visualização: Ferramenta poderosa para explorar dados multidimensionais

## Aplicações Práticas
- Segmentação de clientes
- Detecção de anomalias
- Pré-processamento para outros algoritmos
- Visualização de dados complexos

### 📊 Visualizações Incluídas
- Gráfico de clusters K-Means
- Dendrograma do clustering hierárquico
- Projeção PCA 2D/3D
- Análise de variância dos componentes
- Comparação entre métodos de clusterização

### 🔧 Metodologia
- **Pré-processamento:** Normalização e escalonamento dos dados
- **Clusterização:** Aplicação de múltiplos algoritmos
- **Avaliação:** Análise qualitativa e quantitativa dos clusters
- **Redução de Dimensionalidade:** PCA e interpretação dos componentes
- **Validação:** Comparação com rótulos verdadeiros (quando disponível)

## 🎓 Conceitos Teóricos Abordados
### Clusterização
- Medidas de similaridade e distância
- Algoritmos particionais vs hierárquicos
- Métodos de validação de clusters
- Escolha do número ótimo de clusters

### Redução de Dimensionalidade
- Álgebra linear aplicada
- Autovalores e autovetores
- Preservação de variância
- Interpretabilidade de componentes


## 📋 Estrutura Detalhada dos Notebooks:
### 01_kmeans_clustering.ipynb
- Análise exploratória do dataset Iris
- Implementação do K-Means
- Método do cotovelo para escolha de K
- Visualização dos clusters

### 02_hierarchical_clustering.ipynb
- endrogramas e interpretação
- Agglomerative Clustering
- Comparação de métodos de linkage
- Determinação do número de clusters

### 03_pca_analysis.ipynb
- Análise de componentes principais
- Variância explicada
- Interpretação dos componentes
- Visualização 2D/3D

### 04_comparative_analysis.ipynb
- Comparação entre técnicas
- Análise de performance
- Casos de uso para cada método
