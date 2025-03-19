import ollama

cat_vector = ollama.embed(model='llama3.2', input='gato')
dog_vector = ollama.embed(model='llama3.2', input='minino')
# print(cat_vector)
# print EmbedResponse length

# this function get cosine similarity between two vectors
def cosine_similarity(v1, v2):
    dot_product = sum([a*b for a, b in zip(v1, v2)])
    magnitude_v1 = sum([a**2 for a in v1])**0.5
    magnitude_v2 = sum([a**2 for a in v2])**0.5
    return dot_product / (magnitude_v1 * magnitude_v2)

similarity = cosine_similarity(cat_vector.embeddings[0], dog_vector.embeddings[0])
print(similarity)