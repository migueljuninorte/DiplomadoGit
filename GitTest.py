
option = (input ("Ingrese su nombre: "))

if option == "Miguel Jimenez":
    #Insert code here
    print("Opción 1")

if option == "":
    #Insert code here
    print("")

option = (input ("Ingrese su nombre"))

if option == "Deivid Guauña":
    #Insert code here
    print("option")

if option == "Jesus Gonzalez":
    name = option.split()
    print(name)
    print("El cambio en primera")

if option == "Stiven bustamante":
    def responseSuccess(results, message, row_total, title=None, statusCode=200):
        return {
            'success':True,
            'title': title,
            'message':message,
            'results':results,
            'rowTotal':row_total,
            'status': statusCode
        }
