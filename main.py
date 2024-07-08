from funciones_parcial import *
import os

while True:
    os.system("cls")
    
    match menu():
        case "1":
            os.system("cls")
            lista_movies = obtener_lista_movies("movies.csv")
            print("Lista de peliculas cargada")

        case "2":
            os.system("cls")
            try:
                mostrar_movies(lista_movies)
            except:
                print("No se cargo la lista de peliculas")
                
        case "3":
            os.system("cls")
            try:
                asignar_rating(lista_movies)
                mostrar_datos(lista_movies, "rating")
            except:
                print("No se cargo la lista de peliculas")

        case "4":
            os.system("cls")
            try: 
                asignar_genero(lista_movies)
                mostrar_datos(lista_movies, "genero")
            except:
                print("No se cargo la lista de peliculas")

        case "5":
            os.system("cls")
            try:
                lista_filtrada= filtrar_movies("comedia", lista_movies)
                crear_archivo_generos(lista_filtrada, "comedias.csv")
                print("Archivo SCV creado con lista filtrada por genero")
            except:
                print("No se cargo la lista de peliculas")

        case "6":
            os.system("cls")
            try:
                lista_terror = ordenar_movies_rating(lista_movies, "terror", "rating")
                lista_comedia = ordenar_movies_rating(lista_movies, "comedia", "rating")
                lista_drama = ordenar_movies_rating(lista_movies, "drama", "rating")
                lista_accion = ordenar_movies_rating(lista_movies, "accion", "rating")
                mostrar_movies(lista_terror)
                mostrar_movies(lista_comedia)
                mostrar_movies(lista_drama)
                mostrar_movies(lista_accion)
            except:
                print("No se cargo la lista de peliculas")

        case "7":
            os.system("cls")
            try:
                movie = obtener_mejor_dato(lista_movies, "rating")
                mostrar_nombre_dato(movie, "rating")
            except:
                print("No se cargo la lista de peliculas")

        case "8":
            os.system("cls")
            try:
                crear_json(movie, "mejor_rating.json")
            except:
                print("No se cargo la lista de peliculas")

        case "9":
            os.system("cls")   
            break
           
    os.system("pause")