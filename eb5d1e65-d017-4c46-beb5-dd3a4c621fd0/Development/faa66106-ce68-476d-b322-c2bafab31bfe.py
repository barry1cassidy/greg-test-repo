
# Set random seed for reproducibility
random_seed = 42

# Initialize t-SNE with desired parameters
tsne = TSNE(n_components=2, perplexity=30, random_state=random_seed, n_iter=1000, verbose=1)

# Apply t-SNE to the embeddings
tsne_results = tsne.fit_transform(embeddings)

# Add the t-SNE results to the DataFrame
df['tsne-2d-one'] = tsne_results[:, 0]
df['tsne-2d-two'] = tsne_results[:, 1]