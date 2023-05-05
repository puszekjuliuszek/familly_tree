from src.io_functions import read_data as RD
from src.Classes import person
import queue

#TODO poszukac sposobu rozróżniania zależności krwi,
#liczyc ile do gory/dol bylo ruchów oraz ile w prawo lewo
#(prawo lewo -> żona, mąż)

def BFS(personFirst: person.Person, personSecond: person.Person = None):
    visited = set()
    graph_path = {personFirst: None}
    Q = queue.Queue()
    Q.put(personFirst)
    visited.add(personFirst)

    while not Q.empty():
        person_now = Q.get()

        if person_now.father is not None and person_now.father != 0:
            if person_now.father not in visited:
                visited.add(person_now.father)
                graph_path[person_now.father] = person_now
                Q.put(person_now.father)

        if person_now.mother is not None and person_now.mother != 0:
            if person_now.mother not in visited:
                visited.add(person_now.mother)
                graph_path[person_now.mother] = person_now
                Q.put(person_now.mother)

        for person_partner in person_now.partners:
            if person_partner not in visited:
                visited.add(person_partner)
                graph_path[person_partner] = person_now
                Q.put(person_partner)

        for person_child in person_now.children:
            if person_child not in visited:
                visited.add(person_child)
                graph_path[person_child] = person_now
                Q.put(person_child)

    pointer = personSecond
    path = []
    while pointer is not None:
        path.append(pointer)
        pointer = graph_path.get(pointer)

    print("Path:")
    for p in path:
        print(p)

main_person,person_list = RD.read_data("Zawislak2.json",flag=True)
print("From read:")
for p in range(len(person_list)):
    print(p,":",person_list[p])
print("Start:")
BFS(person_list[1],person_list[8])
