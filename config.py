

class Config :
    HOST = 'dbsample.cmuxpoe5idov.ap-northeast-2.rds.amazonaws.com'
    DATABASE = 'recipe_db'
    DB_USER = 'recipe_db_user'
    PASSWORD = '1234'

    PASSWORD_SALT = 'yh1206hihi'

    ### JWT 관련 변수 셋팅 = > 셋팅 후에는
    ### app.py 파일에서, 설정해줘야 한다.
    JWT_SECRET_KEY = 'yh1206hihi'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True