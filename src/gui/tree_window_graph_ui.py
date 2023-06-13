import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from src.Classes.person import Person
from PIL import Image
import io
import numpy as np
from collections import deque
from graphviz import Digraph


class TreeWindowGraphUi:
    def setup_ui(self, person: Person, person_list: list) -> FigureCanvas:
        G = Digraph(comment='Family Tree')

        partner_edge = []

        already_added = set()
        queue = deque()

        def BFS(person_start):
            queue.append(person_start)
            already_added.add(person_start)
            G.node(str(person_start))
            while len(queue) > 0:
                person_tmp = queue.pop()

                for person_partner in person_tmp.partners:
                    if person_partner not in already_added:
                        already_added.add(person_partner)
                        queue.append(person_partner)

                    if (
                            str(person_tmp),
                            str(person_partner)) not in partner_edge:
                        partner_edge.append(
                            (str(person_partner), str(person_tmp)))

                        with G.subgraph() as s:
                            s.attr(rank='same')
                            s.node(str(person_tmp), shape='oval')
                            s.node(str(person_partner), shape='oval')
                            s.node(str(person_tmp) + str(person_partner),
                                   label=' ', shape='point', color='red',
                                   **{'width': str(0.08)})  # środkowy

                            s.edge(str(person_partner),
                                   str(person_tmp) + str(person_partner),
                                   dir='none', color='red')
                            s.edge(str(person_tmp) + str(person_partner),
                                   str(person_tmp), dir='none', color='red')

                        for person_child in person_tmp.children:

                            if person_child.father in [person_tmp,
                                                       person_partner] and \
                                    person_child.mother in \
                                    [person_tmp, person_partner]:
                                G.node(str(person_child), shape='oval')
                                G.edge(str(person_tmp) + str(person_partner),
                                       str(person_child))

                                if person_child not in already_added:
                                    already_added.add(person_child)
                                    queue.append(person_child)

                if person_tmp.mother is not None:
                    if person_tmp.mother not in already_added:
                        already_added.add(person_tmp.mother)
                        queue.append(person_tmp.mother)

                    G.node(str(person_tmp.mother), shape='oval')

                    if person_tmp.father is None:
                        G.edge(str(person_tmp.mother), str(person_tmp))

                if person_tmp.father is not None:
                    if person_tmp.father not in already_added:
                        already_added.add(person_tmp.father)
                        queue.append(person_tmp.father)

                    G.node(str(person_tmp.father), shape='oval')

                    if person_tmp.mother is None:
                        G.edge(str(person_tmp.father), str(person_tmp))

        BFS(person)

        for person_tmp in person_list:
            if person_tmp not in already_added:
                BFS(person_tmp)

        png_bytes = G.pipe(format='png')
        img = np.array(Image.open(io.BytesIO(png_bytes)))

        ax = plt.gca()
        ax.imshow(img)
        ax.axis('off')

        plt.subplots_adjust(hspace=0.5)
        fig = plt.gcf()

        canvas = FigureCanvas(fig)

        return canvas
