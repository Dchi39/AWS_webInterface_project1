import json
import boto3
import uuid
from datetime import datetime
from decimal import Decimal

# Define both DynamoDB tables
dynamodb = boto3.resource('dynamodb')
websort_table = dynamodb.Table('websort_system')  # For web input data
esp_table = dynamodb.Table('esp_data')            # For ESP32 sensor data

def lambda_handler(event, context):
    method = event['httpMethod']

    # ---------------------
    # POST Method - Insert
    # ---------------------
    if method == 'POST':
        try:
            body = json.loads(event['body'])
            source = body.get('source')

            if source == 'web':
                # Handle web form data
                item = {
                    'id': str(uuid.uuid4()),
                    'item': body.get('item'),
                    'count': int(body.get('count')),
                    'machine': body.get('machine'),
                    'motor': body.get('motor'),
                    'timestamp': datetime.utcnow().isoformat()
                }
                websort_table.put_item(Item=item)
                return response(200, {'message': 'Web data inserted successfully'})

            elif source == 'esp':
                # Handle ESP32 sensor data
                item = {
                    'device_id': body.get('device_id', 'esp32'),
                    'timestamp': datetime.utcnow().isoformat(),
                    'temperature': Decimal(str(body.get('temperature'))),
                    'humidity': Decimal(str(body.get('humidity')))
                }
                esp_table.put_item(Item=item)
                return response(200, {'message': 'ESP data inserted successfully'})

            else:
                return response(400, {'error': 'Invalid source specified'})

        except Exception as e:
            return response(500, {'error': str(e)})

    # ---------------------
    # GET Method - Retrieve
    # ---------------------
    elif method == 'GET':
        try:
            params = event.get('queryStringParameters') or {}
            data_type = params.get('type')  # 'web' or 'esp'

            if data_type == 'web':
                scan = websort_table.scan()
                items = sorted(scan.get('Items', []), key=lambda x: x.get('timestamp', ''), reverse=True)
                return response(200, items[0] if items else {})

            elif data_type == 'esp':
                scan = esp_table.scan()
                items = sorted(scan.get('Items', []), key=lambda x: x.get('timestamp', ''), reverse=True)
                return response(200, items[0] if items else {})

            else:
                return response(400, {'error': 'Invalid type in query parameters'})

        except Exception as e:
            return response(500, {'error': str(e)})

    # ---------------------
    # Unsupported Methods
    # ---------------------
    else:
        return response(405, {'error': 'Method Not Allowed'})

# ---------------------
# CORS + Response Helper
# ---------------------
def response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST'
        },
        'body': json.dumps(body, default=str)
    }
