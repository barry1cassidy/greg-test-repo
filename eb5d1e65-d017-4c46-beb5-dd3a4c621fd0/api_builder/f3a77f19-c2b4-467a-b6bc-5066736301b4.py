# Directory containing .txt files

# Initialize a string to store the combined text of the top 3 articles
combined_text = ""

# Loop through the top 3 filenames and retrieve their text from the .txt files
for filename in top_3_filenames:
    filepath = filename
    
    # Read the article content
    with open(f"{filepath}", 'r', encoding='utf-8') as file:
        article_text = file.read()
    
    # Append the article text to the combined_text
    combined_text += article_text + "\n\n"  # Add some spacing between articles

RESPONSE = f'Answer this question: {prompt} considering the information contained in this text: {combined_text }'

print(RESPONSE)

