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
        print()
        print(response["message"]["result"])
        # print()
        # print(response["translatedText"])


        return {'result' : 'success',
                'chinese' : chinese},200
    
class NewsResource(Resource) :
    def get(self) :

        query = request.args.get('query')
        display = request.args.get('display'),
        # request.args.get('start'),
        sort = request.args.get('sort') 

        # 1. 네이버 뉴스 검색 API를 호출한다

        req_header = { "X-Naver-Client-Id": "lvlXKbxzsfeexwIET9zZ",
                      "X-Naver-Client-Secret" : "K2ho6DDSQR" }
        
        # ***파라미터를 설정할 때엔 딕셔너리로 하여 설정 해준다.
        query_string = {'query' : query,
                        'display' : display,
                        'sort' : sort}

        response = requests.get('https://openapi.naver.com/v1/search/news.json',
                     params= query_string,
                     headers=req_header)
        

        # 리스펀스는 json으로 저장한다.
        response = response.json()
        print(response)
        response = response['items']
        

        return {'result' :'success',
                'items' : response,
                'count' : len(response)}, 200
    
class booksResource(Resource) :
     def get(self) :

        query = request.args.get('query')
        display = request.args.get('display')
        sort = request.args.get('sort')

        # 네이버 함수 호출

        req_parms = {'query' : query,
                         'display' : display,
                         'sort' : sort}
            
        req_header = {'X-Naver-Client-Id' : 'lvlXKbxzsfeexwIET9zZ',
                          'X-Naver-Client-Secret' : 'K2ho6DDSQR'}

        response = requests.get('https://openapi.naver.com/v1/search/book.json',
                         params=req_parms,
                         headers= req_header
                         )
        
        response = response.json()
        print()
        print(response)
        print()

        response = response['items']
    

            

        return {'result' : 'success',
                'items' : response,
                'count' : len(response)}, 200