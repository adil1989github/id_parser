def sum_id(id_customer: str):
    return sum(list(map(int, list(id_customer))))


def counter_customer_start_0(n_customer: int):
    for i, j in dict_group.item():
        if len(j) == n_customer:
            return i


def counter_customer(n_customer: int, n_first_id: str):
    for i, j in dict_group.item():
        if len(j) == n_customer and j[0] == n_first_id:
            return i


def group_funk(list_id):
    dict_ = {}
    for i in list_id:
        num_id = sum_id(i)
        if num_id not in dict_:
            dict_[num_id] = [i]
        else:
            dict_[num_id] += [i]
    return dict_


if __name__ == "__main__":
    # Заполните свой список id
    example_id_list = ['7412567', '7415267', '1234567']
    # Из списка формирует словари. Пример: {32: [7412567, 7415267], 28: [1234567]}
    dict_group = group_funk(list_id)
    # num_customer количество клиентов
    num_customer: int = 1
    # num_first_id первый id в списке
    num_first_id: str = ''
    if n_first_id == '':
        print(counter_customer_start_0(num_customer))
    else:
        print(counter_customer(num_customer, num_first_id))


