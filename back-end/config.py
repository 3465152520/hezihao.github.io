import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# print(BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, 'env'), encoding='utf-8')


class Config(object):
    pass
