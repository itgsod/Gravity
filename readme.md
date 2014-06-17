# Gravity #

Den här uppgiften går ut på att skriva ett program räknar ut vad rymdsonder kommer väga på olika planeter.

Programmet skall läsa in en fil med namn, radie och densitet för olika planeter, och skriva ut vad
sonden kommer väga på de olika planeterna

## Bedömningsmatris ##

### Planering ###

| Förmågor                         | E 																																   | C | A |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Aktivitetsdiagram och pseudokod  | Du använder pseudokod och/eller aktivitetsdiagram för att planera dina uppgifter utifrån exempel, eller i samråd med utbildaren.  | Som för E, men utan exempel eller handledning |   |
| Anpassning					   | Du anpassar med viss säkerhet planeringen till uppgiften 																		   |   | Som för E, men med säkerhet
| Utformning                       | Du väljer med viss säkerhet lämpliga kontrollstrukturer, metoder, variabler, datastrukturer och algoritmer | | Som för E, men du väljer med säkerhet, och motiverar utförligt dina val.|
| Utvärdering | Med viss säkerhet utvärderar du, med enkla omdömen, programmets prestanda, använder datalogiska begrepp, och bedömer din egen förmåga | som för E, men med nyanserade omdömen | Som för C, men med säkerhet, och med förbättringsförslag

### Syntax och Teori ###
| Förmågor                                       | E 																			| C | A |
|------------------------------------------------|------------------------------------------------------------------------------|---|---|
| Datatyper					                     | Du kan redogöra för och använda de vanligaste datatyperna                    |   |   |
| Grundläggande syntax		                     | Du kan redogöra för och använda programmeringsspråkets grundläggande syntax  |   |   |
| Villkor och IF-satser		                     | Du kan redogöra för och använda villkor och IF-satser                        |   |   |
| Loopar & iteration                             | Du kan redogöra för och använda loopar och iterera över listor               |   |   |

### Kodning och kodningsstil ###

| Förmågor                                      | E                                                                         | C                                               | A                                              |
|-----------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| Komplexitet									| Du kan skriva enkla program                                               | Du kan skriva lite mer avancerade program       | Du kan skriva komplexa program
| Sekventiell- & funktionsbaserad programmering | Du använder dig av sekventiell programmering och fördefinerade funktioner | Du skapar och använder enkla funktioner         | Du skapar mer komplexa funktioner              |
| Objektorienterad programmering                | Du använder dig av av fördefinerade klasser och objekt                    | Du skapar och använder enkla klasser och objekt | Du skapar och använder mer komplicerade klasser och objekt  |
| Struktur		 				                | Du skriver kod som är delvis strukturerad, har en konsekvent kodningsstil och tydlig namngivning | Som för E, men du skriver kod som är helt strukturerad |   			   |
| Felsökning                                    | Du felsöker på egen hand enkla syntaxfel | Som för E, men systematiskt, och dessutom även körtidsfel och programmeringslogiska fel | Som för C, men med effektivitet   	   |
| Undantagshantering                            |     																		| Du validerar användardata						  | Som för C, men du skriver även kod som använder undantagshantering |
| Dokumentering 								| Du skriver kod som är delvis kommenterad									|  												  | Du skriver kod som är utförligt kommenterad    |

### Datastrukturer ###

| Förmågor        | E 														   | C 																     | A 									 |
|-----------------|------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------|
| Listor          | Du kan redogöra för och använda dig av listor (Array)      |   																     |   									 |
| Hashtabeller    | Du kan redogöra för vad hashtabeller (Hash) är             | Du kan använda dig av hashtabeller 							     |   									 |

## Beskrivning ##

### Dataformat ###

* Datafilen består av en rad text per planet.
* Varje rad består av 3 kolumner, som är separerade med ett komma.

* Första kolumnen innehåller planetens namn
* Andra kolumnen innehåller planetens radie
* Tredje kolumnen innehåller planetens genomsnittliga densitet


De första raderna i filen:

    Mercury, 2439700, 5427
    Venus, 6051900, 5243
    Earth, 6367445, 5515

### Funktioner ###

I den här uppgiften kommer du bygga flera funktioner som arbetar tillsammans:

#### load_data_file ####

Tar emot en sökväg till en fil, läser in den, och returnerar en array/list med varje rad i filen.

#### parse_lines ####

Tar emot en array som motsvarar raderna i filen (dvs det som load_data_file returnerar), och returnerar en array/list av hashar/dicts
som innehåller planetens namn, radie, och densitet.

#### volume_of_planet ####

Den här funktionen saknar tester.
Den ska ta emot en planets radie och returnera volymen

Formeln för att räkna ut volymen på en sfär givet sfärens radie `r` är

    4 * π * r³
    ----------
        3

#### calculate_weight ####

Tar emot sondens massa och en planethash/dict, och returnerar en sträng med namnet på planeten och sondens vikt på den planeten.


För att räkna ut vikten på sonden används följande formel:

givet gravitationskonstanten G = 6.67e-11

                 massa på objekt 1 (sonden) * massa på objekt 2 (planeten)
    vikt = G * -------------------------------------------------------------
               (avståndet mellan objekt 1 och objekt 2 (planetens radie))²


Det kan vara bra att skapa några egna funktioner för att dela upp calculate_weight i mindre delar.

### Genomförande ###

Programmet skall utvecklas testdrivet.

Skapa funktionerna i lib/gravity.rb, eller lib/gravity.py

Testerna finns i /spec, eller /test

Kör rspec köra testerna, eller nosetests --rednose test/testfilensnamn

## Utvärdering ##

Efter programmet är avslutat skall du utvärdera hur projektet gick.





