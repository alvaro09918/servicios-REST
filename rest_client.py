import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Alvaro",
    "apellido": "Chambilla",
    "carrera": "Informatica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Rodrigo",
    "apellido": "Chambilla",
    "carrera": "Informatica",
}

post_response = requests.request(method="POST", 
                                url=ruta_post, 
                                json=nuevo_estudiante)
print(post_response.text)

# GET consulta a la ruta /buscar_estudiante_inicial/{inicial}
ruta_buscar_incial = url + "buscar_estudiante_inicial/J"
buscar_incial_response = requests.request(method="GET", 
                                url=ruta_buscar_incial)
print(buscar_incial_response.text)

# GET consulta a la ruta /contar_carreras/{carrera}
ruta_contar_carreras= url + "contar_carreras/Informatica"
contar_carreras_response = requests.request(method="GET", 
                                url=ruta_contar_carreras)
print(contar_carreras_response.text)

# GET consulta a la ruta /total_estudiantes
ruta_total_est = url + "total_estudiantes"
total_est_response = requests.request(method="GET", url=ruta_total_est)
print(total_est_response.text)


