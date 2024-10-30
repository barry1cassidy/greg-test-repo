# Initialize PCA with 3 components
pca_3d = PCA(n_components=3)

# Fit and transform
pca_result_3d = pca_3d.fit_transform(embeddings)

# Add to DataFrame
df['pca-three'] = pca_result_3d[:, 2]

# Explained variance
print(f"Explained variance by first 3 principal components: {np.sum(pca_3d.explained_variance_ratio_):.2%}")
