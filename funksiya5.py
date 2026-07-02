def min_maxx(royhat):
    kichik = royhat[0]
    katta  = royhat [0]
    for son in royhat:
        if son < kichik:
          kichik = son
        if son > katta:
          katta = son

    return(kichik , katta)

print(min_maxx([1,3,2,7,5]))
print()