from llama_index.core import SimpleDirectoryReader
from llama_index.core import download_loader
from llama_index.core import Document
from llama_index.readers.database import DatabaseReader
from llama_index.core import VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core import Settings # global
import os

documents = SimpleDirectoryReader("./data").load_data()

reader = DatabaseReader(
    scheme=os.getenv("DB_SCHEME"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    dbname=os.getenv("DB_NAME"),
)

query = "SELECT * FROM users"
documents = reader.load_data(query=query)

doc = Document(text="text")

#High Level

vector_index = VectorStoreIndex.from_documents(documents)
vector_index.as_query_engine()

text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)


Settings.text_splitter = text_splitter
# per-index
index = VectorStoreIndex.from_documents(
    documents, transformations=[text_splitter]
)

#Low Level

documents = SimpleDirectoryReader("./data").load_data()
pipeline = IngestionPipeline(transformations=[TokenTextSplitter(), ...])
nodes = pipeline.run(documents=documents)

document = Document(
    text="text",
    metadata={"filename": "<doc_file_name>", "category": "<category>"},
)