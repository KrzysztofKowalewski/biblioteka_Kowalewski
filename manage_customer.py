import csv
import random
from datetime import date


def addcustomer(cust_id,name,email,phone,created,updated,street,city,country):
    with open('biblio/customer.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([cust_id,name,email,phone,created,updated])
    with open('biblio/address.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([cust_id,street,city,country])
    with open(f'biblio\database\{cust_id}.txt', mode='w') as cust_book_info_file:
        print(f"Utworzono plik {cust_id}.txt")
       

def rent_book(cust_id,book_title):
    file_content = []
    with open(f'biblio\database\{cust_id}.txt', mode='r') as cust_book_info_file:
        # Odczytanie pierwszej linii
        linia = cust_book_info_file.readline()
    
        # Pętla czytająca linie, aż do końca pliku (gdy linia jest pusta)
        while linia:
            # Wyświetlenie odczytanej linii (bez dodatkowego znaku nowej linii)
            linia = linia.rstrip()
            file_content.append(linia)
            
            # Odczytanie kolejnej linii
            linia = cust_book_info_file.readline()
        print(file_content)
    with open(f'biblio\database\{cust_id}.txt', mode='w') as cust_book_info_file:
        if file_content == ['']:
            cust_book_info_file.write(f'{str(book_title)}')
        else:
            for i in file_content:
                cust_book_info_file.write(f'{i} \n')
            cust_book_info_file.write(f'{str(book_title)}')     

def rent_books(cust_id,book_titles):
    file_content = []
    with open(f'biblio\database\{cust_id}.txt', mode='r') as cust_book_info_file:
        # Odczytanie pierwszej linii
        linia = cust_book_info_file.readline()
    
        # Pętla czytająca linie, aż do końca pliku (gdy linia jest pusta)
        while linia:
            # Wyświetlenie odczytanej linii (bez dodatkowego znaku nowej linii)
            linia = linia.rstrip()
            file_content.append(linia)
            
            # Odczytanie kolejnej linii
            linia = cust_book_info_file.readline()
        print(file_content)
    with open(f'biblio\database\{cust_id}.txt', mode='w') as cust_book_info_file:
        if file_content == ['']:
            for book in book_titles:
                cust_book_info_file.write(f'{str(book)} \n')
        else:
            for i in file_content:
                cust_book_info_file.write(f'{i} \n')
            for book in book_titles:
                cust_book_info_file.write(f'{str(book)} \n')   


def delcust_id(del_id):
    try:
        with open('biblio\customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            lines = list(reader)
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return
    
    updated_lines = [line for line in lines if line[0] != str(del_id)]
    
    try:
        with open('biblio\customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_lines)
        print(f"Linia z ID {del_id} została usunięta z pliku.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")

def delcust_name(del_name):
    try:
        with open('biblio\customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            lines = list(reader)
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return
    
    updated_lines = [line for line in lines if line[1] != str(del_name)]
    
    try:
        with open('biblio\customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_lines)
        print(f"Linia z tytułem {del_name} została usunięta z pliku.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")


def return_book(cust_id, book_title):
    file_content = []
    with open(f'biblio\database\{cust_id}.txt', mode='r') as cust_book_info_file:
        # Odczytanie pierwszej linii
        linia = cust_book_info_file.readline()
    
        # Pętla czytająca linie, aż do końca pliku (gdy linia jest pusta)
        while linia:
            # Wyświetlenie odczytanej linii (bez dodatkowego znaku nowej linii)
            linia = linia.rstrip()
            file_content.append(linia)
            
            # Odczytanie kolejnej linii
            linia = cust_book_info_file.readline()
        print(file_content)
    
    with open(f'biblio\database\{cust_id}.txt', mode='w') as cust_book_info_file:
            for i in file_content:
                if i != book_title:
                    cust_book_info_file.write(f'{i} \n')



            
        
    