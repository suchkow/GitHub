from llama_index.core import VectorStoreIndex

# to create an index vectors from Nodes or Documents
index = VectorStoreIndex.from_documents(documents)
index = VectorStoreIndex(nodes)
