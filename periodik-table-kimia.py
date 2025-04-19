import periodictable
element_nama = input("element-> ").capitalize()
Ssss = getattr(periodictable, element_nama, None)

if Ssss:
    print(f"Element: {Ssss.name}")
    print(f"Simbol: {Ssss.symbol}")
    print(f"No Atom: {Ssss.number}")
    print(f"berat Atom: {Ssss.mass}")
    print(f"kepadatan: {Ssss.density}")
else:
    print(f"Element '{element_nama}' gaketemu.")
