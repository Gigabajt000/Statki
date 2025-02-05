
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
    for i in range(1,82):
        print(plansza[i - 1 ],end="|")
        if i%9 == 0:
            print()

Lista = ["O O","O O","O O O","O O O","O O O O","O O O O O"]
liczba_statkow = 6

def Ustawianie(liczba_statkow):
    for i in range(0,liczba_statkow + 1):
        print(Lista[i])
    rząd = int(input("podaj rząd (od 1 do 9)"))
    kolumna = int(input("podaj kolumnę (od 1 do 9)"))
    plansza[rząd * 9 + kolumna - 1] = "O"
    

Ustawianie(liczba_statkow)
while running:
    PokazPlanszy(plansza)
