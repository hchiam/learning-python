def create2dDict(n,m):
    dico = {}
    for i in range(n):
        for j in range(m):
            if i not in dico:
                dico[i] = {}
            dico[i][j] = -1
    return dico

if __name__ == '__main__': # only run the below code if directly running this .py file, not importing it
    print create2dDict(3,2)