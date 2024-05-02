import requests
import psycopg2

api_url = "https://dog.ceo/api/breeds/image/random"
links = []
while len(links) < 100:
    response = requests.get(api_url)
    print(response.json())
    if response.json()['message'] not in links:
        links.append(response.json()['message'])
print(links)


conn = psycopg2.connect(
    dbname="nfac",
    user="nfac",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

for link in links:
    cursor.execute(
        "INSERT INTO scores (link, score) VALUES (%s, %s)",
        (link, 0)
    )

conn.commit()
cursor.close()
conn.close()


