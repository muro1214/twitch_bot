import json
import random
import requests

bms_list = [{'url': 'http://mirai-yokohama.sakura.ne.jp/bms/data.json', 'prefix': '★'},
            {'url': 'https://stellabms.xyz/sl/score.json', 'prefix': 'sl'},
            {'url': 'https://stellabms.xyz/st/score.json', 'prefix': 'st'}
            ]


def random_select(bms, filter=None):
    res = requests.get(bms['url'])
    if not res.status_code == requests.codes.ok:
        return {
            'statusCode': 400,
            'body': f"Error. status = {res.status_code}"
        }

    jsonData = res.json()

    if filter:
        jsonData = [x for x in jsonData if x['level'] == str(filter)]
    
    if jsonData == []:
        return {
            'statusCode': 400,
            'body': "Error. Maybe wrong difficulty?"
        }

    i = random.randrange(len(jsonData))

    return {
        'statusCode': 200,
        'body': f"{bms['prefix']}{jsonData[i]['level']} {jsonData[i]['title']}".encode('utf-8')
    }


def lambda_handler(event, context):
    table = event['queryStringParameters']['table']
    filter = event['queryStringParameters'].get('level')

    if table == 'insane':
        return random_select(bms_list[0], filter)
    elif table == 'satellite':
        return random_select(bms_list[1], filter)
    elif table == 'stella':
        return random_select(bms_list[2], filter)
