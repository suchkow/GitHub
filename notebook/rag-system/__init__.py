from llama_index.core import SimpleDirectoryReader
import os


dir = os.getcwd()
path = os.path.join(dir, 'data')

try:
    data = SimpleDirectoryReader(path).load_data()
    print("Data Loaded:", data[:1])
except Exception as e:
    print("An error occurred while loading data:", e)

# winpath = r'C:\Users\suchk\Documents\Local Dev\GitHub\notebook\rag-system\data\ai_model_predictions.tsv'
# # docpath = os.path.join('data', 'ai_model_predictions.tsv')
# documents = SimpleDirectoryReader(winpath).load_data()
# print(len(documents ))