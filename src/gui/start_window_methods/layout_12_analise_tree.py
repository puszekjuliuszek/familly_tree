from functools import partial
from matplotlib import pyplot as plt
from src.definitions.definitions import X2, Y1, X1, Y4, WIN_WIDTH
from src.definitions.ui_css import START_WINDOW_ANALISE_TREE_CSS
from src.gui.info_window import InfoWindow
from src.gui.start_window_methods.layout_10_find_relation import \
    load_saved_trees
from src.gui.start_window_methods.layout_2 import update_dicts
from src.io_functions.read_data import read_data


def analise_tree_clicked(self):
    self.clear_ui()
    self.error_label.setText(" ")

    self.MainWindow.setStyleSheet(START_WINDOW_ANALISE_TREE_CSS)
    self.verticalLayoutWidget_4.setGeometry(X2, Y1, 0, 0)
    self.verticalLayoutWidget_6.setGeometry(X1, Y1, WIN_WIDTH - X1, Y4)

    self.tree_lbl.setText("wybierz drzewo do przeanalizowania:")
    self.verticalLayout_6.addWidget(self.tree_lbl)

    load_saved_trees(self)
    self.trees.setPlaceholderText("wybierz drzewo")
    self.trees.addItems(self.trees_list)
    self.verticalLayout_6.addWidget(self.trees)

    self.choose_tree_to_analise.setAutoDefault(False)
    self.choose_tree_to_analise.clicked.connect(
        partial(choose_tree_to_analise_clicked, self))
    self.verticalLayout_6.addWidget(self.choose_tree_to_analise)
    self.choose_tree_to_analise.setText("W to drzewo analizuj")

    self.info_label.setText("")
    self.verticalLayout_6.addWidget(self.info_label)


def choose_tree_to_analise_clicked(self):
    places_plot(self)
    info_window(self)


def places_plot(self):
    self.tree_to_open = self.trees.currentText()
    main_person, person_list = read_data(self.tree_to_open, 1, flag=True)
    update_dicts(self)
    places_count_list = [0 for _ in range(max(self.places_dicts.values()))]
    for person in person_list:
        for place in person.residences:
            places_count_list[self.places_dicts.get(place) - 1] += 1

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.barh(self.places, places_count_list)
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)
    ax.grid(color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)
    ax.invert_yaxis()
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='grey')
    ax.set_title("Podział ludzi między miastami",
                 loc='left', )
    plt.show()


def info_window(self):
    main_person, person_list = read_data(self.tree_to_open, 1, flag=True)
    update_dicts(self)
    places_count_list = [0 for _ in range(max(self.places_dicts.values()))]
    for person in person_list:
        for place in person.residences:
            places_count_list[self.places_dicts.get(place) - 1] += 1
    self.info_window = InfoWindow(person_list, self.places[
        places_count_list.index(max(places_count_list))])
    self.info_window.show()