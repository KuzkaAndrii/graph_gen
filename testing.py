#Стандартні бібліотеки
import unittest
import os

#власні бібліотеки
import graph1
from mywold import cut

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.gr_con = open(os.path.join(os.getcwd(), *['tests', 'counted_graphs.txt']))
        self.gf_ucn = open(os.path.join(os.getcwd(), *['tests', 'uncounted_graphs.txt']))
        self.gr_sub = open(os.path.join(os.getcwd(), *['tests', 'subgraphs.txt']))
        self.gr_sht = open(os.path.join(os.getcwd(), *['tests', 'shortestway.txt']))


    def tearDown(self):
        self.gr_con.close()
        self.gf_ucn.close()
        self.gr_sub.close()
        self.gr_sht.close()


    #тестування звязності
    def test_counting(self):
        for r in self.gr_con.readlines():
            way = cut(r)[0]
            way = os.path.join(os.getcwd(), *['tests', 'graphs', way])
            g=graph1.Graph.input_graph(way)
            self.assertTrue(g.is_conected(), r)
        for r in self.gf_ucn.readlines():
            way = cut(r)[0]
            way = os.path.join(os.getcwd(), *['tests', 'graphs', way])
            g = graph1.Graph.input_graph(way)
            self.assertFalse(g.is_conected(), r)


    #тестування підграфа
    def test_subgraphs(self):
        for r in self.gr_sub.readlines():
            way_g, way_h, sub = cut(r)
            way_g = os.path.join(os.getcwd(), *['tests', 'graphs', way_g])
            way_h = os.path.join(os.getcwd(), *['tests', 'graphs', way_h])
            if sub[0]=='F':
                sub = False
            else:
                sub = True
            g = graph1.Graph.input_graph(way_g)
            h = graph1.Graph.input_graph(way_h)
            self.assertEqual(g.has_subgraph(h), sub, r)


    #тестування найкоротшого шляху
    def test_short(self):
        for r in self.gr_sht.readlines():
            way, st, fn, d, = cut(r)
            way = os.path.join(os.getcwd(), *['tests', 'graphs', way])
            g = graph1.Graph.input_graph(way)
            st = int(st)
            fn = int(fn)
            d = float(d)
            new_d, way = g.Dijkstra(st, fn)
            self.assertEqual(d, new_d, r)
if __name__ == '__main__':
    unittest.main()