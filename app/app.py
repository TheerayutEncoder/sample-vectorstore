from dotenv import load_dotenv
import os


from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


# Clear existing environment variables
os.environ.clear()

# get the API keys from the environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['PINECONE_API_KEY'] = os.getenv("PINECONE_API_KEY")


# initialize the OpenAI embeddings and Pinecone vector store
index_name = "sample-vector"
embeddings = OpenAIEmbeddings()

# path to an example text file
loader = TextLoader("src/textfile/sample.txt")
documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)

# vectorstore_from_docs = PineconeVectorStore.from_documents(
#     docs,
#     index_name=index_name,
#     embedding=embeddings
# )

# print(vectorstore_from_docs)
# print(type(vectorstore_from_docs))
# texts = ["Tonight, I call on the Senate to: Pass the Freedom to Vote Act.", "ne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.", "One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence."]

# vectorstore_from_texts = PineconeVectorStore.from_texts(
#     texts,
#     index_name=index_name,
#     embedding=embeddings
# )

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)


if __name__ == "__main__":
    query = "Who is Theerayut?"
    response = vectorstore.similarity_search(query)
    print(response)