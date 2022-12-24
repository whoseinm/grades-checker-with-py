marks={
    "Günay":223,
    "Mahir":254,
    "Nərminə":270,
}
pr = int(input("Keçid balını daxil edin"))
for k,v in marks.items():
    if v >= pr:
        print(k)