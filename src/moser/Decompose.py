def Decompose(lis):
    '''Decomposes a list of molecules into their composition.

            The decomposition yields a list containing a dictionary for each molecule,
            connecting each element to their occurrences in the compound
            (element (str) : occurrences in molecule (int)).

            Args:
                lis (list) : contains the molecules as strings

            Returns:
                l_dics (list) :  contains a dictionnary for each molecule'''

    l_dics = []
    for i in range(len(lis)):
        l_temp = list(lis[i] + "*")

        '''Concatenates lower- and uppercase letters'''
        j = 0
        while j < len(l_temp) - 1:
            if str(l_temp[j]).isupper() and str(l_temp[j + 1]).islower():
                l_temp[j] = l_temp[j] + l_temp[j + 1]
                del l_temp[j + 1]
            j = j + 1

        '''Concatenates coefficients'''
        j = 0
        while j < len(l_temp) - 1:
            if str(l_temp[j]).isdigit():
                idx_start = j
                idx_end = j
                while str(l_temp[idx_end]).isdigit() and idx_end < len(l_temp)-1:
                    idx_end = idx_end + 1
                if idx_end - idx_start > 1:
                    number = "".join(l_temp[idx_start:idx_end])
                    l_temp.insert(idx_start, number)
                j = idx_end + 1
            else:
                j = j + 1

        '''Adds the implicit coefficient 1'''
        j = 0
        while j < len(l_temp) - 1:
            if str(l_temp[j]).isalpha() and str(l_temp[j+1]).isdigit() == False:
                l_temp.insert(j+1, 1)
            j = j + 1

        '''Distributes coefficients in brackets'''
        l_idx = []
        for j in range(len(l_temp)):
            if l_temp[j] == "(":
                l_idx.append(j)

        cnt = -1
        for j, z in enumerate(l_temp):
            if str(l_temp[j]).isdigit() and l_temp[j - 1] == ")":
                cnt = cnt + 1
                for k in range(l_idx[cnt], j, 2):
                    if str(l_temp[k]).isnumeric():
                        l_temp[k] = int(l_temp[k]) * int(l_temp[j])

        j = 0
        while j < len(l_temp) - 1:
            if str(l_temp[j]).isdigit() and l_temp[j - 1] == ")":
                del l_temp[j]
            j = j + 1

        if str(l_temp[-1]).isdigit() and str(l_temp[-2]) == ")":
            del l_temp[-1]

        '''Deletes brackets'''
        while "(" in l_temp:
            l_temp.remove("(")

        while ")" in l_temp:
            l_temp.remove(")")

        '''Creates a dictionary element:total_coefficient'''
        d_temp = {}
        for j in range(len(l_temp)-1):
            if str(l_temp[j]).isalpha():
                if l_temp[j] in d_temp:
                    d_temp[l_temp[j]] = int(d_temp[l_temp[j]]) + int(l_temp[j + 1])
                else:
                    d_temp[l_temp[j]] = int(l_temp[j + 1])

        d_temp = {key:value for key, value in sorted(d_temp.items())}

        l_dics.append(d_temp)

    return l_dics

