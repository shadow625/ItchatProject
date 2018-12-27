import itchat
import requests
import json

url = 'http://openapi.tuling123.com/openapi/api/v2'
mIsItchatEnabled = False


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg_check_text_before_reply(msg) == 'True':
        return "auto reply is enabled"
    if msg_check_text_before_reply(msg) == 'False':
        return "auto reply is disabled"
    if not mIsItchatEnabled:
        return
    value = {"reqType": 0, "perception": {"inputText": {"text": msg.text}},
             "userInfo": {"apiKey": "501dba59c7f54555b0d9b66f4acabd94", "userId": "235827"}}
    req = requests.post(url, data=json.dumps(value))
    a = eval(req.text)
    reply = a.get("results")[0].get('values').get('text')
    print("{\n\'msg\':\t\t%s\n\'reply\':\t%s\n}\n" % (msg.text, reply))
    return reply


def image_reply(msg):
    pass


def msg_check_text_before_reply(msg):
    global mIsItchatEnabled
    if str.lower(msg.text) == 'true':
        mIsItchatEnabled = True
        return 'True'
    if str.lower(msg.text) == 'false':
        mIsItchatEnabled = False
        return 'False'
    return


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
