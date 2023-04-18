from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from src.Classes.person import Person
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

# TODO zamykanie okna powoduje zapis drzewa ?

class TreeWindowGraphUi:
    # def on_node_click(self, event):
    #     node_text = event.artist.get_text()
    #     node_num = str(node_text)
    #     print(f"Kliknięto węzeł {node_num}")

    def setup_ui(self, person:Person):
        G = nx.DiGraph() #graf skierowany
        G.add_node(str(person))

        already_added = set()
        queue = deque()
        queue.append(person)
        already_added.add(person)

        while len(queue) > 0:
            person_tmp = queue.pop()
            for person_partner in person_tmp.partners:
                if person_partner not in already_added:
                    already_added.add(person_partner)
                    queue.append(person_partner)
                G.add_node(str(person_partner))
                G.add_edge(str(person_tmp), str(person_partner))

            for person_child in person_tmp.children:
                if person_child not in already_added:
                    already_added.add(person_child)
                    queue.append(person_child)
                G.add_node(str(person_child))
                G.add_edge(str(person_tmp), str(person_child))

            if person_tmp.mother is not None:
                if person_tmp.mother not in already_added:
                    already_added.add(person_tmp.mother)
                    queue.append(person_tmp.mother)
                G.add_node(str(person_tmp.mother))
                #G.add_edge(str(person_tmp), str(person_tmp.mother))

            if person_tmp.father is not None:
                if person_tmp.father not in already_added:
                    already_added.add(person_tmp.father)
                    queue.append(person_tmp.father)
                G.add_node(str(person_tmp.father))
                #G.add_edge(str(person_tmp), str(person_tmp.father))

        # pos = nx.spring_layout(G)
        pos = graphviz_layout(G,prog="twopi")
        # https://stackoverflow.com/questions/57512155/how-to-draw-a-tree-more-beautifully-in-networkx

        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

        ax = plt.gca()
        ax.axis('off')


        for node in G.nodes:
            button = ax.annotate(str(node), xy=pos[node], ha="center", va="center")
            button.set_picker(True)
            # przycisk odpala okieno z person z danymi tej osoby, przyciski do dodania rodziny,

        self.fig = plt.gcf()
        #self.fig.canvas.mpl_connect('pick_event', self.on_node_click)
        canvas = FigureCanvas(self.fig)



        return canvas

