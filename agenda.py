from ast import operator
import csv
from pickle import TRUE

lista_contactos = []

def mostrarAgenda():
    with open("agenda.csv") as csv_file:
        # Creamos que el archivo csv se convierta en un diccionario separado por ;
        csv_reader = csv.DictReader(csv_file, delimiter=",")

        # Leemos las cabeceras y si estan imprimimos su contenido
        for row in csv_reader:
            lista_contactos.append(row)
            print(row)

    csv_file.close()

def agregarContacto():

    nombre=input("Escribe el nombre: ")
    apellidos=input("Escribe los apellidos: ")
    email=input("Escribe el email: ")
    tef1=input("Escribe el telefono1: ")
    tef2=input("Escribe los telefono2: ")
    direcc=input("Escribe la direccion: ")

    contacto = {
        "nombre": nombre,
        "apellidos": apellidos,
        "email": email,
        "tef1": tef1,
        "tef2": tef2,
        "direccion": direcc
    }

    lista_contactos.append(contacto)

def mostrarAgendaOrdenada():
    with open("agenda.csv") as csv_file:
        # Hacemos que el archivo csv se convierta en un diccionario separado por ;
        csv_reader = csv.DictReader(csv_file, delimiter=",")

        listadicc = list(csv_reader)


        #         listadicc = list(entrada)  # Obtener lista de diccionarios
        # listadiccord = sorted(listadicc, 
        #                     key=operator.itemgetter('consumo'), 
        #                     reverse=True)
        # for registro in listadiccord:
        #     print(registro)

        # print(ordenada)

    csv_file.close()

def salir():
    print("Saliendo...")
    with open('agenda.csv', 'w', newline='') as csvfile:
        fieldnames = ['nombre', 'apellidos', 'email', 'tef1', 'tef2', 'direccion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lista_contactos)

# Inicio Programa

bucle = True

while bucle == True:
    print("**************************")
    print("1. Mostrar un menú para usar la agenda")
    print("2. Guardar datos de un contacto")
    print("3. Modificar datos de un contacto")
    print("4. Dar de baja a un contacto (Eliminar)")
    print("5. Buscar un contacto")
    print("6. Mostrar la lista de contactos ordenada")
    print("7. Salir y guardar")
    print("**************************")

    opcion = input("Que opcion eliges: ")
    listaAgregar = []
    x = range(6)

    if (opcion == "1"):
        mostrarAgenda()
    elif (opcion == "2"):
        agregarContacto()
    elif (opcion == "3"):
        print("Estas en el tres")
    elif (opcion == "4"):
        print("Estas en el cuatro")
    elif (opcion == "5"):
        print("Estas en el cinco")
    elif (opcion == "6"):
        mostrarAgendaOrdenada()
    elif (opcion == "7"):
        salir()
        bucle=False
    else:
        print("Opción no encontrada")