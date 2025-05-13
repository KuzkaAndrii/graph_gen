import copy
import tkinter as tk

import drove
from graph import Graph
import random
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Interface:
    def __init__(self):
        self.root=tk.Tk()
        self.graph_exist = False
        self._g = None
    def import_part(self, r):
        self.but_import = tk.Button(self.root, text="ввести граф", width=30, command=self.import_graph)
        self.ent_import = tk.Entry(self.root, width=20)
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
        self.ent_search=tk.Entry(self.root, width=20)

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

        self.lis=tk.Listbox(self.root, selectmode="browse", height=3)
        self.lis.insert(tk.END, "graph")
        self.lis.insert(tk.END, "orgraph")
        self.lis.insert(tk.END, "veight")
        self.leb_lis=tk.Label(self.root, text="введіть тип графу з яким працюватимете")
        self.leb_lis.grid(row=r+1, column=0, columnspan=1)
        self.lis.grid(row=r+1, column=1)

        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.subplot = self.fig.add_subplot(111)
        self.subplot.plot()




        self.canv=FigureCanvasTkAgg(self.fig, master=self.root)
        self.canv_wid=self.canv.get_tk_widget()
        self.canv_wid.grid(row=0, column=0, rowspan=1, columnspan=3)
        return r+3
    def show(self):
        i=1
        i=self.import_part(i)
        i=self.short_way_part(i)
        i=self.otherG_part(i)
        i=self.gen_part(i)
        i=self.comunic_part(i)
        self.root.mainloop()
        return

    def select(self):
        s_i = self.lis.curselection()
        if s_i:
            s_it = self.lis.get(s_i[0])
            return s_it
        else:
            return False

    def import_graph(self):

        s = self.select()
        print(s)
        st=self.ent_import.get()
        print(st)
        if s == False:
            return
        elif self.graph_exist:
            return
        try:
            self._g = Graph.input_as_vertex_list(s, file=st)
            self.graph_exist = True
        except:
            return

    def is_together(self):
        if self._g.typo == "veight":
            self.leb_com.configure(text="Для такого типу графа код невизначений")
        res = self._g.is_together()
        if res:
            self.leb_com.configure(text="Граф зв'язний")
        else:
            self.leb_com.configure(text="Граф незв'язний")
        return

    def graph_gen(self):
        if self.graph_exist:
            self.leb_com.configure(text="граф вже існує")
        else:
            self._g = Graph.graph_gen(int(self.ent_gen1.get()), int(self.ent_gen2.get()), typo=self.select())
            self.graph_exist = True

    def visualize(self):
        if not self.graph_exist:
            com.configure(text="граф не існує")
        else:
            print(type(self._g._v))
            self._g.vertex_dict_x = np.random.rand(self._g._v + 1)
            self._g.vertex_dict_y = np.random.rand(self._g._v + 1)
            print("OKK")
            print(self._g.typo)
            if self._g.typo == "veight":
                print("1")
            elif self._g.typo == "orgraph":
                print("2")
            else:
                print("Ok")
                self.subplot.plot(self._g.vertex_dict_x[1:], self._g.vertex_dict_y[1:], 'o', markersize=5, color='black')
                self.canv.draw()
                im_list=np.zeros((self._g._v+1, self._g._v+1))
                for i in range(1, self._g._v+1):
                    for v in self._g._e[i]:
                        if i>v and self._g.typo!="orgraph":
                            continue
                        if v==i:
                            drove.petl(self._g.vertex_dict_x[i], self._g.vertex_dict_y[i], im_list[i, i], self.subplot, self.canv)
                            im_list[i][i]+=1
                        else:
                            drove.edge(self._g.vertex_dict_x[i], self._g.vertex_dict_y[i], self._g.vertex_dict_x[v], self._g.vertex_dict_y[v], im_list[i, v], self.subplot, self.canv)
                            im_list[i, v]+=1

if __name__=="__main__":
    Int=Interface()
    Int.show()