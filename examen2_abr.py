#  === BIBLIOTECA ===
#  Desarrolla un programa en Python que gestione un sistema de biblioteca.No hace falta que
#  comentes cada cosa que realices pero sí lo que consideres debería saber otro compañero
#  tuyo, para cuando te vayas de vacaciones y tu compañero debe manipular tu código.

from abc import ABC,abstractmethod  #? Importación para Abstracción de Clase

#* FUNCIONES ---------------------------------------------------------------------

#? GENERAR ESTADÍSTICAS - Genera la estadísticas de la BIBLIOTECA
def generarEstadisticas(biblioteca:dict):

    print("\n--- BIBLIOTECA: Estadísticas ---\n")

    #Total de materiales registrados.
    print("Número de Materiales registrados:",len(biblioteca))

    #Número de libros y revistas.
    libros = 0
    revistas = 0
    for key in biblioteca:
        if(isinstance(biblioteca[key],Libro)):
            libros += 1
        elif(isinstance(biblioteca[key],Revista)):
            revistas +=1
    print("Número de Libros registrados:",libros)
    print("Número de Revistas registradas:",revistas)

    #Promedio de páginas para los libros.
    totalPaginas = 0
    for key in biblioteca:
        if(isinstance(biblioteca[key],Libro)):
            totalPaginas += biblioteca[key].paginas
    print("Promedio de Páginas en Libros:",(totalPaginas / libros))

#? LISTAR BIBLIOTECA - Lista los Materiales de la BIBLIOTECA
def listarBiblioteca(biblioteca:dict):
    print("\n--- Listado de BIBLIOTECA ---\n")
    for key in biblioteca:
        print(biblioteca[key])

#? NUM CHECK - Comprueba que el dato introducido por teclado es un número
def numCheck(mensaje:str, variable:str) -> int:
    isNum = False
    while(isNum is False):
        try:
            print(mensaje)
            num = int(input(variable))
            isNum = True
        except ValueError:
            print("No se ha introducido un número, inténtelo de nuevo.")
    return num

#? BOOLEAN CHECK - Devuelve true si la respuesta es SI y false si la respuesta es NO
def booleanCheck(mensaje:str) -> bool:
    resultado : bool = False
    flag : bool = False
    while(flag is False):
        print(mensaje)
        respuesta = input("Respuesta: ")
        if((respuesta.lower() == "si") or (respuesta.lower() == "sí")):
            resultado = True
            flag = True
        elif(respuesta.lower() == "no"):
            resultado = False
            flag = True
        else:
            print("Respuesta no válida, inténtelo de nuevo.")
            flag = False
    return resultado

#? TYPE CHECK - Devuelve True si la respuesta es LIBRO y False si la respuesta es REVISTA
def typeCheck(mensaje:str) -> bool:
    resultado : bool = False
    flag : bool = False
    while(flag is False):
        print(mensaje)
        respuesta = input("Respuesta: ")
        if((respuesta.lower() == "libro")):
            resultado = True
            flag = True
        elif(respuesta.lower() == "revista"):
            resultado = False
            flag = True
        else:
            print("Respuesta no válida, inténtelo de nuevo.")
            flag = False
    return resultado

#? SELECT LIST - Devuelve el índice seleccionado de la Lista introducida por parámetro
def selectList(lista:list,mensaje:str,variable:str) -> int:
    indice = -1
    while((indice < 0) or (indice > (len(lista)-1))):
        for element in lista:
            print(f'{lista.index(element)}. {element}',end="\t")
        print("")
        indice = numCheck(mensaje,variable)
        if((indice < 0) or (indice > (len(lista)-1))):
            print("ERROR: Opción introducida inválida. Inténtelo de nuevo.")
    return indice

#* -------------------------------------------------------------------------------

#? 1. Define una clase base Material que tenga atributos comunes a todos los materiales de la biblioteca

class Material(ABC):

    # ---   CONSTRUCTOR
    @abstractmethod
    def __init__(self, id:int, titulo:str, autor:str, anyo:int):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo
    
    def __str__(self):
        return f"{self.__class__.__name__.upper()}\tID: {self.id}\tTítulo: {self.titulo}\tAutor: {self.autor}\tAño de Publicación: {self.anyo}"

