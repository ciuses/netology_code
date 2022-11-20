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
        print(filo_name)
        print(filo_len)
        print(filo.seek(0))
        print(filo.readline())





if __name__ == '__main__':


    # for obj in prepare_your_objects():
    #     print(obj)
    #     sp_obj = obj[0]
    #     print(sp_obj.readlines())


    write_your_objects()