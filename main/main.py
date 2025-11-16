def find_kth_missing_positive_number(numbers, kth_missing):
    if not numbers:
        return kth_missing
    range_end_num = kth_missing + numbers[-1] + 1
    missing_nums_list = []

    for x in range(1, range_end_num):
        if x not in numbers:
            missing_nums_list.append(x)

    return missing_nums_list[kth_missing - 1]

