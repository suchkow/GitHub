from typing import Optional
from nemoguardrails.actions import action
from llama_index.core import SimpleDirectoryReader
from llama_index.core.llama_pack import download_llama_pack
from llama_index.packs.recursive_retriever import RecursiveRetrieverSmallToBigPack
from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.core.base.response.schema import StreamingResponse

# Global variable to cache the query_engine
query_engine_cache = None

def init():
    global query_engine_cache
    if query_engine_cache is not None:
        print('Using cached query engine')
        return query_engine_cache

    documents = SimpleDirectoryReader("data").load_data()
    print(f'Loaded {len(documents)} documents')
    recursive_retriever_stb_pack = RecursiveRetrieverSmallToBigPack(documents)
    query_engine_cache = recursive_retriever_stb_pack.query_engine

    return query_engine_cache


def get_query_response(query_engine: BaseQueryEngine, query: str) -> str:
    response = query_engine.query(query)
    if isinstance(response, StreamingResponse):
        typed_response = response.get_response()
    else:
        typed_response = response
    response_str = typed_response.response
    if response_str is None:
        return ""
    return response_str


@action(is_system_action=True)
async def user_query(context: Optional[dict] = None):
    user_message = context.get("user_message")
    print('user_message is ', user_message)
    query_engine = init()
    return get_query_response(query_engine, user_message)
