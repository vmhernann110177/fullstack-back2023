from flask import Flask, request, redirect, Response
from persistencia import guardar_pedido

app = Flask(__name__)


#   Pequeña prueba de flask.
@app.route("/helloActFin")
def hello():
#   """
#   Hello world, Prueba
#   """
    return "<html><body><div>Hello world, since flask II! Final Activitie</div></body></html>"


@app.route("/pizza", methods=['POST'])
def pizza():
#   """
#   pedir una pizza
#   """
    parametro_1 = request.form.get("p1")
    parametro_2 = request.form.get("p2")

# Aquí se imprime en la consola de python, Nombre y Apellido.
    print(parametro_1)
    print(parametro_2)

    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
        print("He limpiado el archivo: pedidos.txt")

    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        guardar_pedido(parametro_1, parametro_2,"pedidos.txt")
        print("")
        print("En pedidos.txt; he imprimido una lineas que es:")
        print("")
        print("parametro_1 (Nombre), parametro_2 (Apellidos): ")
        print(" " + parametro_1  + " "+ parametro_2)
        file.close()


    return redirect("http://localhost/solicita_pedido.html", code=302)


#   CORRIÓ MUY BIEN tanto tanto en el Navegador como en Postman, pero...
#   ...
#   
#   Veamos;
#   No queda claro del todo. Hay aspectos que se deben suponer que ocurran.
#   y efectivamente ocurren como se espera, sin embargo, lo que NO me gusta es tener que plantear estas supociciones.
#   
#   Éstas se hacen a partir del fichero: 'Naxer.FullStack.M1. Actividad_Final.U1.pdf' (La actividad).
#   
#   Me da impresión que es más claro deducir lo que debe ocurrir a partir de este documento.
#   Pienso que hace falta una breve explicación en los videos de la clase de lo que se espera que ocurra y como debe ocurrir.
#   
#   A pesar de esto, SI CORRIÓ lo supuesto, y lo hizo MUY BIEN, tanto en el navegadoR como en la APP de Escritorio de Postman.
#   
#   Hago notar que en postman hay que hacer click en "Preview" para ver la página solicita_pedido.html.
