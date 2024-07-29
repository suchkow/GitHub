# pip install chromadb
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext


documents = SimpleDirectoryReader("./data").load_data() # load some documents
db = chromadb.PersistentClient(path="./chroma_db") # initialize client, setting path to save data
chroma_collection = db.get_or_create_collection("quickstart") # create collection

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(documents, storage_context=storage_context) # create your index

# create a query engine and query
query_engine = index.as_query_engine()
response = query_engine.query("What is the meaning of life?")
print(response)