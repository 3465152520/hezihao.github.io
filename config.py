import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))    # 获取路径
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

print('aa', basedir)
print('bb', os.path.dirname(__file__))


class Config(object):
    pass


if __name__ == '__main__':
    config = Config()
