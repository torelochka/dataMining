import vk

import psycopg2

def take_posts():
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
    return list_d


def main():
    all_posts = take_posts()
    
    con = psycopg2.connect(
        database="vk_parse",
        user="postgres",
        password="Qwerty007",
        host="datamining.cailalbtgvc7.us-east-1.rds.amazonaws.com",
        port="5432"
    )

    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS WORDS
                (ID SERIAL PRIMARY KEY,
                WORD VARCHAR(200) NOT NULL,
                NUM INT);'''
    )
    cur.execute('TRUNCATE TABLE WORDS')

    query = "INSERT INTO words (WORD, NUM) VALUES"
    count = 0
    for i in all_posts:
        if count >= 100:
            break
        query += "('" + i[0] + "' ," + str(i[1]) + "),"
        count += 1
    query = query[0:-1] + ";"

    cur.execute(query)

    con.commit()
    con.close()

main()