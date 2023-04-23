import math
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from src.Classes.person import Person
import random
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import igraph as ig


# TODO zamykanie okna powoduje zapis drzewa ?

class TreeWindowGraphUi:
    # def on_node_click(self, event):
    #     node_text = event.artist.get_text()
    #     node_num = str(node_text)
    #     print(f"Kliknięto węzeł {node_num}")

    def setup_ui(self, person: Person):
        G = nx.DiGraph()  # graf skierowany
        G.add_node(str(person))

        already_added = set()
        queue = deque()

        level = 0
        level_max = -1 * math.inf
        level_min = math.inf
        persons_dict = {}

        queue.append((person, level))
        already_added.add(person)

        while len(queue) > 0:
            person_tmp, level_tmp = queue.pop()

            # level_max = max(level_max,level_tmp)
            # level_min = min(level_min,level_tmp)
            persons_dict[str(person_tmp)] = (random.uniform(0, 1),level_tmp)

            for person_partner in person_tmp.partners:
                if person_partner not in already_added:
                    already_added.add(person_partner)
                    queue.append((person_partner,level_tmp))
                G.add_node(str(person_partner))
                G.add_edge(str(person_tmp), str(person_partner))

            for person_child in person_tmp.children:
                if person_child not in already_added:
                    already_added.add(person_child)
                    queue.append((person_child,level_tmp-1))
                G.add_node(str(person_child))
                G.add_edge(str(person_tmp), str(person_child))

            if person_tmp.mother is not None:
                if person_tmp.mother not in already_added:
                    already_added.add(person_tmp.mother)
                    queue.append((person_tmp.mother,level_tmp+1))
                G.add_node(str(person_tmp.mother))
                # G.add_edge(str(person_tmp), str(person_tmp.mother))

            if person_tmp.father is not None:
                if person_tmp.father not in already_added:
                    already_added.add(person_tmp.father)
                    queue.append((person_tmp.father,level_tmp+1))
                G.add_node(str(person_tmp.father))
                # G.add_edge(str(person_tmp), str(person_tmp.father))

        print(persons_dict)
        print(persons_dict)
        # pos = nx.spring_layout(G)
        #pos = graphviz_layout(G, prog="twopi")
        # https://stackoverflow.com/questions/57512155/how-to-draw-a-tree-more-beautifully-in-networkx
        pos = persons_dict


        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos, arrowstyle='-', arrowsize=20)

        ax = plt.gca()
        ax.axis('off')

        for node in G.nodes:
            button = ax.annotate(str(node), xy=pos[node], ha="center", va="center")
            button.set_picker(True)
            # przycisk odpala okieno z person z danymi tej osoby, przyciski do dodania rodziny,

        plt.subplots_adjust(hspace=0.5)
        self.fig = plt.gcf()
        # self.fig.canvas.mpl_connect('pick_event', self.on_node_click)
        canvas = FigureCanvas(self.fig)

        return canvas
