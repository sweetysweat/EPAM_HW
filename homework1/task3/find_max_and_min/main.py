from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as f:
        numbers = f.read().replace('\n', ' ').split()
        print(numbers)
    max_value = min_value = int(numbers[0])
    for i in numbers:
        if int(i) > max_value:
            max_value = int(i)
        elif int(i) < min_value:
            min_value = int(i)
    return min_value, max_value


if __name__ == '__main__':
    print(find_maximum_and_minimum("file.txt"))
