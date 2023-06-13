from os import listdir
from shutil import copyfile

from src.definitions.definitions import ROOT_DIR
from _csv import reader


def add_tree_to_saved_trees(path: str) -> None:
    if len(path.split("/")) > 1:
        tree_name = path.split("/")[-1]
    else:
        tree_name = path.split("\\")[-1]
    relative_path = "../../resources/Tree_files/" + tree_name
    tree_names = []
    with open(ROOT_DIR + "\\resources\\saved_trees.csv", "r") as file:
        csvreader = reader(file)
        for row in csvreader:
            tree_names.append(row[1].strip())
    if tree_name not in tree_names:
        with open(ROOT_DIR + "\\resources\\saved_trees.csv", "a") as file:
            file.write(relative_path + "," + tree_name + "\n")
    else:
        # TODO może info, że drzewo jest już zapisane?
        pass


def make_copy_of_a_tree(path: str) -> None:
    filenames = listdir('/'.join(path.split("/")[0:-1]))
    tree_name = path.split("/")[-1]
    if tree_name not in filenames:
        copyfile(path, "../../resources/Tree_files/" + tree_name)


def on_node_click(event):
    node_text = event.artist.get_text()
    node_num = str(node_text)
    print(f"Kliknięto węzeł {node_num}")

def pyqt_date_to_json_date(date: str) -> str:
    date_list = date.split(".")
    date_list.reverse()
    return "-".join(date_list)