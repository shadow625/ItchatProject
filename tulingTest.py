#  -*- coding:utf-8 -*-
import requests
import urllib
import json

url='http://openapi.tuling123.com/openapi/api/v2'
def get_reply(stext):
	value={"reqType":0,"perception":{"inputText":{"text":str(stext)}},"userInfo":{"apiKey":"501dba59c7f54555b0d9b66f4acabd94","userId":"235827"}}
	req=requests.post(url,data=json.dumps(value))
	return req.text
if __name__ == '__main__':
	print(get_reply("我的亲"))