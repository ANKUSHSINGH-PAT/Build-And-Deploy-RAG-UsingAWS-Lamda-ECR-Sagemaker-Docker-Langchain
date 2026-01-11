import os
import boto3
import sys
import json
print("Imported modules successfully.")

prompt="""You are a smart assistant. Please let me know what is machine learning?
"""

payload={

}
body=json.dumps(payload)
model_id='meta.llama3-3-70b-instruct-v1:0'

bedrock=boto3.client(service_name='badrock-runtime')
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept='application/json',
    contentType='application/json'

)
json_response=json.loads(response['body'].read().decode())
response_text=json_response['generatedText']
print(response_text)
