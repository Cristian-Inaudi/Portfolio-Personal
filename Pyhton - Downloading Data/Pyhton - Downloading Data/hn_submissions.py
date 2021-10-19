from operator import itemgetter

import requests

#Crear una llamada API y almacenar la respuesta.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Procesar informacion sobre cada presentacion.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #Crear una llama a API separada para cada presentacion.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #Construir un diccionario para cada articulo.
    if "descendants" in response_dict:
        comentarios = response_dict['descendants']
    else:
        comentarios = 0
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': comentarios,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse= True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

