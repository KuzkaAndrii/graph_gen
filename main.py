#стандартні бібліотеки
import tkinter as tk

#завантажені бібліотеки
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#власні бібліотеки
import drawe
from graph1 import Graph


class Interface:
    def __init__(self):
        self.root=tk.Tk()
        self.graph_exist = False
        self._g = None

    #частина інтерфейсу що в основному відповідає за ввід графу з файла
    def import_part(self, r):
        self.but_import = tk.Button(self.root, text="ввести граф", width=30, command=self.import_graph)
        self.ent_import = tk.Entry(self.root, width=20)
        self.leb_import = tk.Label(self.root, text="Введіть шлях до текстового файлу", width=30)
        self.but_import.grid(row=r, column=0)
        self.leb_import.grid(row=r, column=1)
        self.ent_import.grid(row=r, column=2)
        return r+1


    # частина інтерфейсу що в основному відповідає за комунікацію
    def comunic_part(self, r):
        self.leb_int_com = tk.Label(text="Рядок для комунікації:", width=30)
        self.leb_com = tk.Label(text="Ласкаво просимо", width=60)
        self.leb_int_com.grid(row=r, column=0)
        self.leb_com.grid(row=r, column=1, columnspan=2)

        self.lis = tk.Listbox(self.root, selectmode="browse", height=3)
        self.lis.insert(tk.END, "graph")
        self.lis.insert(tk.END, "orgraph")
        self.lis.insert(tk.END, "weight")
        self.leb_lis = tk.Label(self.root, text="введіть тип графу, який буде згенерований")
        self.leb_lis.grid(row=r + 1, column=0, columnspan=1)
        self.lis.grid(row=r + 1, column=1)
        return r + 3


    #частина інтерфейсу що в основному відповідає за візуалізацію
    def visualize_part(self, r):
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.subplot = self.fig.add_subplot(111)
        self.subplot.plot()
        self.canv = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canv_wid = self.canv.get_tk_widget()
        self.canv_wid.grid(row=0, column=0, rowspan=1, columnspan=3)

        self.but_clean = tk.Button(self.root, text="Стерти граф з полотна", width=30, command=self.clean)
        self.but_cl_g = tk.Button(self.root, text="Стерти граф", width=30, command=self.clean_g)
        self.but_vis = tk.Button(self.root, text="Візуалізувати", width=30, command=self.visualize)
        self.but_clean.grid(row=r, column=0)
        self.but_cl_g.grid(row=r, column=1)
        self.but_vis.grid(row=r, column=2)
        return r+1


    #частина інтерфейсу що в основному відповідає за пошук найкоротшого шляху
    def short_way_part(self, r):
        self.but_short=tk.Button(self.root, text="Пошук найкоротшого шляху", width=30, height=3, command=self.highlight_way)
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


    # частина інтерфейсу що в основному відповідає за решту
    def otherG_part(self, r):
        self.but_is_t=tk.Button(self.root, text="Перевірка на зв'язність", width=30, height=3, command=self.is_together)
        self.but_search=tk.Button(self.root, text="Шукати підграф", width=60, command=self.check_subgraph)
        self.leb_searsh=tk.Label(self.root, text="Введіть файл з підграфом")
        self.ent_search=tk.Entry(self.root, width=20)

        self.but_is_t.grid(row=r, column=0, rowspan=2)
        self.but_search.grid(row=r, column=1, columnspan=2)
        self.leb_searsh.grid(row=r+1, column=1)
        self.ent_search.grid(row=r+1, column=2)

        return r+2


    # частина інтерфейсу що в основному відповідає за генерацію графа
    def gen_part(self, r):
        self.but_gen=tk.Button(self.root, text="згенерувати граф", width=30, height=3, command=self.graph_gen)
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

    # частина інтерфейсу що в основному відповідає за збереження графа
    def save_part(self, r):
        self.but_save = tk.Button(self.root, text="зберегти граф", width=30, command=self.safe)
        self.leb_save = tk.Label(self.root, text='Текстовий файл для зберігання:')
        self.ent_save = tk.Entry(self.root)

        self.but_save.grid(row=r, column=0)
        self.leb_save.grid(row=r, column=1)
        self.ent_save.grid(row=r, column=2)

        return r+1

    # виклад віджетів
    def show(self):
        i=1
        i=self.comunic_part(i)
        i=self.gen_part(i)
        i=self.import_part(i)
        i=self.visualize_part(i)
        i=self.short_way_part(i)
        i=self.otherG_part(i)
        i=self.save_part(i)
        self.root.mainloop()
        return

    # вводить дані про тип графу зі списку
    def select(self):
        s_i = self.lis.curselection()
        if s_i:
            s_it = self.lis.get(s_i[0])
            return s_it
        else:
            return False


    # функця перевірки на зв'язність для віджета
    def is_together(self):
        res = self._g.is_together()
        if res:
            self.leb_com.config(text="Граф зв'язний")
        else:
            self.leb_com.config(text="Граф незв'язний")
        return


    # функця вводу графа для віджета
    def import_graph(self):
        st=self.ent_import.get()
        if self.graph_exist:
            self.leb_com.configure(text='Граф вже існує')
        else:
            self._g = Graph.input_graph(st)
            self.graph_exist = True
            self.visualize()
        return


    # функця генерації графа для віджета
    def graph_gen(self):
        if self.graph_exist:
            self.leb_com.configure(text="граф вже існує")
        else:
            self._g = Graph.gen_graph(int(self.ent_gen1.get()), int(self.ent_gen2.get()), self.select())
            self.graph_exist = True
            self.leb_com.configure(text="граф згенеровано")
            self.visualize()


    # функця візуалізації графа
    def visualize(self):
        if not self.graph_exist:
            self.leb_com.configure(text="граф не існує")
        else:
            self.subplot.plot(self._g._v_x[1:], self._g._v_y[1:], 'o', markersize=5, color='black')
            self.canv.draw()
            nv=len(self._g.list_v)
            im_list=np.zeros((nv+1, nv+1))

            for i in range(1, nv + 1):
                for v in self._g._edge_list[i]:
                    if self._g.type != 'orgraph':
                        if i > v:
                            continue
                        if v == i:
                            drawe.petl(self._g._v_x[i], self._g._v_y[i], im_list[i, i], self.subplot, self.canv)
                            im_list[i][i] += 1
                        else:
                            drawe.edge(self._g._v_x[i], self._g._v_y[i], self._g._v_x[v], self._g._v_y[v], im_list[i, v], self.subplot, self.canv)
                            im_list[i, v] += 1
                    else:
                        if v == i:
                            drawe.petl_arr(self._g._v_x[i], self._g._v_y[i], im_list[i, i], self.subplot, self.canv)
                            im_list[i][i] += 1
                        else:
                            drawe.edge_arr(self._g._v_x[i], self._g._v_y[i], self._g._v_x[v], self._g._v_y[v], im_list[i, v], self.subplot, self.canv)
                            im_list[i, v] += 1
        return


    # функця видалення візуалізації графа для віджета
    def clean(self):
        self.subplot.cla()
        self.canv.draw()
        self.leb_com.configure(text="Граф стерто")
        return


    # функця видалення графа для віджета
    def clean_g(self):
        self.clean()
        self.graph_exist=False
        self.leb_com.configure(text="Граф видалено")
        return


    # функця збереження графа для віджета
    def safe(self):
        way = self.ent_save.get()
        self._g.print_graph(way=way)
        self.leb_com.configure(text='Граф збережено')
        return


    # функця переходу на підграф для віджета
    def check_subgraph(self):
        way=self.ent_search.get()
        h=Graph.input_graph(way)
        if self._g.has_subgraph(h):
            self.leb_com.configure(text="Є підграфом")
        else:
            self.leb_com.configure(text="Не є підграфом")
        return


    # функця пошуку найкоротшого шляху для віджета
    def highlight_way(self):
        st = int(self.ent_short1.get())
        fn = int(self.ent_short2.get())

        d, way = self._g.Dijkstra(st, fn)
        if d == None:
            self.leb_com.configure(text='Нема шляху між даними ребрами')
            return
        print(d, way)
        vert=way[0::2]
        edges=way[1::2]

        self.subplot.plot(self._g._v_x[vert], self._g._v_y[vert], 'o', markersize=5, color='red')
        self.canv.draw()

        for v, num in edges:
            i=0
            while self._g._edge_list[v][i] != self._g._edge_list[v][num]:
                i+=1
            n = num - i
            x1 = self._g._v_x[self._g._dedge_list[v][num]._s]
            y1 = self._g._v_y[self._g._dedge_list[v][num]._s]
            x2 = self._g._v_x[self._g._dedge_list[v][num]._f]
            y2 = self._g._v_y[self._g._dedge_list[v][num]._f]
            drawe.edge(x1, y1, x2, y2, n, self.subplot, self.canv, col='red')
if __name__=="__main__":
    Int=Interface()
    Int.show()