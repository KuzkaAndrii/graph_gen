import tkinter as tk
from graph import Graph
class Interface:
    def __init__(self):
        self.root=tk.Tk()
    def import_part(self, r):
        self.but_import = tk.Button(self.root, text="ввести граф", width=30)
        self.ent_import = tk.Entry(self.root, width=30)
        self.leb_import = tk.Label(self.root, text="Введіть шлях до текстового файлу", width=30)
        self.but_import.grid(row=r, column=0)
        self.leb_import.grid(row=r, column=1)
        self.ent_import.grid(row=r, column=2)
        return r+1
    def short_way_part(self, r):
        self.but_short=tk.Button(self.root, text="Пошук найкоротшого шляху", width=30, height=3)
        self.leb_short1=tk.Label(self.root, text="Від", width=10)
        self.leb_short2=tk.Label(self.root, text="до", width=10)
        self.ent_short1=tk.Entry(self.root, width=20)
        self.ent_short2=tk.Entry(self.root, width=20)

        self.but_short.grid(row=r, column=0, rowspan=2)
        self.leb_short1.grid(row=r, column=1)
        self.ent_short1.grid(row=r, column=2)
        self.leb_short2.grid(row=r+1, column=1)
        self.ent_short2.grid(row=r+1, column=2)
        return r+2
    def otherG_part(self, r):
        self.but_is_t=tk.Button(self.root, text="Перевірка на зв'язність", width=30, height=3)
        self.but_search=tk.Button(self.root, text="Шукати підграф", width=60)
        self.leb_searsh=tk.Label(self.root, text="Введіть файл з підграфом")
        self.ent_search=tk.Entry(self.root, width=30)

        self.but_is_t.grid(row=r, column=0, rowspan=2)
        self.but_search.grid(row=r, column=1, columnspan=2)
        self.leb_searsh.grid(row=r+1, column=1)
        self.ent_search.grid(row=r+1, column=2)
        return r+2
    def gen_part(self, r):
        self.but_gen=tk.Button(self.root, text="згенерувати граф", width=30, height=3)
        self.leb_gen1=tk.Label(self.root, text="число вершин")
        self.leb_gen2=tk.Label(self.root, text="число ребер")
        self.ent_gen1=tk.Entry(self.root)
        self.ent_gen2=tk.Entry(self.root)

        self.but_gen.grid(row=r, column=0, rowspan=2)
        self.leb_gen1.grid(row=r, column=1)
        self.ent_gen1.grid(row=r, column=2)
        self.leb_gen2.grid(row=r+1, column=1)
        self.ent_gen2.grid(row=r+1, column=2)
        return r+2
    def comunic_part(self, r):
        self.leb_int_com=tk.Label(text="Рядок для комунікації:", width=30)
        self.leb_com=tk.Label(text="", width=60)

        self.leb_int_com.grid(row=r, column=0)
        self.leb_com.grid(row=r, column=1, rowspan=2)
        return r+1
    def show(self):
        i=0
        i=self.import_part(i)
        i=self.short_way_part(i)
        i=self.otherG_part(i)
        i=self.gen_part(i)
        i=self.comunic_part(i)
        self.root.mainloop()
        return

if __name__=="__main__":
    Int=Interface()
    Int.show()