#? 2.Crea dos clases que hereden de Material:
#*   Libro: Incluye atributos adicionales como género (debe seleccionarse entre una lista
#*   predefinida: "Ficción", "No Ficción", "Terror", "Ciencia") y número de páginas (debe ser mayor a 0).

generos = ["FICCIÓN","NO FICCIÓN","TERROR","CIENCIA"]

class Libro(Material):
    def __init__(self,id:int,titulo:str,autor:str,anyo:int,genero:str,paginas:int):
        super().__init__(id,titulo,autor,anyo)
        if(genero.upper() not in generos): raise Exception("El campo GÉNERO debe contener un género válido.")
        if(paginas <= 0): raise Exception("El campo PÁGINAS debe ser mayor que 0.")
        self.genero = genero
        self.paginas = paginas

    def __str__(self):
        return super().__str__() + f"\tGénero: {self.genero}\tNúmero de Páginas: {self.paginas} {"página" if self.paginas == 1 else "páginas"}"

#*   Revista: Incluye atributos adicionales como número de edición y mes de publicación (debe
#*   seleccionarse entre los meses válidos: "Enero", "Febrero", ..., "Diciembre")

meses = ["ENERO","FEBERERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"]

class Revista(Material):
    def __init__(self,id:int,titulo:str,autor:str,anyo:int,edicion:int,mes:str):
        super().__init__(id,titulo,autor,anyo)
        if(mes.upper() not in meses): raise Exception("El campo MES debe contener un mes válido.")
        self.edicion = edicion
        self.mes = mes
    
    def __str__(self):
        return super().__str__() + f"\tEdición: {self.edicion}\tMes de Publicación: {self.mes}"

#? 3.Utiliza un diccionario para almacenar los materiales, donde la clave sea el id y el valor sea un objeto de tipo Libro o Revista. 

biblioteca : dict = {
    1 : Libro(1,"El Faro Maldito","Carlos Ruis Zafrán",2005,"Terror",200),
    2 : Revista(2,"Muy Curioso","Editorial Carlos Haya",2020,5,"Junio"),
    3 : Libro(3,"Luces de Enero","Sebastián de la Fuente",1987,"No Ficción",200),
    4 : Revista(4,"Revista Dibus!","Editorial Comic Rayo",2010,1,"Diciembre"),
    5 : Libro(5,"Diciembre","Noelle Dreemurr Caskell",2024,"Ficción",500)
}

#? 4.Mantén una lista de todos los id existentes para verificar que no se repitan al agregar nuevos materiales.

idList = []
for id in biblioteca:
    idList.append(id)

#? 5. Generar Estadísticas:debe devolver todos estos valores

generarEstadisticas(biblioteca)

