import math
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from src.Classes.person import Person
import matplotlib.image as mpimg
from PIL import Image
import io
import numpy as np
import random
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from graphviz import Digraph
from src.definitions import definitions

# TODO zamykanie okna powoduje zapis drzewa ?

from collections import deque
import random
import math
import pydot

from graphviz import Digraph, Source, Graph


class TreeWindowGraphUi:
    def setup_ui(self, person: Person) -> FigureCanvas:
        G =Digraph(comment='Family Tree')

        # add the root node
        G.node(str(person))

        partner_edge = []

        already_added = set()
        queue = deque()

        level_max = -1 * math.inf
        level_min = math.inf

        queue.append((person, 0))
        already_added.add(person)

        while len(queue) > 0:
            person_tmp, level_tmp = queue.pop()

            level_max = max(level_max, level_tmp)
            level_min = min(level_min, level_tmp)

            for person_partner in person_tmp.partners:
                if person_partner not in already_added:
                    already_added.add(person_partner)
                    queue.append((person_partner, level_tmp))


                if (str(person_tmp),str(person_partner)) not in partner_edge:
                    partner_edge.append((str(person_partner),str(person_tmp)))
                    with G.subgraph() as s:
                        s.attr(rank='same')
                        s.node(str(person_tmp))
                        s.node(str(person_partner))
                        s.edge(str(person_tmp), str(person_partner),dir='none')
                        #s.edge(str(person_partner),str(person_tmp))

            if person_tmp.children != []:
                with G.subgraph() as c:
                    c.attr(rank='same')
                    for person_child in person_tmp.children:
                        c.node(str(person_child))


                for person_child in person_tmp.children:
                    if person_child not in already_added:
                        already_added.add(person_child)
                        queue.append((person_child, level_tmp - 1))


                    G.edge(str(person_tmp), str(person_child))

            if person_tmp.mother is not None:
                if person_tmp.mother not in already_added:
                    already_added.add(person_tmp.mother)
                    queue.append((person_tmp.mother, level_tmp + 1))

                G.node(str(person_tmp.mother))

            if person_tmp.father is not None:
                if person_tmp.father not in already_added:
                    already_added.add(person_tmp.father)
                    queue.append((person_tmp.father, level_tmp + 1))

                G.node(str(person_tmp.father))

        print("end bfs")
        # render the graph
        # G.render('family_tree1.gv')
        # print("end ernder")
        # Gtmp = nx.DiGraph()
        # Gtmp.add_node("Gi")
        print("1")
        # nx.draw(Gtmp)

        # fig, ax = plt.subplots()
        print("2")
        png_bytes = G.pipe(format='png')
        img = np.array(Image.open(io.BytesIO(png_bytes)))
        print("3")
        ax = plt.gca()
        ax.imshow(img)
        ax.axis('off')
        print("3.5")
        plt.subplots_adjust(hspace=0.5)
        fig = plt.gcf()
        print("3.7")
        canvas = FigureCanvas(fig)
        print("4")
        return canvas
