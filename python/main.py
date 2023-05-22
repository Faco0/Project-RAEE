# Progetto svolto da Facoetti, Brignoli e Panseri
from data import ListaR, Lista10
import json

Elenco={
    "Grande Bianco Freddo": {"Grandi Elettrodomestici": []},
    "Grande Bianco Non Freddo": {"Grandi Elettrodomestici": []},
    "Tv Monitor A Tubo Catodico": [],
    "Elettronica Di Consumo": {
        "Apparecchiature Informatiche E Per Telecomunicazioni": [],
        "Apparecchiature Di Consumo E Pannelli Fotovoltaici": [],
        "Apparecchiature Di Illuminazione": [],
        "Utensili Elettrici Ed Elettronici": [],
        "Giocattoli E Apparecchiature Per Il Tempo Libero E Lo Sport": [],
        "Dispositivi Medici": [],
        "Strumenti Di Monitoraggio E Di Controllo": [],
        "Piccoli Elettrodomestici": [],
        "Distributori Automatici": []
    },
    "Sorgenti Luminose A Scarica": {
        "Lampade Fluorescenti": [],
        "Sorgenti Luminose Compatte": [],
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
            rag=str(input("\nInserisci il raggruppamento dove inserirai il rifiuto: ")).title()
            if rag not in ListaR:
                print("\nScelta errata!")
                continue
            break
        except:
            print("\nErrore!")
    while True:
        try:
            if Elenco[rag] == []:
                break
            print("\nCategorie presenti nel raggruppamento", rag + ":", list(Elenco[rag]))
            cat=str(input("\nInserisci la categoria: ")).title()
            if cat not in (Elenco[rag]):
                print("\nScelta errata!")
                continue
            break
        except:
            print("\nErrore!")
    while True:
        try:
            c = True
            rif=str(input("\nInserisci il rifiuto: ")).title()
            if Elenco[rag] == []:
                if rif not in Elenco[rag]:
                    pass
                else:
                    print("\nRifiuto già presente")
                    continue
            else:
                if rif not in Elenco[rag][cat]:
                    pass
                else:
                    print("\nRifiuto già presente")
                    continue
            for i in rif:
                if i in "!|\[]{#@§+*'?^()/&%$}£":
                    print("\nStringa non alfanumerica")
                    c = False
                if c == False:
                    break
            if c == False:
                continue
            else:
                if Elenco[rag] == []:
                    Elenco[rag].append(rif)
                else:
                    Elenco[rag][cat].append(rif)
                break
        except:
            print("\nErrore!")
    controllo = True
    return controllo

def rimuovi():
    controllo = False
    if Elenco=={"Grande Bianco Freddo": {"Grandi Elettrodomestici": []},"Grande Bianco Non Freddo": {"Grandi Elettrodomestici": []},"Tv Monitor A Tubo Catodico": [],"Elettronica Di Consumo": {"Apparecchiature Informatiche E Per Telecomunicazioni": [],"Apparecchiature Di Consumo E Pannelli Fotovoltaici": [],"Apparecchiature Di Illuminazione": [],"Utensili Elettrici Ed Elettronici": [],"Giocattoli E Apparecchiature Per Il Tempo Libero E Lo Sport": [],"Dispositivi Medici": [],"Strumenti Di Monitoraggio E Di Controllo": [],"Piccoli Elettrodomestici": [],"Distributori Automatici": []},"Sorgenti Luminose A Scarica": {"Lampade Fluorescenti": [],"Sorgenti Luminose Compatte": [],}}:
        print("\nELENCO VUOTO")
        return controllo
    while True:
        try:
            print("\nRaggruppamenti disponibili:", ListaR)
            rag=str(input("\nInserisci il raggruppamento dove rimuoverai il rifiuto: ")).title()
            if rag not in ListaR:
                print("\nScelta errata!")
                continue
            break
        except:
            print("\nErrore!")
    while True:
        try:
            if Elenco[rag] == []:
                break
            print("\nCategorie presenti nel raggruppamento", rag + ":", list(Elenco[rag]))
            cat=str(input("\nInserisci la categoria: ")).title()
            if cat not in (Elenco[rag]):
                print("\nScelta errata!")
                continue
            break
        except:
            print("\nErrore!")
    while True:
        try:
            c = True
            rif=str(input("\nInserisci il rifiuto che vuoi rimuovere: (0 se vuoi uscire)")).title()
            if rif == "0":
                break
            else:
                try:
                    if Elenco[rag] == []:
                        Elenco[rag].remove(rif)
                    else:
                        Elenco[rag][cat].remove(rif)
                    break
                except:
                    print("\nRifiuto non presente!")
                    continue
        except:
            print("\nErrore!")
    controllo = True
    if rif == "0":
        controllo = False
    return controllo

def modifica():
    controllo = False
    if Elenco=={"Grande Bianco Freddo": {"Grandi Elettrodomestici": []},"Grande Bianco Non Freddo": {"Grandi Elettrodomestici": []},"Tv Monitor A Tubo Catodico": [],"Elettronica Di Consumo": {"Apparecchiature Informatiche E Per Telecomunicazioni": [],"Apparecchiature Di Consumo E Pannelli Fotovoltaici": [],"Apparecchiature Di Illuminazione": [],"Utensili Elettrici Ed Elettronici": [],"Giocattoli E Apparecchiature Per Il Tempo Libero E Lo Sport": [],"Dispositivi Medici": [],"Strumenti Di Monitoraggio E Di Controllo": [],"Piccoli Elettrodomestici": [],"Distributori Automatici": []},"Sorgenti Luminose A Scarica": {"Lampade Fluorescenti": [],"Sorgenti Luminose Compatte": [],}}:
        print("\nELENCO VUOTO")
        return controllo
    while True:
        try:
            print("\nRaggruppamenti disponibili:", ListaR)
            rag=str(input("\nInserisci il raggruppamento dove modificherai il rifiuto: ")).title()
            if rag not in ListaR:
                print("\nScelta errata!")
                continue
            break
        except:
            print("\nErrore!")
    while True:
        try:
            if Elenco[rag] == []:
                break
            print("\nCategorie presenti nel raggruppamento", rag + ":", list(Elenco[rag]))
            cat=str(input("\nInserisci la categoria: ")).title()
            if cat not in (Elenco[rag]):
                print("\nScelta errata!")
                continue
            break
        except:
            print("\nErrore!")
    while True:
        try:
            c = True
            rif=str(input("\nInserisci il rifiuto che vuoi modificare: (0 se vuoi uscire)")).title()
            if rif == "0":
                break
            rif2=str(input("\nInserisci il nuovo nome del rifiuto: ")).title()
            for i in rif2:
                if i in "!|\[]{#@§+*'?^()/&%$}£":
                    print("\nStringa non alfanumerica")
                    c = False
                if c == False:
                    break
            if c == False:
                continue
            else:
                try:
                    if Elenco[rag] == []:
                        pos=Elenco[rag].index(rif)
                        Elenco[rag][pos] = rif2
                    else:
                        pos=Elenco[rag][cat].index(rif)
                        Elenco[rag][cat][pos] = rif2
                    break
                except:
                    print("\nRifiuto non presente!")
                    continue
        except:
            print("\nErrore!")
    controllo = True
    if rif == "0":
        controllo = False
    return controllo

def salvaDati():
    controllo = False
    if Elenco=={"Grande Bianco Freddo": {"Grandi Elettrodomestici": []},"Grande Bianco Non Freddo": {"Grandi Elettrodomestici": []},"Tv Monitor A Tubo Catodico": [],"Elettronica Di Consumo": {"Apparecchiature Informatiche E Per Telecomunicazioni": [],"Apparecchiature Di Consumo E Pannelli Fotovoltaici": [],"Apparecchiature Di Illuminazione": [],"Utensili Elettrici Ed Elettronici": [],"Giocattoli E Apparecchiature Per Il Tempo Libero E Lo Sport": [],"Dispositivi Medici": [],"Strumenti Di Monitoraggio E Di Controllo": [],"Piccoli Elettrodomestici": [],"Distributori Automatici": []},"Sorgenti Luminose A Scarica": {"Lampade Fluorescenti": [],"Sorgenti Luminose Compatte": [],}}:
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

def stampa_dizionario(dizionario, livello):
    spazi = "  " * livello
    for chiave, valore in dizionario.items():
        if isinstance(valore, dict):
            print(f"{spazi}{chiave}:")
            stampa_dizionario(valore, livello + 1)
        else:
            print(f"{spazi}{chiave}: {valore}")

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
                    stampa_dizionario(Elenco, 0)
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

with open(".\python\elenco.json", 'r') as file:
    Elenco=json.load(file)
main()