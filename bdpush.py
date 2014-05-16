
# coding:utf-8

import hashlib
import requests
from time import time
try:
    import ujson as json
except ImportError:
    import json
try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus


class BaiduPush:

    expire = 300
    host = 'http://channel.api.duapp.com/rest/2.0/'

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def gen_sign(self, http_method, url, params):
        txt = ''
        keys = list(params.keys())
        keys.sort()

        for i in keys:
            txt += '%s=%s' % (i, params[i])
        return  hashlib.md5(quote_plus('%s%s%s%s' % (http_method, url, txt, self.secret_key)).encode('utf-8')).hexdigest()

    def request(self, method, uri, req_params, req_method='POST'):
        url = '%s%s' % (self.host, uri)

        params = {
            'method' : method,
            'apikey' : self.api_key,
            'timestamp' : int(time()),
            'expires' : int(time()) + self.expire,
        }

        params.update(req_params)
        params['sign'] = self.gen_sign(req_method, url, params)


        if req_method == 'POST':
            return requests.post(url, data=params)
        else:
            return requests.get(url, params=params)


    def push_msg(self, push_type, msg_title, msg_txt, msg_keys, user_id=None, channel_id=None, tag=None,
                 device_type=None, message_type=None):
        return self._push_msg(push_type, json.dumps({'title':msg_title,'description':msg_txt}), msg_keys,
                 user_id=user_id, channel_id=channel_id, tag=tag, device_type=device_type, message_type=message_type)

    def _push_msg(self, push_type, messages, msg_keys, user_id=None, channel_id=None, tag=None,
                 device_type=None, message_type=None):
        params = {
            'push_type': push_type,
            'messages': messages,
            'msg_keys': msg_keys,
        }

        if device_type:
            params['device_type'] = device_type
        if message_type:
            params['message_type'] = message_type

        if push_type == 1:
            if user_id and channel_id:
                params['user_id'] = user_id
                params['channel_id'] = channel_id
            else:
                return 1
        elif push_type == 2:
            if tag:
                params['tag'] = tag
            else:
                return 2

        return self.request('push_msg', 'channel/channel', params)


if __name__ == '__main__':
    i = BaiduPush('api_key','secret_key')
    #ret = i.push_msg(1, '通知', '内容', 'key', user_id=0, channel_id=0)
    #ret = i.push_msg(2, 'tag消息', '内容', 'key', tag="qwerasdfz")
    ret = i.push_msg(3, 'test', '内容', 'key')

    print(ret.status_code)
    print(ret.text)
