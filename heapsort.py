
def heapsort(a: list[int]) -> list[int]:


    def print_heap(a: list[int], int_size=6, blancs=1) -> None:
        a = [i for i in a]
        del a[0]
        def design_one_line(part_a: list[int], _counter) -> str:
            emmitator = " " * blancs + " " * int_size + " " * blancs
            part_a = [blancs * " " + (str(i) + "-" + str(ind)).center(int_size, " ") + " " * blancs for ind, i in enumerate(part_a, (len(part_a)))]
            is_digit = _counter // len(part_a)
            part_a = [(part_a[i // is_digit] if i % is_digit == is_digit // 2 else emmitator) for i in range(_counter)]
            return "|" + "".join(part_a) + "|"

        deep = 1
        _counter = 1
        while _counter <= len(a):
            deep += 1
            _counter *= 2
        a.extend([""] * (_counter - len(a) + 1))
        print("=" * (2 + int_size * _counter + 2 * blancs * _counter))
        last_ind = 0
        for i in range(0, deep - 1):
            print(design_one_line(a[last_ind: 2 * last_ind + 1], _counter))
            print("|" + " " * (int_size * _counter + 2 * blancs * _counter) + "|")
            last_ind = 2 * last_ind + 1
        print("=" * (2 + int_size * _counter + 2 * blancs * _counter))

    def _shift(a: list[int], index, l, r):

        if r > (ind2 := l + index * 2 + 1):
            if a[(ind1 := l + index * 2)] > a[ind2]:
                if a[(ind := l + index)] < a[ind1]:
                    a[ind], a[ind1] = a[ind1], a[ind]
                    a = _shift(a, index * 2, l, r)
                    print_heap(a)
                    return a
            else:
                if a[(ind := l + index)] < a[ind2]:
                    a[ind], a[ind2] = a[ind2], a[ind]
                    a = _shift(a, index * 2 + 1, l, r)
                    print_heap(a)
                    return a
        elif r > (ind1 := l + index * 2):
            if a[(ind := l + index)] < a[ind1]:
                a[ind], a[ind1] = a[ind1], a[ind]
                a = _shift(a, index * 2, l, r)
                print_heap(a)
                return a
        print_heap(a)
        return a

    def _reverse_shift(a: list[int], index, l, r):
        if r > (ind2 := l + index * 2 + 1):
            if a[(ind1 := l + index * 2)] < a[ind2]:
                if a[(ind := l + index)] > a[ind1]:
                    a[ind], a[ind1] = a[ind1], a[ind]
                    a = _shift(a, index * 2, l, r)
                    print_heap(a)
                    return a
            else:
                if a[(ind := l + index)] > a[ind2]:
                    a[ind], a[ind2] = a[ind2], a[ind]
                    a = _shift(a, index * 2 + 1, l, r)
                    print_heap(a)
                    return a
        elif r > (ind1 := l + index * 2):
            if a[(ind := l + index)] > a[ind1]:
                a[ind], a[ind1] = a[ind1], a[ind]
                a = _shift(a, index * 2, l, r)
                print_heap(a)
                return a
        print_heap(a)
        return a

    def create_heap(a: list[int]) -> list[int]:
        a = [float("-inf")] + a
        [(_shift(a, i, 0, len(a)), print(f"c {1} <= {i} <= {len(a)}")) for i in range(len(a) // 2 - 1, 0, -1)]
        return a

    def _sort_shift(a: list[int], min_el_index, next_index) -> None:
        print(a)
        a[min_el_index], a[next_index] = a[next_index], a[min_el_index]
        print(a)
        _shift(a, min_el_index, 0, next_index)
        return None

    def _heap_sort(a: list[int]) -> list[int]:
        [(_sort_shift(a, 1, i), print(i)) for i in range(len(a) - 1, 0, -1)]
        return a




    a = create_heap(a)
    a = _heap_sort(a)
    print(a)
    return a


if __name__ == "__main__":
    from random import shuffle
    a = [44, 55, 12, 42, 94, 18, 6, 67]
    a = list(range(1, 16))
    shuffle(a)
    a = [12, 5, 7, 11, 4, 6, 8, 9, 2, 13, 10, 15, 3, 14, 1]
    print(a)
    heapsort([i for i in a])
    # shuffle(a)
    # print(a)
    # heapsort([i for i in a])
