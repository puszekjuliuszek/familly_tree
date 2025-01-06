from src.io_functions.save_data import save_data
from src.io_functions.read_data import read_data


if __name__ == "__main__":
    main_person = read_data('Zawislak2.json', 10)
    main_person.print_tree()
    save_data(main_person, "Zawislak3.json")

