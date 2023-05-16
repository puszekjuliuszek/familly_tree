def update_partners(id: int, partenrs_list: list, file_data: list) -> None:
    for person in file_data:
        if person['person_id'] in partenrs_list:
            person['partners_id'].append(id)
