import vk
import re
import string
frequency = {}

if __name__ == "__main__":
    token = "9f5da77d9f5da77d9f5da77d729f2b1ef599f5d9f5da77dff1ca9a0dec3327365effe5c"
    session = vk.Session(access_token=token)
    vk_api = vk.API(session)
    data = vk_api.wall.get(owner_id='-35488145', v=5.21, count=200)
    d = dict()
    for item in data['items']:
        word = item['text'].lower().split()
        for i in set(word):
            if len(i) > 2:
                d[i] = word.count(i)
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1], reverse=True)

    for i in list_d:
        print(i[0], ':', i[1])
