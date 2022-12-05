# Design A/B testing
Dit is een tool om de aantrekkelijkheid van twee ontwerpen te vergelijken.


### Instructies: 

Download alle files uit deze repository naar de je computer (via het groene knopje 'Code' - download ZIP, of gebruik git clone als je een git-gebruiker bent) en unzip de bestanden naar een handige map. 

Je maakt twee ontwerpen op basis van het template in de map 'designs'. Gebruik je creativiteit om de aandacht te vestigen op het blokje (je mag alle ruimte gebruiken, maar laat het blokje leeg). In het blokje gaan straks letters worden getoond en we testen welke letter het beste opvalt en dus of je ontwerp succesvol is geweest.

Maak binnen de map 'designs' een nieuwe map voor jouw test run (zie bestaand voorbeeld 'test1') en plaats er de twee .png bestanden die je wil vergelijken in. Geef de bestanden een begrijpelijke naam, deze worden namelijk gebruikt om de resultaten te rapporteren. 

Open nu een terminal of command prompt en navigeer naar de map waar je de code hebt opgeslagen. Run vanuit daar het python script 'design_AB_test.py' gevolgd door -folder en de naam van je testmap, bijv 
```python design_AB_test.py -folder test1```
en optioneel stel je met -n het aantal herhalingen in (default -n 25). Als je het package cv2 nog niet hebt kan je dat eerst installeren via ```pip install opencv-python```.

De ontwerpen worden nu in verschillende volgordes en combinaties getoond. Druk telkens op de toets op je toetsenbord die hoort bij de letter die je het snelste opvalt ('z' of 'm'). NB: je moet dus niet kiezen voor links/rechts maar voor de letter zelf! Aan het eind krijg je de resultaten te zien van welk ontwerp je het vaakst hebt gekozen. Gebruik deze feedback om je ontwerp te verbeteren en test het nog een keer!

Als het venster niet in je beeldscherm past kan je de grootte aanpassen door via -s een schaalfactor mee te geven bij het uitvoeren (bijv ```python design_AB_test.py -folder test1 -s 1.5``` om het venster 1.5x kleiner te makem). 

Voor vragen of verbeteringen van dit script, stuur een email naar p.c.bons@hva.nl. 
