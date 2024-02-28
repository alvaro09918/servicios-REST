from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
            
        elif self.path.startswith("/buscar_estudiante_inicial/"):
            inicial =self.path.split("/")[-1]
            
            estudiante = next(
                (estudiante for estudiante in estudiantes if (estudiante["id"])[0] ==inicial),
                None,
            )
            if estudiante:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        elif self.path.startswith("/contar_carreras/"):
            carrera =self.path.split("/")[-1]
            cant_estudiantes = next(
                (sum(1 for estudiante in estudiantes if estudiante["carrera"]==carrera)),
                None,
            )
            if cant_estudiantes:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(cant_estudiantes).encode("utf-8"))
        elif self.path=="/total_estudiantes":
            total_estudiantes=len(estudiantes)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(total_estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
       
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()