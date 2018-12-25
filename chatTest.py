import itchat
import requests
import urllib
import json
import pprint

url='http://openapi.tuling123.com/openapi/api/v2'
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	if msg['User']['NickName'] != "五歲兒":
		return
	value={"reqType":0, "perception":{"inputText":{"text":msg.text}}, "userInfo":{"apiKey":"501dba59c7f54555b0d9b66f4acabd94","userId":"235827"}}
	req=requests.post(url, data=json.dumps(value))
	a=eval(req.text)
	reply = a.get("results")[0].get('values').get('text')
	print("{\n\'msg\':\t\t%s\n\'reply\':\t%s\n}\n" % (msg.text, reply))
	return reply
itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
