def volume_sphere(r):
    v = 4 * 3.14 * r * r * r / 3
    return v

vs = volume_sphere(10)
print("半径１０ｃｍの急の体積は", vs, "cm3")
print("半径２０ｃｍの急の体積は", volume_sphere(20), "cm3")