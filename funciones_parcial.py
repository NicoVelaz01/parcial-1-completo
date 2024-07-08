from random import randint

def menu()-> str:
    """Imprimi un menu

    Returns:
        input: nos pide una opcion
    """
    print(f"{'Menu de Opciones':^50s}")
    print("1- Cargar archivo .CSV")
    print("2- Imprimir Lista")
    print("3- Asignar Rating")
    print("4- Asignar Genero")
    print("5- Filtrar por genero")
    print("6- Ordenar Peliculas por genero y rating descendente")
    print("7- Informar mejor Rating")
    print("8- Guardar pelicula con mejor rating en archivo .JSON")
    print("9- Salir")

    return input("Ingrese una opcion: ")
# 1
def get_path_actual(nombre_archivo: str)-> str:
    """Obtiene el path del nombre del archivo

    Args:
        nombre_archivo (str): archivo a obtener path

    Returns:
        str: path
    """
    import os
    direccion_actual = os.path.dirname(__file__)
    return os.path.join(direccion_actual, nombre_archivo)

def obtener_lista_movies(nombre_archivo: str)-> list:
    """Obtiene una lista de un archivo scv que le pasamos 

    Args:
        nombre_archivo (str): nombre del archivo del cual queremos obtener la lista

    Returns:
        list: lista de diccionarios
    """
    with open(get_path_actual(nombre_archivo), "r", encoding = "utf-8") as archivo:
        lista = []
        archivo.readline()
        
        for linea in archivo.readlines():
            movie = {}
            linea = linea.strip("\n").split(",")

            id, titulo, genero, rating = linea
            movie["id"] = int(id)
            movie["titulo"] = titulo
            movie["genero"] = genero
            movie["rating"] = float(rating)
            lista.append(movie)

        return lista
#2  
def mostrar_movies(lista_movies: list)-> None:
    """Muestra una lista de peliculas

    Args:
        lista_movies (list): lista de peliculas a mostrar
    """
    tam = len(lista_movies)
    print()
    print("ID           Titulo                       Genero        Rating")
    print("---------------------------------------------------------------")
    for i in range(tam):
        mostrar_movies_item(lista_movies[i])
    print()

def mostrar_movies_item(una_movie: dict):
    """Muestra los key de un diccionario

    Args:
        una_movie (dict): diccionario a mostrar
    """
    print(f"{una_movie['id']:<4}     {una_movie['titulo']:<30}  {una_movie['genero']:<14}  {una_movie['rating']:.2f}")

#3
def asignar_rating(lista_movies: list):
    """Recorre la lista de peliculas asignado ratings

    Args:
        lista_movies (list): lista de diccionario a asignar ratings
    """
    from random import randint
    for el in lista_movies:
        el["rating"] = randint(1, 100) / 10


def mostrar_datos(lista_movies:list, dato:str):
    """Recorre la lista de peliculas y muestra el titulo y el dato de cada una

    Args:
        lista_movies (list): lista de peliculas a recorrer
        dato (str): dato a mostrar junto al titulo
    """
    print(f"Titulo                               {dato.capitalize()}")
    for el in lista_movies:
        print(f"{el['titulo']:<30}       {el[dato]}")
        
#4
def asignar_genero(lista_movies:list):
    """Recorre la lista de peliculas y les asigna un genero entre 4 al azar

    Args:
        lista_movies (list): Lista de peliculas a recorrer para asignar genero
    """
    from random import randint
    for el in lista_movies:
        aux = randint(1, 4)
        match aux:
            case 1:
                el["genero"] = "drama"
            case 2:
                el["genero"] = "comedia"
            case 3:
                el["genero"] = "accion"
            case 4:
                el["genero"] = "terror"

#5
def filtrar_movies(genero:str, lista_movies: list)-> list:
    """Recibe una lista de peliculas y devuelve una nueva con peliculas del genero pasado por parametro

    Args:
        genero (str): Genero por el cual queremos que filtre
        lista_movies (list): Lista de peliculas a filtrar

    Returns:
        list: Nueva lista filtrada
    """
    lista_filtrada = []
    for el in lista_movies:
        if el["genero"] == genero:
            lista_filtrada.append(el)
    return lista_filtrada

def crear_archivo_generos(lista_movies: list, nombre_archivo: str):
    """Escribre la lista de peliculas que le pasemos a un archivo scv

    Args:
        lista_movies (list): Lista a escribir en el archivo scv
        nombre_archivo (str): Nombre del archivo donde vamos a escribir la lista
    """
    with open(get_path_actual(nombre_archivo), "w", encoding = "utf-8") as archivo:
        encabezado = ",".join(list(lista_movies[0].keys())) + "\n"
        archivo.write(encabezado)
        
        for persona in lista_movies:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
            
            linea = ",".join(l) + "\n"
            archivo.write(linea) 

#6
def swap_lista(lista: list, i:int, j:int)-> None:
    """Intercambia valores de i a j

    Args:
        lista (list): lista de los elemetos i y j
        i (int): elemento uno
        j (int): elemento dos
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordenar_movies(lista_movies: list, campo: str):
    """Ordena los elementos de una lista de manera descendente

    Args:
        lista_movies (list): lista de peliculas a recorrer y comparar sus elementos
        campo (str): campo a tener en cuenta para ordenar
    """
    tam = len(lista_movies)
    for i in range(tam - 1):
        for j in range(i + 1, tam):            
            if lista_movies[i][campo] < lista_movies[j][campo]:
                swap_lista(lista_movies, i, j)                

def ordenar_movies_rating(lista_movies: list, campo:str, campo_2:str)-> list:
    """Filtra por campo y ordena los elementos de manera descendente

    Args:
        lista_movies (list): lista a filtrar
        campo (str): campo a filtrar
        campo_2 (str): campo a ordenar 

    Returns:
        list: Nueva lista filtrada y ordenada
    """
    lista_filtrada = filtrar_movies(campo, lista_movies)
    ordenar_movies(lista_filtrada, campo_2)
    return lista_filtrada
       
#7
def obtener_mejor_dato(lista_movies: list, dato: str)-> dict:
    """Recorre la lista de peliculas y obtiene la pelicula con major dato

    Args:
        lista_movies (list): lista a recorrer 
        dato (str): dato a encotrar su maximo

    Returns:
        dict: pelicula con el mejor dato
    """
    pelicula = None
    mayor_rating = 0
    flag_mayor_rating = True
    for el in lista_movies:
        if flag_mayor_rating or el[dato] > mayor_rating:
            mayor_rating = el[dato]
            pelicula = el
            flag_mayor_rating = False
    return pelicula

def mostrar_nombre_dato(pelicula: dict, dato: str):
    """Recibe una pelicula y muestra su titulo y el dato recibido

    Args:
        pelicula (dict): Pelicula a mostrar
        dato (str): dato a mostrar
    """
    print(f"Pelicula con mejor {dato.capitalize()}")
    print(f"Titulo: {pelicula['titulo'].capitalize()} | {dato.capitalize()}: {pelicula[dato]}")
    
#8
def crear_json(pelicula: dict, nombre_archivo: str):
    """Escribe los datos de una pelicula en un archivo JSON

    Args:
        pelicula (dict): pelicula a escribir en el archivo JSON
        nombre_archivo (str): nombre del archivo donde vamos a escribir
    """
    import json
    with open(get_path_actual(nombre_archivo), "w", encoding = "utf-8") as archivo:
        json.dump(pelicula, archivo, indent = 4)
        
