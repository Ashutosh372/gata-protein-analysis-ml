# GATA Protein Analysis Using Machine Learning

This is my personal project where I analyze GATA transcription factors in *Capsicum annuum* (chili pepper) using machine learning techniques.  
The aim is to cluster the proteins, identify patterns, visualize feature relationships, and understand how different GATA proteins behave based on computational analysis.

---

## Project Overview

- Extracted biological and structural features from protein sequences.
- Performed dimensionality reduction using PCA and t-SNE.
- Applied unsupervised learning models:
  - DBSCAN
  - K-Means
  - Hierarchical Clustering
- Compared clustering models and evaluated them using silhouette score.
- Achieved a DBSCAN silhouette score of approximately **0.88**.
- Visualized clusters, feature correlations, and relationships between proteins.
- Developed optional Streamlit visualization for interactive exploration.

---

## Installation

Install all required Python libraries using:

pip install numpy pandas scikit-learn matplotlib seaborn biopython streamlit plotly

---

## How to Run

1. Open the project notebook:
gata_analysis.ipynb

2. (Optional) Run the Streamlit app:
streamlit run streamlit_app/app.py

---

## Files Included

- **gata_analysis.ipynb** → Main project notebook containing all steps  
- **requirements.txt** → Python dependencies  
- **results/** → Plots, figures, cluster visualizations 
- **data/** → Small sample dataset if required
- features.csv contains numerical descriptors (MW, length, GRAVY, aromaticity) generated from raw protein sequences.
- **streamlit_app/** → Streamlit dashboard code 

---

## Techniques Used

- Machine Learning (Unsupervised Learning)
- Feature Extraction & Dimensionality Reduction
- PCA & t-SNE Visualization
- Protein Sequence Analysis (Basic)
- Silhouette Score Evaluation
- Python: NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn
- Optional: Streamlit for UI

---

## Notes

- This project is continually improving; more features may be added later.
- Large datasets are not included due to GitHub’s file size limits.
- The notebook may be updated with additional visualizations or analysis.

---

## Author

**Ashutosh Barik**


   


