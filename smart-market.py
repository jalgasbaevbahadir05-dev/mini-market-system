## Smart Market Terminal v1.0
# Avtor: [Jalg'asbaev Bahadir]
def market_sistemasi():
    sklad = ["alma", "kartoshka", "anar", "piyaz", "limon"]
    mugdar = {"alma": 30, "kartoshka": 20, "anar": 0, "piyoz": 25, "limon": 5} # "anar" o'rniga "anar" (lug'atda ham bir xil bo'lsin)
    pul = {"alma": 5000, "kartoshka": 4000, "anar": 10000, "piyaz": 2000, "limon": 20000}
    
    buyirtpalar = []
    jami = 0
    
    for i in range(3):
        onim = input(f"{i+1}-ónimdi kiritiñ:\n-->")
        buyirtpalar.append(onim.lower())
    
    print("\n--- Tekseriw nátiyjesi ---")
    
    for onim in buyirtpalar:
        if onim in sklad:
            if mugdar[onim] > 0:
                print(f"{onim.title()} bizde bar. Bahası: {pul[onim]} sum")
                jami += pul[onim]
                mugdar[onim] -= 1
            else:
                print(f" Keshiresiz, búginshe {onim.title()} bizde joq (tawsılǵan)")
        else: 
            print(f" Keshiresiz, bizde {onim.title()} degen ónim joq")
            
    print("-" * 30)
    print(f"Tólem ushın jámi: {jami} sum tóleysiz")

market_sistemasi()