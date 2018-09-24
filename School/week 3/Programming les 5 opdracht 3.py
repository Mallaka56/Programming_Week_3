leeftijd = int(input('Voer je leeftijd in: '))
paspoort = input('Heb je een Nederlands paspoort: ')
if leeftijd >=18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen.')
else:
    if leeftijd <18 or paspoort == 'nee':
        print('Helaas, je mag niet stemmen.')
