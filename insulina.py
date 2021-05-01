jednostka = input("W jakiej jednostce chcesz podać stężenie glukozy - mg/dl czy mmol/l? - wpisz odpowiednią: ")

def mmol_l_na_mg_dl(glukoza2):
    glukoza2_1 = glukoza2 * 18
    return glukoza2_1

def mg_dl_na_mmol_l(glukoza1):
    glukoza1_1 = glukoza1 / 18
    return glukoza1_1

while jednostka != "mmol/l" and jednostka != "mg/dl":
    print("Jednostka została źle wpisana")
    jednostka = input("W jakiej jednostce chcesz podać stężenie glukozy - mg/dl czy mmol/l? - wpisz odpowiednią: ")
if jednostka == "mg/dl":
    glukoza1 = int(input("Podaj wartość w mg/dl: "))
    if glukoza1 > 216:
        print("Zwiększ insulinę o 0,5-1U co 12 godzin")
    elif 180 <= glukoza1 <= 216:
        print("Utrzymaj tę samą dawkę insuliny")
    elif 144 <= glukoza1 < 180:
        print("Rozważ zmniejszenie dawki insuliny o 0,5U co 12 godzin")
    elif 80 <= glukoza1 < 144:
        print("Koniecznie zmniejsz dawkę insuliny o 0,5U co 12 godzin")
    else:
        print("Nie podawaj insuliny")
    while glukoza1 < 54:
        print("Natychmiast podaj glukozę na błony śluzowe i ponownie zmierz stężenie glukozy")
        glukoza1 = int(input("Ponownie zmierzona wartość stężenia glukozy w mg/dl wynosi: "))
    przelicznik1 = input("Czy chcesz przeliczyć wartość w mg/dl na mmol/l? - wpisz tak lub nie: ")
    if przelicznik1 == "tak":
        print(mg_dl_na_mmol_l(glukoza1))
    elif przelicznik1 == "nie":
        print("nie to nie")

elif jednostka == "mmol/l":
    glukoza2 = float(input("Podaj wartość w mmol/l: "))
    if glukoza2 > 12.0:
        print("Zwiększ insulinę o 0,5-1U co 12 godzin")
    elif 10.0 <= glukoza2 <= 12.0:
        print("Utrzymaj tę samą dawkę insuliny")
    elif 8.0 <= glukoza2 < 10.0:
        print("Rozważ zmniejszenie dawki insuliny o 0,5U co 12 godzin")
    elif 4.5 <= glukoza2 < 8.0:
        print("Koniecznie zmniejsz dawkę insuliny o 0,5U co 12 godzin")
    else:
        print("Nie podawaj insuliny")
    while glukoza2 < 3.0:
        print("Natychmiast podaj glukozę na błony śluzowe i ponownie zmierz stężenie glukozy")
        glukoza2 = float(input("Ponownie zmierzona wartość stężenia glukozy w mmol/l wynosi: "))
    przelicznik2 = input("Czy chcesz przeliczyć wartość w mg/dl na mmol/l? - wpisz tak lub nie: ")
    if przelicznik2 == "tak":
        print(mmol_l_na_mg_dl(glukoza2))
    elif przelicznik2 == "nie":
        print("nie to nie")

input()
