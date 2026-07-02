def bomi(royhat,element):
    if len (royhat)==0:
        return False
    if royhat[0] == element:
        return True
    return bomi(royhat[1:],element)

print(bomi ([2,3,4,5,67,7,7],67))