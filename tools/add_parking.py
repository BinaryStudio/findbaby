import requests

uids = [
'ae31ba01c745236158bbbc6e',
'b602922413add6f8430245be',
'ea4a3dc9e93c18534e5547de',
'13be88500133bf7095ca072a',
'd146b3889ba9a5de7402694c',
'a0e3e112271efdc753e5c581',
'386d6b975e5afee8e5e965d9',
'7a6be49e97da00155fd4feda',
'5e3725436d58e5afa1046430',
'6ee010206fbc449152e5c528' 
]

if __name__ == '__main__':
    for uid in uids:
        url = 'http://182.92.186.215:5000/rest/parkings'
        data = {'name': 'test', 'info': 'test', 'hour': 20.0, 'day': 80.0,
                'uid': uid, 'total_pak':200}
        print uid
        print data
        print requests.post(url, data=data)
