"""
Response 返回格式
"""


class Response(object):
    @staticmethod
    def success(data, msg='success'):
        return {
            "data": data,
            "message": msg,
            "code": 0,
        }

    @staticmethod
    def error(msg, data):
        return {
            "data": data,
            "message": msg,
            "code": 1,
        }
