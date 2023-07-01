import uuid

import boto3


class TransactionsTable:
    def __init__(self):
        self.db = boto3.resource(
            "dynamodb",
            endpoint_url="http://database:8000",
            region_name="dummy",
            aws_access_key_id="dummy",
            aws_secret_access_key="dummy"
        )
        self.table_name = "Transactions"
        self.table = self.db.Table(self.table_name)

    def create_table(self):
        try:
            self.db.create_table(
                TableName=self.table_name,
                AttributeDefinitions=[
                    {
                        "AttributeName": "transaction_id",
                        "AttributeType": "S"
                    }
                ],
                KeySchema=[
                    {
                        "AttributeName": "transaction_id",
                        "KeyType": "HASH"
                    }
                ],
                ProvisionedThroughput={
                    "ReadCapacityUnits": 10,
                    "WriteCapacityUnits": 10
                }
            )
        except self.db.meta.client.exceptions.ResourceInUseException:
            print("Table already exists.")

    def insert_items(self, data: dict):
        item = {
            "transaction_id": str(uuid.uuid4()),
            "price": {
                "original_price": data.get("price")[1],
                "offer_price": data.get("price")[0]
            },
            "title": data.get("title")
        }
        self.table.put_item(Item=item)

    def get_items(self, limit):
        response = self.table.scan(Limit=limit)
        items = response["Items"]

        return items
