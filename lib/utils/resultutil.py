
def returnSucc(data):
    rs = {}
    rs['result'] = 'success'
    rs['data'] = data
    return rs

def returnErr(message):
    return "{'result': error, 'message': %s}" %(message)
