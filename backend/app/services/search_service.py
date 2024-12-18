from sentence_transformers import SentenceTransformer
import weaviate

# Initialize the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Weaviate client
client = weaviate.Client("http://localhost:8080")


def process_and_store_messages(messages):
    """
    Process and store messages with semantic embeddings.
    """
    for msg in messages:
        content = msg.get("content", "")
        vector = model.encode(content).tolist()

        # Store in Weaviate
        client.data_object.create(
            data_object={"content": content, "platform": msg.get("platform")},
            vector=vector,
            class_name="Message",
        )
