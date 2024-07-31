from llama_index.core import SimpleDirectoryReader
# from llama_index.core import download_loader
# from llama_index.readers.database import DatabaseReader
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core import Settings
from llama_index.core import Document
import os


dir = os.getcwd()
path = os.path.join(dir, 'data')
documents = SimpleDirectoryReader(path).load_data()

# reader = DatabaseReader(
#     scheme=os.getenv("DB_SCHEME"),
#     host=os.getenv("DB_HOST"),
#     port=os.getenv("DB_PORT"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASS"),
#     dbname=os.getenv("DB_NAME"),
# )
# query = "SELECT * FROM users"
# documents = reader.load_data(query=query)


# to create document instance manually 
# from llama_index.core import Document
# doc = Document(text="text")

# HIGH LEVEL
# for controlling document split-up more precise
# creates Nodes which store text, metadata (as Document) and the relationship to their parent
# vector_index = VectorStoreIndex.from_documents(documents)
# vector_index.as_query_engine()

# customizing core components (pass custom transformations list or apply global Settings)
# text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)
# Settings.text_splitter = text_splitter
# index = VectorStoreIndex.from_documents(documents, transformations=[text_splitter]) # per-index

# LOW LEVEL
# key step to process your documents is to split them into "chunks"/Node objects.
# The key idea is to process your data into bite-sized pieces that can be retrieved / fed to the LLM.
pipeline = IngestionPipeline(transformations=[
                                SentenceSplitter(chunk_size=1024, chunk_overlap=20),
                                TokenTextSplitter(chunk_size=1024, chunk_overlap=20, separator='/t')])
pipeline.disable_cache = True
nodes = pipeline.run(documents=documents, num_workers=4)

print(len(nodes))

index = VectorStoreIndex(nodes)

# # if needed add metadata for documents
# document = Document(text="text", metadata={"filename": "<doc_file_name>", "category": "<category>"})

# # passing Nodes directly into vector index (indexer)
# from llama_index.core.schema import TextNode
# node1 = TextNode(text="<text_chunk>", id_="<node_id>")
# node2 = TextNode(text="<text_chunk>", id_="<node_id>")
# index = VectorStoreIndex([node1, node2])
