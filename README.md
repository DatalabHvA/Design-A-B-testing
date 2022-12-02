# Design A/B testing
Dit is een tool om de aantrekkelijkheid van twee ontwerpen te vergelijken.


### Instructies: 

Je maakt twee ontwerpen op basis van het template in de map 'designs'. Gebruik je creativiteit om de aandacht te vestigen op het blokje (je mag alle ruimte gebruiken, maar laat het blokje leeg). In het blokje gaan straks letters worden getoond en we testen welke letter het beste opvalt en dus of je ontwerp succesvol is geweest.

Maak binnen de map 'designs' een nieuwe map voor jouw test run (zie bestaand voorbeeld 'test1') en plaats er de twee .png bestanden die je wil vergelijken in. Geef de bestanden een begrijpelijke naam, deze worden namelijk gebruikt om de resultaten te rapporteren. 

Run nu vanuit een terminal of command prompt het python script 'design_AB_test.py' gevolgd door -folder en de naam van je testmap, bijv 
```python design_AB_test.py -folder test1```
en optioneel stel je met -n het aantal herhalingen in (default -n 25). 

De ontwerpen worden in verschillende volgordes en combinaties getoond. Druk telkens op de toets op je toetsenbord die hoort bij de letter die je het snelste opvalt ('z' of 'm'). NB: je moet dus niet kiezen voor links/rechts maar voor de letter zelf! Aan het eind krijg je de resultaten te zien van welk ontwerp je het vaakst hebt gekozen. Gebruik deze feedback om je ontwerp te verbeteren en test het nog een keer!

Voor vragen of verbeteringen van dit script, stuur een email naar p.c.bons@hva.nl. 
