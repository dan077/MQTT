import json
import mysql.connector


def send(paquete):
    # convertimos el string a json
    try:
        info_json = json.loads(paquete)

    except:
        return "Error al procesar paquete json";
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin",
            database="prueba1"
        )
    except:
        return "Error de conexion (DB)"

    nodo = info_json['Nodo_desc'][1].get('idNodo')  # como el id está en la posicion 1.
    if (nodo is None):
        return "No se encontro el nodo";

    mycursor = mydb.cursor()

    for Sensores_info in info_json['Sensores_info']:
        mycursor.execute("""INSERT INTO prueba (sensor,valor,nodo) values (%s,%s,%s)""",
                         (Sensores_info["idSensor"], Sensores_info["Valor"], nodo))

        mydb.commit()

    return "ok";