#? 6.Implementa un menú que permita al usuario realizar las siguientes acciones:
respuesta = ""
while(respuesta.lower() != "f"):
    print("\n=== EXÁMEN PYTHON - Biblioteca ===\n"
                  +"\na) Agregar MATERIAL"
                  +"\nb) Listar MATERIALES"
                  +"\nc) Buscar MATERIAL por ID"
                  +"\nd) Eliminar MATERIAL"
                  +"\ne) Generar Estadísticas"
                  +"\nf) Salir del programa")
    print("Introduzca la opción a ejecutar")
    respuesta = input("Opción: \n")
    match(respuesta.lower()):
        case("a"):                                                      #* Agregar Material: Permite al usuario agregar un nuevo Libro o Revista.
            print("--- Agregar nuevo MATERIAL ---\n")
            idTaken = True
            while(idTaken):
                nuevoID = numCheck("Introduzca la ID del nuevo MATERIAL","ID:")
                if(nuevoID in idList):
                    print("ERROR: La ID introducida ya está registrada. Inténtelo de nuevo.")
                else:
                    idTaken = False
            print("Introduzca el TÍTULO del nuevo MATERIAL")
            nuevoTitulo = input("Título:")
            print("Introduzca el AUTOR del nuevo MATERIAL")
            nuevoAutor = input("Autor:")
            nuevoAnyo = numCheck("Introduzca el AÑO DE PUBLICACIÓN del nuevo MATERIAL","Año:")
            if(typeCheck("Introduzca el tipo de MATERIAL que desea crear (LIBRO / REVISTA)")):
                nuevoGenero = selectList(generos,"Introduzca el índice del GÉNERO del nuevo LIBRO","Género:")
                nuevoPaginas = numCheck("Introduzca el NÚMERO DE PÁGINAS del nuevo LIBRO","Páginas:")
                try:
                    nuevoLibro = Libro(nuevoID,nuevoTitulo,nuevoAutor,nuevoAnyo,generos[nuevoGenero],nuevoPaginas)
                    biblioteca[nuevoID] = nuevoLibro
                    print("\n--- LIBRO añadido a BIBLIOTECA ---\n\n",biblioteca[nuevoID])
                    idList.append(nuevoID)
                except Exception:
                    print("\nHa ocurrido un error al crear el LIBRO, inténtelo de nuevo.")
            else:
                nuevoEdicion = numCheck("Introduzca la EDICIÓN de la nueva REVISTA","Edición:")
                nuevoMes = selectList(meses,"Introduzca el índice del MES DE PUBLICACIÓN de la nueva REVISTA","Mes:")
                try:
                    nuevoRevista = Revista(nuevoID,nuevoTitulo,nuevoAutor,nuevoAnyo,nuevoEdicion,meses[nuevoMes])
                    biblioteca[nuevoID] = nuevoRevista
                    print("\n--- REVISTA añadida a BIBLIOTECA ---\n\n",biblioteca[nuevoID])
                    idList.append(nuevoID)
                except Exception:
                    print("\nHa ocurrido un error al crear la REVISTA, inténtelo de nuevo.")  
        case("b"):                                                      #* Listar Materiales: Muestra una lista de todos los materiales registrados con sus detalles. 
            if(len(biblioteca) > 0):
                listarBiblioteca(biblioteca)
            else:
                print("\nERROR: La BIBLIOTECA no contiene ningún registro.")
        case("c"):                                                      #* Buscar Material por ID: Permite al usuario buscar un material específico por su id.
            if(len(biblioteca) > 0):
                idBuscar = numCheck("\nIntroduzca la ID del MATERIAL a BUSCAR.","ID:")
                if(idBuscar in biblioteca):
                    print("\n--- MATERIAL encontrado ---\n")
                    print(biblioteca[idBuscar])
                else:
                    print("ERROR: La ID introducida no está registrada en la BIBLBIOTECA.")
            else:
                print("\nERROR: La BIBLIOTECA no contiene ningún registro.")
        case("d"):                                                      #* Eliminar Material: Elimina un material específico usando su id.
            if(len(biblioteca) > 0):
                idEliminar = numCheck("\nIntroduzca la ID del MATERIAL a ELIMINAR.","ID:")
                if(idEliminar in biblioteca):
                    print("\n--- MATERIAL encontrado ---\n")
                    print(biblioteca[idEliminar])
                    if(booleanCheck("\n¿Está seguro de que desea ELIMINAR este MATERIAL? (SI/NO)")):
                        del biblioteca[idEliminar]
                        del idList[idList.index(idEliminar)]
                    else:
                        print("Operación cancelada. Volviendo al Menú Principal ...")
                else:
                    print("ERROR: La ID introducida no está registrada en la BIBLBIOTECA.")
            else:
                print("\nERROR: La BIBLIOTECA no contiene ningún registro.")
        case("e"):                                                      #* Generar Estadísticas
            if(len(biblioteca) > 0):
                generarEstadisticas(biblioteca)
            else:
                print("\nERROR: La BIBLIOTECA no contiene ningún registro.")
        case("f"):                                                      #! Salir: Termina la ejecución del programa.
            print("Saliendo del Programa ...")
        case _:                                                         #! Input Error
            print("Opción introducida no válida, inténtelo de nuevo.")
