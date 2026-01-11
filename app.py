import json
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

prompt = """
<|begin_of_text|>
<|system|>
You are a helpful AI assistant. Give clear and concise explanations.
<|end_of_system|>

<|user|>
When RCB will win the title?
<|end_of_user|>

<|assistant|>
"""

payload = {
    "prompt": prompt,
    "max_gen_len": 512,
    "temperature": 0.7,
    "top_p": 0.9
}

response = bedrock.invoke_model(
    modelId="meta.llama3-70b-instruct-v1:0",
    body=json.dumps(payload),
    contentType="application/json",
    accept="application/json"
)

result = json.loads(response["body"].read())
print(result["generation"])
