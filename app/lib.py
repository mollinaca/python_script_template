import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


class MyClass:
    def __init__(self):
        self.my_value = os.getenv("MY_VALUE")

    def myclass_test(self):
        print(self.my_value)


class F:

    def my_function(self):
        ret = {"ok": True}
        my_instance = MyClass()
        my_instance.myclass_test()
        return ret
