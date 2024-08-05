import numpy as np
import pandas as pd

data = { 
    "Kuru otlar Üstüne" : ["Nuri Bilge Ceylan", "2023", "Deniz Celiloğlu", "Merve Dizdar"],
    "Yeralti" : ["Zeki Demirkubuz", "2012", "Engin Günaydin", "Nihal Yalcin"],
    "Kurak Günler" : ["Emin Alper", "2022", "Selahattin Pasali", "Ekin Koc"]
}
# "key" (film adı) : "value" [(yönetmen), "gösterim yılı", "birinci oyuncu", "ikinci oyuncu"]

def display_film_list():
    film_lib = pd.DataFrame.from_dict(data, orient='index', columns=["Yönetmen", "Gösterim Yılı", "Birinci Oyuncu", "İkinci Oyuncu"])
    print(film_lib)

def menu():
    menu_list = [
        "Filme göre", "Yönetmene göre", "Oyuncuya göre", "Yayınlanma yılına göre",
        "Film listesi üzerinden", "Rastgele", "Bulunduğun ayda vizyona girmiş filmler",
        "Mevsime göre filmler", "Ünlülerin önerileri"
    ]
    print("Pitirflix'e hoş geldiniz. \n----------------------------------------")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item}")

def main():
    menu()
    choice = input("Which recommendation do you want? (Enter the number): ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 5:
            display_film_list()
        else:
            print("This feature is not implemented yet.")
    else:
        print("Invalid input. Please enter a number.")

main()
