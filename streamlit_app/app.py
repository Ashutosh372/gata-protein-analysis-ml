import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

st.set_page_config(layout="wide", page_title="GATA Protein Analysis Dashboard")

st.title("GATA Protein Analysis — Interactive Dashboard")

uploaded_file = st.file_uploader("Upload CSV (first column = ID, rest = features)", type=["csv"])

st.sidebar.header("Settings")
method = st.sidebar.selectbox("Dimensionality Reduction", ["PCA", "t-SNE"])
cluster_algo = st.sidebar.selectbox("Clustering Method", ["DBSCAN", "KMeans"])

eps = st.sidebar.number_input("DBSCAN eps", value=0.5)
min_samples = st.sidebar.slider("DBSCAN min_samples", 1, 10, 5)
k = st.sidebar.slider("K for KMeans", 2, 10, 3)

show_heatmap = st.sidebar.checkbox("Show Heatmap", True)
show_table = st.sidebar.checkbox("Show Labeled Table", True)

def projection(X, method_name):
    if method_name == "PCA":
        return PCA(n_components=2).fit_transform(X)
    return TSNE(n_components=2, random_state=42).fit_transform(X)

def scatter(X_proj, labels, title):
    fig, ax = plt.subplots(figsize=(6, 5))
    for lab in np.unique(labels):
        mask = labels == lab
        ax.scatter(X_proj[mask, 0], X_proj[mask, 1], label=str(lab), alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel("Component 1")
    ax.set_ylabel("Component 2")
    ax.legend(title="Cluster")
    return fig

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    ids = df.iloc[:, 0].astype(str)
    X = df.iloc[:, 1:]
    X_numeric = X.select_dtypes(include=[np.number])

    if X_numeric.empty:
        st.error("No numeric features detected.")
        st.stop()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_numeric)

    proj = projection(X_scaled, method)

    if cluster_algo == "DBSCAN":
        labels = DBSCAN(eps=eps, min_samples=min_samples).fit_predict(X_scaled)
    else:
        labels = KMeans(n_clusters=k, random_state=42).fit_predict(X_scaled)

    if len(np.unique(labels)) > 1:
        try:
            mask = labels != -1
            sil = silhouette_score(X_scaled[mask], labels[mask])
            sil_text = f"Silhouette Score: {sil:.3f}"
        except:
            sil_text = "Silhouette Unavailable"
    else:
        sil_text = "Only one cluster detected"

    st.write(f"### Projection + Clusters ({sil_text})")
    fig = scatter(proj, labels, f"{method} + {cluster_algo}")
    st.pyplot(fig)

    if show_heatmap:
        st.write("### Feature Correlation Heatmap")
        corr = X_numeric.corr()
        fig2, ax2 = plt.subplots(figsize=(7, 5))
        im = ax2.imshow(corr, cmap="coolwarm")
        ax2.set_xticks(range(len(corr.columns)))
        ax2.set_yticks(range(len(corr.columns)))
        ax2.set_xticklabels(corr.columns, rotation=90)
        ax2.set_yticklabels(corr.columns)
        fig2.colorbar(im)
        st.pyplot(fig2)

    labeled_df = pd.DataFrame(X_numeric, columns=X_numeric.columns)
    labeled_df.insert(0, "ID", ids)
    labeled_df["Cluster"] = labels

    if show_table:
        st.write("### Labeled Data")
        st.dataframe(labeled_df.head(50))

    csv = labeled_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Labeled CSV", csv, "gata_labeled.csv", "text/csv")

else:
    st.info("Upload a CSV file to begin.")

