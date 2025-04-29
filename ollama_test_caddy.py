from langchain_ollama import ChatOllama

# Configuration
encoded_credentials = "dXNlcjE6bXlwYXNzMQ=="

headers = {
'Authorization': f'Basic {encoded_credentials}'
}
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0,
    base_url="http://<server-url>:8085",
    client_kwargs={'headers': headers}
)

# Invoke the llm
try:
    response = llm.invoke("Hello, how are you?")
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")