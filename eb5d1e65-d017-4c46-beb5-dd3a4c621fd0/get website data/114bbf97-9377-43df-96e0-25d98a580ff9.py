
# Initialize PCA with 2 components
pca = PCA(n_components=2)

# Fit PCA on the embeddings and transform
pca_result = pca.fit_transform(embeddings)

# Add PCA results to the DataFrame
df['pca-one'] = pca_result[:, 0]
df['pca-two'] = pca_result[:, 1]

# Explained variance
print(f"Explained variance by first 2 principal components: {np.sum(pca.explained_variance_ratio_):.2%}")
