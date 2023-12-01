import pinecone

# Initialize Pinecone
pinecone.init(api_key='4318148e-67ad-46b4-9120-8df54a6fb5f4', environment='asia-southeast1-gcp')

# Connect to your index
index_name = 'canopy--pdf-embeddings-index'
index = pinecone.Index(index_name)

# Delete all vectors in the index
delete_response = index.delete(deleteAll=True)

print(delete_response)