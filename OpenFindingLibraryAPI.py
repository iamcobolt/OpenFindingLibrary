from flask import Flask, request, jsonify
from azure.cosmos import CosmosClient
import os

app = Flask(__name__)

# Configure the Cosmos DB connection
url = os.environ['https://ofldb01.documents.azure.com:443/']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)
database_name = 'your_database_name'
container_name = 'your_container_name'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)


# API endpoint to send JSON data
@app.route('/api/send', methods=['POST'])
def send_data():
    data = request.get_json()
    container.upsert_item(data)
    return jsonify({"message": "Data stored successfully"}), 200


# API endpoint to receive JSON data based on id
@app.route('/api/receive/<id>', methods=['GET'])
def receive_data(id):
    query = f'SELECT * FROM c WHERE c.id = "{id}"'
    items = list(container.query_items(query=query, enable_cross_partition_query=True))

    if len(items) == 0:
        return jsonify({"message": "Data not found"}), 404

    return jsonify(items[0]), 200


if __name__ == '__main__':
    app.run()
