import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))  # 获取路径
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

# aa = os.getenv('FLASK_DEBUG')
# bb = os.getenv('FLASK_APP')
# print('aa', aa)
# print('bb', bb)


class Config(object):
    pass
    # DEBUG = os.getenv('FLASK_DEBUG')


if __name__ == '__main__':
    config = Config()
