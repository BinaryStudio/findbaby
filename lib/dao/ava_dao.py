from firebase import firebase
from random import random

class AvaDao(object):
    def __init__(self):
        self.fb = firebase.FirebaseApplication \
                  ('https://parkplace.firebaseio.com', None)

    def create(self, id, nums):
        self.fb.put('/ava', str(id), nums)

    def update(self, id, nums):
        self.fb.patch('/ava', { str(id): nums })

    def delete(self, id):
        self.fb.delete('/ava', str(id))

    def get(self, id):
        return self.fb.get('/ava', str(id))

    def incn(self, id, num):
        cur = int(self.get(id))
        cur += num
        self.update(id, cur)

    def decn(self, id, num):
        cur = int(self.get(id))
        cur -= num
        self.update(id, cur)


if __name__ == '__main__':
    ava = AvaDao()
