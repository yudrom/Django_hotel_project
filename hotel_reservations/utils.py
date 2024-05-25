def get_room_type_russian(type_name):
    if type_name == 'single':
        return 'Одиночный'
    elif type_name == 'double':
        return 'Двухместный'
    elif type_name == 'triple':
        return 'Трёхместный'
    elif type_name == 'quadruple':
        return 'Четырехместный'
    else:
        return type_name