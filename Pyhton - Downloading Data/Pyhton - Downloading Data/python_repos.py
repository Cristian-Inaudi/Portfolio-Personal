import requests

#Crear una llamada API y almacenar la respuesta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Almacenar respuesta de API en una variable.
response_dict = r.json()
print(f"Total de repositorios: {response_dict['total_count']}")

#Explorar informacion sobe los repositorios.
repo_dicts = response_dict['items']
print(f"Repositorios retornados: {len(repo_dicts)}")

print(f"\nInformacion seleccionada sobre el primer repositorio:")
for repo_dict in repo_dicts:
    print(f"Nombre: {repo_dict['name']}")
    print(f"Propietario: {repo_dict['owner']['login']}")
    print(f"Estrellas: {repo_dict['stargazers_count']}")
    print(f"Repositorio: {repo_dict['html_url']}")
    print(f"Creado: {repo_dict['created_at']}")
    print(f"Actualizado: {repo_dict['updated_at']}")
    print(f"Descripcion: {repo_dict['description']}")
    print("")

