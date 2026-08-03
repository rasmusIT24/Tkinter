#Harjutus 4
#Rasmus Ojala
import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("400x100")
    aken.title("Värvi nupud")

    def kuva_varv(v):
        vastus.config(text=v)

    nupp1 = tk.Button(aken, bg="red", fg="red", font=("Arial", 16), command=lambda: kuva_varv("punane"))
    nupp2 = tk.Button(aken, bg="orange", fg="orange", font=("Arial", 16), command=lambda: kuva_varv("oranž"))
    nupp3 = tk.Button(aken, bg="yellow", fg="yellow", font=("Arial", 16), command=lambda: kuva_varv("kollane"))
    nupp4 = tk.Button(aken, bg="green", fg="green", font=("Arial", 16), command=lambda: kuva_varv("roheline"))
    nupp5 = tk.Button(aken, bg="blue", fg="blue", font=("Arial", 16), command=lambda: kuva_varv("sinine"))
    vastus = tk.Label(aken, text=f"Siia tuleb vastus")
    vastus.pack(side="bottom", expand=True, fill="x")
    nupp1.pack(side="left", expand=True, fill="x")
    nupp2.pack(side="left", expand=True, fill="x")
    nupp3.pack(side="left", expand=True, fill="x")
    nupp4.pack(side="left", expand=True, fill="x")
    nupp5.pack(side="left", expand=True, fill="x")

    aken.mainloop()

if __name__ == "__main__":
    main()