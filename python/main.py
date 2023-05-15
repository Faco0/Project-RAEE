# Progetto svolto da Facoetti, Brignoli e Panseri
from data import ListaR, Lista10
import json

Elenco={
    "Grande Bianco Freddo": {"Grandi elettrodomestici": []},
    "Grande Bianco non Freddo": {"Grandi elettrodomestici": []},
    "TV Monitor a tubo catodico": [],
    "Elettronica di consumo": {
        "Apparecchiature informatiche e per telecomunicazioni": [],
        "Apparecchiature di consumo e pannelli fotovoltaici": [],
        "Apparecchiature di illuminazione": [],
        "Utensili elettrici ed elettronici": [],
        "Giocattoli e apparecchiature per il tempo libero e lo sport": [],
        "Dispositivi medici": [],
        "Strumenti di monitoraggio e di controllo": [],
        "Piccoli elettrodomestici": [],
        "Distributori automatici": []
    },
    "Sorgenti luminose a scarica": {
        "Lampade fluorescenti": [],
        "Sorgenti luminose compatte": [],
    }
}


def menu():
    while True:
        print('''\nMenu di scelta:')
1-Aggiungi elemento
2-Elimina un elemento
3-Modifica un elemento
4-Salva dati su file
5-Carica dati da file
6-Visualizza elenco
7-Visualizza le fonti
8-Esci''')

        try:
            scelta=int(input('\nInserisci la tua scelta: '))
            return scelta
        except:
            print('\nErrore Input: formato scelta incorretto (NotInt)')

def aggiungi():
    controllo = False
    while True:
        try:
            print("\nRaggruppamenti disponibili:", ListaR)
            rag=str(input("\nInserisci il raggruppamento dove inserirai il rifiuto: "))
            if rag not in ListaR:
                continue
            break
        except:
            print("\nErrore!")
    while True:
        try:
            #fare il controllo per la categoria (deve essere presente nel raggruppamento!!!)
            break
        except:
            print("\nErrore!")
            
    controllo = True
    return controllo

def rimuovi():
    controllo = False
    if Elenco=={"Grande Bianco Freddo": {"Grandi elettrodomestici": []},"Grande Bianco non Freddo": {"Grandi elettrodomestici": []},"TV Monitor a tubo catodico": [],"Elettronica di consumo": {"Apparecchiature informatiche e per telecomunicazioni": [],"Apparecchiature di consumo e pannelli fotovoltaici": [],"Apparecchiature di illuminazione": [],"Utensili elettrici ed elettronici": [],"Giocattoli e apparecchiature per il tempo libero e lo sport": [],"Dispositivi medici": [],"Strumenti di monitoraggio e di controllo": [],"Piccoli elettrodomestici": [],"Distributori automatici": []},"Sorgenti luminose a scarica": {"Lampade fluorescenti": [],"Sorgenti luminose compatte": [],}}:
        print("\nELENCO VUOTO")
        return controllo
    controllo = True
    return controllo

def modifica():
    controllo = False
    if Elenco=={"Grande Bianco Freddo": {"Grandi elettrodomestici": []},"Grande Bianco non Freddo": {"Grandi elettrodomestici": []},"TV Monitor a tubo catodico": [],"Elettronica di consumo": {"Apparecchiature informatiche e per telecomunicazioni": [],"Apparecchiature di consumo e pannelli fotovoltaici": [],"Apparecchiature di illuminazione": [],"Utensili elettrici ed elettronici": [],"Giocattoli e apparecchiature per il tempo libero e lo sport": [],"Dispositivi medici": [],"Strumenti di monitoraggio e di controllo": [],"Piccoli elettrodomestici": [],"Distributori automatici": []},"Sorgenti luminose a scarica": {"Lampade fluorescenti": [],"Sorgenti luminose compatte": [],}}:
        print("\nELENCO VUOTO")
        return controllo
    controllo = True
    return controllo

def salvaDati():
    controllo = False
    if Elenco=={"Grande Bianco Freddo": {"Grandi elettrodomestici": []},"Grande Bianco non Freddo": {"Grandi elettrodomestici": []},"TV Monitor a tubo catodico": [],"Elettronica di consumo": {"Apparecchiature informatiche e per telecomunicazioni": [],"Apparecchiature di consumo e pannelli fotovoltaici": [],"Apparecchiature di illuminazione": [],"Utensili elettrici ed elettronici": [],"Giocattoli e apparecchiature per il tempo libero e lo sport": [],"Dispositivi medici": [],"Strumenti di monitoraggio e di controllo": [],"Piccoli elettrodomestici": [],"Distributori automatici": []},"Sorgenti luminose a scarica": {"Lampade fluorescenti": [],"Sorgenti luminose compatte": [],}}:
        while True:
            try:
                scelta=str(input("\nElenco vuoto, sei sicuro di voler sovrascrivere il file dati? (si/no) ")).lower()
                match scelta:
                    case "si":
                        break
                    case "no":
                        return controllo
                    case "_":
                        print("\nScelta errata!")
                        continue
            except:
                print("\nInput errato!")
    try:
        with open(".\python\elenco.json", 'w') as file:
            json.dump(Elenco, file, indent=4)
        controllo = True
        return controllo
    except:
        print('\nErrore SalvaDati!')

def caricaDati():
    controllo = False
    try:
        global Elenco
        with open(".\python\elenco.json", 'r') as file:
            Elenco=json.load(file)
        controllo = True
        return controllo
    except:
        print('\nErrore CaricaDati: File Archivio non esistente!')
        return controllo

def main():
    print("[INIZIO PROGRAMMA!]")
    while True:
        scelta = menu()
        while True:
            match scelta:
                case 1:
                    print("\n[AGGIUNTA ELEMENTO]")
                    aggiungi()
                    print("\n[ELEMENTO AGGIUNTO CON SUCCESSO!]")
                    break
                case 2:
                    print("\n[RIMUOVI ELEMENTO]")
                    controllo = rimuovi()
                    if controllo == False:
                        pass
                    else:
                        print("\n[ELEMENTO RIMOSSO CON SUCCESSO!]")                 
                    break
                case 3:
                    print("\n[MODIFICA ELEMENTO]")
                    controllo = modifica()
                    if controllo == False:
                        pass
                    else:
                        print("\n[ELEMENTO MODIFICATO CON SUCCESSO!]")
                    break
                case 4:
                    print("\n[SALVA ELENCO]")
                    controllo = salvaDati()
                    if controllo == False:
                        pass
                    else:
                        print("\n[ELENCO SALVATO CON SUCCESSO!]")
                    break
                case 5:
                    print("\n[CARICA ELENCO]")
                    controllo = caricaDati()
                    if controllo == False:
                        pass
                    else:
                        print("\n[ELENCO CARICATO CON SUCCESSO!]")
                    break
                case 6:
                    
                    break
                case 7:
                    print("\nElenco delle fonti:")
                    print("Dlgs n.49/2014: https://www.governo.it/sites/governo.it/files/75158-9343.pdf")
                    break
                case 8:
                    print("\n[USCITA PROGRAMMA]")
                    quit()
                case _:
                    print('\nErrore Input: scelta non compresa tra 1 e 8!')
                    break

main()