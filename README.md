# 🔍 Unsupervised Learning - Clustering Dimensionality Reduction 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2%2B-orange)](https://scikit-learn.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)

Um projeto feito no curso "Fundamentos de IA: investigando algoritmos e abordagens de machine learning" na Alura conciso de aprendizado não supervisionado demonstrando técnicas fundamentais de clusterização e redução de dimensionalidade usando o dataset Iris, focando na aplicação prática de:

- **K-Means Clustering**: Agrupamento particional
- **Hierarchical Clustering**: Agrupamento hierárquico com dendrogramas  
- **PCA (Principal Component Analysis)**: Redução de dimensionalidade

**Destaque**: Todas as técnicas são aplicadas no dataset Iris, permitindo comparação direta entre diferentes abordagens.


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


## 📈 Resultados e Visualizações
O notebook gera uma análise visual comparativa incluindo:
- **Dendrograma:** Estrutura hierárquica dos dados
- **Comparação de Clusters:** K-Means vs Hierarchical vs Dados reais
- **Projeção PCA:** Dados originais em 2 dimensões
- **Análise de Variância:** Eficiência da redução dimensional


## 💡 Principais Insights
### Clusterização
- **K-Means:** Eficiente e rápido para clusters bem definidos
- **Hierarchical:** Revela estrutura natural através do dendrograma
- **Resultados:** Ambas as técnicas identificam padrões similares aos rótulos verdadeiros

## PCA
- **Eficácia:** 2 componentes preservam a maioria da informação
- **Visualização:** Possibilidade de analisar dados 4D em 2D
- **Aplicação:** Pré-processamento para outros algoritmos


### 🎯 Aplicações Práticas
- Segmentação de clientes sem rótulos prévios
- Exploração de dados para identificar grupos naturais
- Pré-processamento para reduzir dimensionalidade
- Análise exploratória de datasets complexos
