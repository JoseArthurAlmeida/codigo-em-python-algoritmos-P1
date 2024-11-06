pais = input("Digite um país: ")

# if pais == "Brasil":
#     print("Toque o hino do Brasil")
# elif pais == "Italia":
#     print("Toque o hino do Italia")
# elif pais == "Japao":
#     print("Toque o hino do Japao")
# else:
#     print("Toque o hino da Argentina")

match(pais):
    case "Brasil":
        print("Toque o hino do Brasil")
    case "Italia":
        print("Toque o hino do Italia")
    case "Japao":
        print("Toque o hino do Japao")
    case _ :
        print("Toque o hino da Argentina")