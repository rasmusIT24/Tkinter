#Harjutus 3
#Rasmus Ojala
import tkinter as tk

def main():
    aken = tk.Tk()
    aken.title("Tkinderi ülesanded")
    aken.geometry("400x400")
    # Akna suuruse muutja/keelamine
    aken.resizable(False, True)

  # Funktsioon mis kuvab sisestused
    def kuva_sisestus():
        laenusumma = int(sisestus1.get()) #Võtab esimese sisestuse
        kuuintressimäär = float(sisestus2.get())/12/100  # Võtab esimese sisestuse
        maksete_arv = int(sisestus3.get())*12  # Võtab teise sisestuse

        igakuine_makse = laenusumma * kuuintressimäär / (1- (1 + kuuintressimäär) ** -maksete_arv)
        vastus = tk.Label(aken, text=f"{maksete_arv:.2f}")
        vastus.pack()

    # Esimene sisestusväli
    label = tk.Label(aken, text="Laenusumma (€)").pack()
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
   
    # Teine sisestusväli
    label = tk.Label(aken, text="Aastane intressimäär (%)").pack()
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()

    # Teine sisestusväli
    label = tk.Label(aken, text="Laenuperiood (aastad)").pack()
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()
   
    # Nupp mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()