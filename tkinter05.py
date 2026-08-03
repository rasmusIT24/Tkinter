#Harjutus 5
#Rasmus Ojala
import tkinter as tk

def main():
    aken = tk.Tk()
    aken.title("Tkinderi ülesanded")
    aken.geometry("400x400")
    # Akna suuruse muutmise keelamine
    aken.resizable(False, True)

  # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        laenusumma = int(sisestus1.get()) #Võtab esimese sisestuse
        kuuintressimäär = float(sisestus2.get())/12/100  # Võtab esimese sisestuse
        maksete_arv = int(sisestus3.get())*12  # Võtab teise sisestuse

        igakuine_makse = laenusumma * kuuintressimäär / (1- (1 + kuuintressimäär) ** -maksete_arv)
        vastus = tk.Label(aken, text=f"{maksete_arv:.2f}")
        vastus.pack()

    # Loo raamid
    frame = tk.Frame(aken)
    frame.pack(pady=5, padx=5, fill="both")
    frame2 = tk.Frame(aken)
    frame2.pack(pady=5, padx=5, fill="both")
    frame3 = tk.Frame(aken)
    frame3.pack(pady=5, padx=5, fill="both")

    # Esimene sisestusväli
    label1 = tk.Label(frame, text="Laenusumma (€)").pack(side='left')
    sisestus1 = tk.Entry(frame)
    sisestus1.pack(side='left', expand=True, fill="x")
   
    # Teine sisestusväli
    label2 = tk.Label(frame2, text="Aastane intressimäär (%)").pack(side='left')
    sisestus2 = tk.Entry(frame2)
    sisestus2.pack(side='left', expand=True, fill="x")

    # Teine sisestusväli
    label3 = tk.Label(frame3, text="Laenuperiood (aastad)").pack(side='left')
    sisestus3 = tk.Entry(frame3)
    sisestus3.pack(side='left', expand=True, fill="x")
   
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Arvuta", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()