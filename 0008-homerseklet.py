valassz = input('Mit szeretnél váltani?\nA: Celsius -> Fahrenheit\nB: Fahrenheit -> Celsius\n\n')
if valassz.lower() == 'a':
    c = input('Kérlek, írd be, hány Celsius-fokot szeretnél Fahrenheitté alakítani: ')
    f = int(c) * (9 / 5) + 32
    print(c, 'Celsius-fok egyenlő', f, 'Fahrenheit-fokkal.')
elif valassz.lower() == 'b':
    f = input('Kérlek, írd be, hány Fahrenheit-fokot szeretnél Celsiussá alakítani: ')
    c = (int(f) - 32) * 5/9
    print(f, 'Fahrenheit-fok egyenlő', c, 'Celsius-fokkal.')
else:
    print('Valószínűleg valamit helytelenül adtál meg, ugyanis a(z)', valassz, 'nem szerepel a választási lehetőségek (A és B) között.')
