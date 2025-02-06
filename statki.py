
running = True

plansza = ["-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",
           "-","-","-","-","-","-","-","-","-",]

def PokazPlanszy(plansza):
    print(end="|")
    for i in range(1,82):
        print(plansza[i - 1 ],end="|")
        if i%9 == 0 :
            print()
            if i != 81:
                print(end="|")

Lista = ["OO","OO","OOO","OOO","OOOO","OOOOO"]


def Ustawianie(Lista):
    print("Twoje Statki: ")
    for i in range(0,len(Lista) ):
        print(Lista[i])
    rząd = int(input("podaj rząd (od 1 do 9)"))
    kolumna = int(input("podaj kolumnę (od 1 do 9)"))
    plansza[(rząd - 1) * 9 + kolumna - 1] = "O"
    Lista.pop(0)
    kierunek = input("kierunek N E S W: ")
    
    
    


while running:
    PokazPlanszy(plansza)
    Ustawianie(Lista)
