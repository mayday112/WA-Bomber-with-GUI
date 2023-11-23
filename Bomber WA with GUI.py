import pyautogui as py, time, tkinter as tk
from tkinter import ttk
from tkinter.messagebox import*

window = tk.Tk()
window.title("Bomber WA Python")
window.geometry("400x300")
window.configure(background="lightgray")

label = tk.Label(window, text="Jangan lupa buka WhatsApp dulu ngab!\nSama buka chat ke orang yang mau di bomber")
label.pack(padx=10, pady=10,fill="x")

pesan = tk.StringVar()
jumlah = tk.StringVar()

frame = ttk.Frame(window)
frame.pack(pady=10,fill="x", expand=True)

label1 = ttk.Label(frame, text="Tulis pesannya ngab:")
label1.pack(padx=10, pady=10,  fill="x")

pesan1 = ttk.Entry(frame,textvariable=pesan)
pesan1.pack(padx=10,pady=10,fill="x", expand=True)

label2 = ttk.Label(frame, text="Berapa jumlahnya ngab:")
label2.pack(padx=10, pady=10,  fill="x")

jlh = ttk.Entry(frame,textvariable=jumlah)
jlh.pack(padx=10,pady=10,fill="x", expand=True)

def kirim(psn, jlh):
        showinfo(message="Habis klik ok langsung buka WA lagi\ntrus tunggu selama 5 detik")
        time.sleep(5)
        pesan = psn
        jumlah = int(jlh)
        for i in range (jumlah) :
            py.write(pesan)
            time.sleep(0.05)
            py.press("enter")
tombol = ttk.Button(frame, text="Let`s Go!", command= lambda: kirim(pesan.get(), jumlah.get()))
tombol.pack(padx=100,pady=10,fill="x", expand=True)
window.mainloop()