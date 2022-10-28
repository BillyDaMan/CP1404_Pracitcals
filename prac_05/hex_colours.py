COLOUR_NAME_TO_CODE = {"ABSOLUTE ZERO": "#0048ba", "BLACK": "#000000", "BLOND": "#faf0be", "CELESTE": "#b2ffff",
                       "DENIUM": "#1560bd", "EBONY": "#555d50", "FROSTBITE": "#e936a7", "GREEN": "#00ff00",
                       "HELIOTROPE": "#df73ff", "ICEBERG": "#71a6d2"}
print(COLOUR_NAME_TO_CODE)

colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()


