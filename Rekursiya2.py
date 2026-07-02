def max(royhat):
    
    kattasi = royhat[0]
    for son in royhat:
        if son > kattasi:
            kattasi = son
    return kattasi

print(max([1,2,3,4,5,200]))
