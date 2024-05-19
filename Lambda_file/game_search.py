import json
import boto3

def lambda_handler(event, context):
    # 建立Bedrock客戶端
    bedrock_client = boto3.client('bedrock-agent-runtime')
    
    # 設置Agent的參數
    agent_name = 'Assistant_Game_score'
    agentAliasId = 'peko'
    input_text = event['input_text']
    sessionId = event['session_id']
    
    # 呼叫Bedrock Agent
    response = bedrock_client.invoke_agent(
        sessionId=sessionId,
        agentAliasId='6RKZPTFOFV',    
        agentId="DMKKPHYXDK",
        inputText=input_text,
        enableTrace= True,
endSession= False
    )
    print("____")
    # 獲取Agent的回應
    # output_text = response['functionResult']['']
    
    res = ''
    # try:
    for event in response['completion']:
        if 'chunk' in event:
            data = event['chunk']['bytes']
            res = data.decode('utf8')
            end_event_received = True
    # except:
    #     res.append("???")
    #     # res.append(e.message)
    return {
        'statusCode': 200,
        'body':res
    }
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps({
    #         'input_text': input_text,
    #         'output_text': output_text
    #     })
    # }