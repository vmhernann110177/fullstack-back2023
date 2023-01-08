""" docstring: imports"""
from flask import Flask, request, redirect
from persistencia import guardar_pedido

app = Flask(__name__)

#   Prepara http://localhost:5000/helloW en GET
@app.route("/helloActFin")
def hello():
    """ docstring: levanta http://localhost:5000/helloW) """
    return "<html><body><div>Hello world, since flask II!.. In Final Activitie</div></body></html>"

#   Prepara http://localhost:5000/pizza en POST
@app.route("/pizza", methods=['POST'])
def pizza():
    """ docstring: levanta http://localhost:5000/pizza) """
    parametro_1 = request.form.get("p1")
    parametro_2 = request.form.get("p2")
# Aquí se imprime en la consola de python, Nombre y Apellido.
    print(parametro_1)
    print(parametro_2)
# Limpia el archivo pedidos .txt de cualquier contenido
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
        print("He limpiado el archivo: pedidos.txt")
# Escribe archivo pedidos.txt nombre y apellido d prepara_pedido.html, imprimelos en consola pyhton
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        guardar_pedido(parametro_1, parametro_2,"pedidos.txt")
        print("")
        print("En pedidos.txt; he imprimido una lineas que es:")
        print("")
        print("parametro_1 (Nombre), parametro_2 (Apellidos): ")
        print(" " + parametro_1  + " "+ parametro_2)
        file.close()

# Si todo bien redirige navegador a  pagina solicita_pedido.html
    return redirect("http://localhost/solicita_pedido.html", code=302)
