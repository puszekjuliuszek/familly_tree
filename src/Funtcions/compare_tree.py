from src.io_functions.read_data import read_data

#TODO tworzyc to nowe polączone drzewo?

# def connect_trees(accepted_matches: list, tree1_person_list:list, tree2_person_list:list):
#
#     for tree1_person,tree2_person in accepted_matches:
#         tree1_person



def find_matching(tree1_list: list, tree2_list: list, minimum_matching: int, matches: list) -> None:
    for tree1_person in tree1_list:
        for tree2_person in tree2_list:
            if tree1_person.check_matching(tree2_person) >= minimum_matching:
                matches.append((tree1_person, tree2_person))
    return None


def split_gender(people_list) -> (list, list):
    man_list = []
    woman_list = []

    for person in people_list:
        if person.gender == 1:
            man_list.append(person)
        else:
            woman_list.append(person)

    return man_list, woman_list


def compare_tree(tree_path1: str, tree_path2: str, minimum_matching: int,)->list:
    _, tree1_people_list = read_data(tree_path1, flag=True)
    _, tree2_people_list = read_data(tree_path2, flag=True)

    tree1_man_list, tree1_woman_list = split_gender(tree1_people_list)
    tree2_man_list, tree2_woman_list = split_gender(tree2_people_list)

    matches = [] #lista krotek z obiektami klasy Person miedzy ktorymi występuje podobienstwo

    find_matching(tree1_man_list, tree2_man_list, minimum_matching, matches)
    find_matching(tree1_woman_list, tree2_woman_list, minimum_matching, matches)



    return matches


if __name__ == "__main__":
    tree_path1 = "Zawislak3.json"
    tree_path2 = "Zawislak4.json"
    minimum_matching = 8
    # minium matching from 1 to 9
    # minium matching znajduje poprawnie
    compare_tree(tree_path1, tree_path2, minimum_matching, True)
