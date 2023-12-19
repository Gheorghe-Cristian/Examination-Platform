class Sortare:

    def quick_sort_cresc(self, data):
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2][0]
        less = []
        equal = []
        greater = []

        for row in data:
            if row[0] < pivot:
                less.append(row)
            elif row[0] == pivot:
                equal.append(row)
            else:
                greater.append(row)

        return self.quick_sort_cresc(less) + equal + self.quick_sort_cresc(greater)
    def quick_sort_descresc(self, data):
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2][0]
        less = []
        equal = []
        greater = []

        for row in data:
            if row[0] < pivot:
                less.append(row)
            elif row[0] == pivot:
                equal.append(row)
            else:
                greater.append(row)

        return self.quick_sort_descresc(greater) + equal + self.quick_sort_descresc(less)
