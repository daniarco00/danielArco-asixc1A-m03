

#region Funcion ReadIntList
def ReadIntList(list):
    list_int = []
    for i in list:
        if int(i) != -1:
            list_int.append(i)
        else:
            return list_int
#endregion