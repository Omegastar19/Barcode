# Barcode
voorraad systeem met barcode scanner

PC1: Database met producten

PC2: Barcode scanner, scanned barcodes en stuurt ze door naar PC1 om de voorraad aan te passen.

PC2 bevat 3 bestanden die van elkaar afhankelijk zijn en dus samen in een folder geplaatst moeten worden.

Main.py bevat de main loop waarmee je het programma start.

BarcodeScanner.py bevat code voor het openen van de camera, het scannen van barcodes, het versturen van de barcode naar de Database-pc, en het schrijven van een logboek. 

LET OP: Het programma voegt gescande producten toe aan de Database door middel van een '+' in de functie 'handle_barcode_info' op lijn 40. Als je het programma juist gescande producten moet weghalen uit de Database, verander dan de '+' in een '-'.

BarcodeScanner_GUI.py bevat de grafische interface dat het programma toegankelijk maakt, en bestaat uit een menu met een optie om de scanner/camera aan en uit te zetten, een optie om het logboek te laten zien, en een optie om de snelheid van de scanner te veranderen (de delay geeft het aantal secondes aan tussen elke scan die de camera maakt)

LET OP: Naast het downloaden van de bestanden moet ook een logboek-bestand aangemaakt worden VOORDAT je het programma start, onder de naam 'barcode_logbook.txt', dat in dezelfde folder geplaatst moet worden. 
