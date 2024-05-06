import csv
from globals import reading
def delbook_id(del_id):
    try:
        with open('biblio/book.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            lines = list(reader)
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return
    
    updated_lines = [line for line in lines if line[0] != str(del_id)]
    
    try:
        with open('biblio/book.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_lines)
        print(f"Linia z ID {del_id} została usunięta z pliku.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")

def delbook_title(del_title):
    try:
        with open('biblio/book.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            lines = list(reader)
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return
    
    updated_lines = [line for line in lines if line[2] != str(del_title)]
    
    try:
        with open('biblio/book.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_lines)
        print(f"Linia z tytułem {del_title} została usunięta z pliku.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")
    
