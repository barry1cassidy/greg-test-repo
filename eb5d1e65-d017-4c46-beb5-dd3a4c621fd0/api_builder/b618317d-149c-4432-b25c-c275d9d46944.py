def vectorize_article(text):
    # Tokenize the input text and convert to tensor
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding=True)
    
    # Get the hidden states from the model (we only need the last hidden state)
    with torch.no_grad():
        outputs = model(**inputs)
        last_hidden_state = outputs.last_hidden_state

    # Mean pooling to get a single vector for the article
    article_vector = last_hidden_state.mean(dim=1).squeeze()
    return article_vector

new_article_vector = vectorize_article(prompt).numpy().reshape(1, -1)

# Extract the vectors from the DataFrame for comparison
existing_vectors = np.array(df['embedding'].tolist())
 
# Compute cosine similarity between the new article vector and all existing vectors
similarities = cosine_similarity(new_article_vector, existing_vectors).flatten()

# Find the top 3 most similar articles
top_3_indices = similarities.argsort()[-3:][::-1]  # Get indices of top 3 articles

# Get the corresponding filenames of the top 3 similar articles
top_3_filenames = df.iloc[top_3_indices]['filename'].values

# Display the top 3 filenames
print("Top 3 similar articles:")
for filename in top_3_filenames:
    print(filename)

