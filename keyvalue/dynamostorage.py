import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb')


class DynamoDB:
    def __init__(self, tableName="Practica1Cloud"):
        super().__init__()
        existing_tables = dynamodb.list_tables()
        print(existing_tables)

        if tableName not in existing_tables['TableNames']:
            try:
                dynamodb.create_table(
                    AttributeDefinitions=[
                        {
                            'AttributeName': 'key',
                            'AttributeType': 'S'
                        },
                        {
                            'AttributeName': 'sort',
                            'AttributeType': 'N'
                        }
                    ],
                    KeySchema=[
                        {
                            'AttributeName': 'key',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'sort',
                            'KeyType': 'RANGE'
                        }
                    ],
                    ProvisionedThroughput={
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5
                    },
                    TableName=tableName
                )
                dynamodb.get_waiter('table_exists').wait(TableName=tableName)
                self._tableName = tableName
                print("creación de tabla: " + tableName)
            except ClientError as e:
                print("err:" + tableName)
                print(e.response['Error'])
                print()
                raise e
        else:
            self._tableName = tableName
            print("la tabla ya existe: " + tableName)
        return

    def put(self, key, sort, value):
        if not isinstance(key, str):
            raise TypeError('key must be of str type!')
        if not isinstance(sort, int):
            raise TypeError('sort must be of int type!')
        if not isinstance(value, str):
            raise TypeError('sort must be of int type!')
        try:
            response = dynamodb.put_item(
                TableName=self._tableName,
                Item={
                    'key': {"S": key},
                    'sort': {"N": str(sort)},
                    'value': {"S": value}
                }
            )
        except ClientError as e:
            print(e.response['Error'])
            raise e
        return

    def get(self, key, sort):
        if not isinstance(key, str):
            raise TypeError('key must be of str type!')
        response = dynamodb.get_item(
            TableName=self._tableName,
            Key={
                'key': {"S": key},
                'sort': {"N": str(sort)}
            },
            ReturnConsumedCapacity='TOTAL',
        )
        return response

    def close(self):
        response = dynamodb.delete_table(
            TableName=self._tableName
        )
        print(response)
        return
