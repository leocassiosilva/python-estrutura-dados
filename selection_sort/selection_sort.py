def selection_sort(v):
    len_v = len(v)
    for i in range (len_v - 1):
        menor = i
        for j in range(i + 1, len_v):
            if v[j] < v[menor]:
                menor = j
        v[menor], v[i] = v[i], v[menor]

v = [10, 40, 5, 15, 30, 70, 20]
print(v)
selection_sort(v)
print(v)