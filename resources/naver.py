from flask import request
from flask_restful import Resource
import requests
from mysql_connection import get_connection

class ChineseResurece(Resource) :
    def post(self) :

        data = request.get_json()

        # 네이버의 파파고 API를 호출하여 결과를 가져온다.

        # 파파고 API의 문서를 보고,
        # 어떤 데이터를 보내야 하는지 파악하여
        # requests 의 get, post, put, delete 등의
        # 함수를 이용하여 호출하면 된다.

        req_data = {
                        "source": "ko",
                        "target": "zh-CN",
                        "text": data['sentence']
                    }
        
        req_header = { "X-Naver-Client-Id": "lvlXKbxzsfeexwIET9zZ",
                      "X-Naver-Client-Secret" : "K2ho6DDSQR" }

        response = requests.post("https://openapi.naver.com/v1/papago/n2mt",  
                      req_data, 
                      headers= req_header )
        # 데이터를 파파고 서버로부터 받아 왔으니,
        # 우리가 필요한 데이터만 뽑아내면 된다.
        response = response.json()
        print()
        print(response)

        chinese = response["message"]["result"]["translatedText"]
        print()
        print(response["message"])
        print()
        print(chinese)
        # print()
        # print(response["result"])
        # print()
        # print(response["translatedText"])


        return {'result' : 'success',
                'chinese' : chinese},200