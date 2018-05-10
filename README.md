# Ångström financiën
Dit script zet de transactions.csv welke zijn gedownload via de Rabobank om naar een gebruiksvriendelijk Excel bestand. Hierdoor kunnen de transacties zoals deze in de Rabobank afschriften staan direct gebruikt kunnen worden in Excel voor de administratie van de financiën.

## Hoe te gebruiken
Volg onderstaand stappenplan om de transacties bij de Rabobank te downloaden.

1. Open de website van de [Rabobank](https://www.rabobank.nl/bedrijven/)
2. Ga naar het tabblad 'Internetbankieren' en klik op de betreffende rekening.
![alt text](figuren/stap1.png)
3. Links op het scherm is nu 'Downloaden transacties' zichtbaar, klik hier op.
![alt text](figuren/stap2.png)
4. Stel vervolgens de instellingen in zoals deze zijn weergegeven in onderstaande screenshot.
![alt text](figuren/stap3.png)
5. Klik op 'Bestand downloaden' en sla het bestand op in dezelfde folder als waar het python script staat opgeslagen.
6. Voer het Python script uit.
7. Open het gegenereerde 'transactions.xlsx' bestand en controleer via de website van de [Rabobank](https://www.rabobank.nl/bedrijven/) of de gedownloade transacties exact aansluiten met de huidige administratie. Wanneer er niet tussendoor transacties met de optie 'Vanaf de laatste download' gedownload zijn, dan zouden de gedownloade transacties netjes moeten aansluiten. Indien dit niet het geval is dan kan via de optie 'Specifieke datum reeks' de juiste datum reeks worden gekozen. Mogelijk is het dan wel nodig om enkele transacties aan het begin te verwijderen. Controleer daarom weer even of de transactie van cel 2, 3, ... in Excel niet al in de huidige administratie staat. Herhaal in iedergeval deze hele stap om er zeker van te zijn dat er geen transacties dubbel staan of ontbreken. Het gegenereerde bestand ziet er als volgt uit.
![alt text](figuren/stap4.png)

## Controle van de transacties
Om stap 7 iets nader te specificeren is er in onderstaand figuur een voorbeeld van de controle te zien. Het linker Excel sheet is het bestand waar de administratie in word gedaan. Hier is te zien dat de laatste geadministreerde transactie is op datum *08-02-2018* van tegenrekening *NL85...*. In het middelste gedeelte is het transactie overzicht op de website van de Rabobank zichtbaar. Wanneer deze vergeleken word met de linker sheet dan is te zien dat de eerste transactie op *08-02* met rekeningnummer *NL85...* is geadministreerd. Vervolgens heeft er op *08-02* een transactie plaatsgevonden met *NL04...*. Deze staat niet in de linker sheet! De gedownloade transacties moeten dus bij deze transactie beginnen. Dit is het geval en het is zichtbaar in de rechter sheet. Hier is een transactie op *08-02-2018* met tegenrekening *NL04...*. 

![alt text](figuren/stap5.png)
Het downloaden en omzetten van de transacties is dus succesvol. Het rechtersheet kan gekopieerd worden en worden geplakt onder het einde van de linker sheet.