import itchat
import requests
import urllib
import json

url='http://openapi.tuling123.com/openapi/api/v2'
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	value={"reqType":0,"perception":{"inputText":{"text":msg.text}},"userInfo":{"apiKey":"501dba59c7f54555b0d9b66f4acabd94","userId":"235827"}}
	req=requests.post(url,data=json.dumps(value))
	a=eval(req.text)
	print(a)
	return a.get("results")[0].get('values').get('text')
itchat.auto_login()
itchat.run()
