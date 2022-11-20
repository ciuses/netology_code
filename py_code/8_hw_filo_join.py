import os


def prepare_your_objects(path_to_fils: str = 'other\\files\\') -> list:
    files_objects = []
    for full_paths in [path_to_fils + filo_name for filo_name in os.listdir(path_to_fils)]:
        files_objects.append(open(full_paths, 'rt', encoding='utf-8'))
    row_list = [(file_object, len(file_object.readlines())) for file_object in files_objects]
    return sorted(row_list, key=lambda row_list: row_list[1])


def write_your_objects(list_obj_and_len: str = prepare_your_objects()):
    for filo, filo_len in list_obj_and_len:
        filo_path = filo.name
        _, _, filo_name = filo_path.split('\\')
        filo.seek(0)
        write_to_filo(filo_name, filo_len, filo.readlines())



def write_to_filo(filo_name: str, filo_len: str, list_of_lines: list):
    with open('final_filo.txt', 'a', encoding='utf8') as file_object:
        file_object.write(f'{filo_name}\n{filo_len}\n')
        for line in list_of_lines:
            file_object.write(line)



if __name__ == '__main__':


    # for obj in prepare_your_objects():
    #     print(obj)
    #     sp_obj = obj[0]
    #     print(sp_obj.readlines())


    write_your_objects()

    # write_to_filo('test.txt', '23')