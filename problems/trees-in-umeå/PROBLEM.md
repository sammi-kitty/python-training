Den här uppgiften är stor, den kommer sträcka sig över både lektion 5 och 6, och ni kan också då inte hinna. Lös så långt ni hinner.

Umeå är som bekant 'björkarnas stad', och Umeå kommun har följaktligen många björkar att sköta. För att hålla ordning har de en databas av alla träd som sköts av kommunen på opendata.umea.se. Det kan dock vara svårt att navigera denna råa data för hand, så låt oss ta Python till hjälp för att reda ut vad som finns och inte!

Ni kan ladda ner den kompletta filen här: https://people.cs.umu.se/mbe/trad.csv. Då det finns 30,750 träd i denna fil kan det under utvecklingen vara praktiskt att använda en liten exempelfil som gör det lätt att identifiera när saker går fel. I filen https://people.cs.umu.se/mbe/trad_dobelns_park.csv hittar ni följande träd från mitten av Döbelns park i centrum:

Geo Point;Löv- eller barrträd;Trädart vetenskapligt namn;Trädart svenskt namn;Gatu- eller parkträd;Planteringsdatum
63.82300408270902, 20.269983819258425;Lövträd;Acer Platanoides;Skogslönn;Parkträd;
63.82279098707962, 20.270625453505563;Lövträd;Betula Pubescens Rubra;Finsk Rödbjörk;Parkträd;2011-07-01
63.82305287146964, 20.270125581436098;Lövträd;Fraxinus Chinensis Var. Rhynchophylla;Kinesisk Ask;Parkträd;2021-05-24
63.823103177554884, 20.270333850953733;Lövträd;Prunus Pensylvanica;Amerikanskt Häggkörsbä;Parkträd;
63.82273103008566, 20.270134396976548;Barrträd;Picea Pungens Glauca-Gruppen;Blågran;Parkträd;
63.8229941499964, 20.27043579699731;Lövträd;Ulmus Laevis;Vresalm;Parkträd;
63.82299908170276, 20.269813439507217;Lövträd;Acer Platanoides;Skogslönn;Parkträd;
63.822838164027196, 20.270107835262216;Barrträd;Pinus Sibirica;Sibirisk Cembratall;Parkträd;
63.82282308955348, 20.27012206661297;Barrträd;Pinus Sibirica;Sibirisk Cembratall;Parkträd;
63.822952136495516, 20.27058988979781;Lövträd;Aesculus Hippocastanum;Hästkastanj;Parkträd;
63.822721586303274, 20.27029102432705;Lövträd;Populus Laurifolia;Lagerpoppel;Parkträd;
63.82291314874386, 20.27028178179637;Lövträd;Prunus Virginiana;Virginiahägg;Parkträd;2011-07-01
63.82301763881295, 20.2705555942879;Lövträd;Prunus Sargentii;Bergkörsbär;Parkträd;2011-07-01
63.822823661263556, 20.270509381852968;Lövträd;Betula Pubescens Rubra;Finsk Rödbjörk;Parkträd;2011-07-01
63.822873291315396, 20.270434031963593;Lövträd;Betula Pendula;Vårtbjörk;Parkträd;
63.82282956119599, 20.27067356125068;Lövträd;Acer Freemanii Autumn Blaze Jeffersr;Freemanlönn Autumn Blaze Jef;Parkträd;2011-07-01

På en karta ser den här delen ut så här (barrträd i mörkare färg): // Bild saknas

Första raden är instruktion om innehållet i filen (finns både i stora och lilla), sedan representerar varje rad ett träd. Informationen är uppdelad med semikolon (';'), första elementet på varje rad är de två koordinaterna för trädet (i grader longitud och latitud), sedan information om det är ett barr- eller lövträd, latinskt namn på arten, svenskt namn på arten, vilken roll trädet spelar i stadsplaneringen (bara parkträd i lilla filen), och slutligen när trädet planterades (om man vet). Koordinaterna i första kolumnen är i sin tur två flyttal delade på med ett komma och mellanslag (', ').

Filerna finns också på Canvas som trad-som-forvaltas-av-gator-och-parker.csv och dobelns_park.csv om dessa fungerar bättre. // Finns INTE på canvas då uppgiften inte finns där

Uppgift 1: Räkna björkar
Ladda ner filerna (https://people.cs.umu.se/mbe/trad.csv och https://people.cs.umu.se/mbe/trad_dobelns_park.csv). Ni måste inte använda den stora filen alls, men den kan vara mer intressant.
Skriv en funktion som tar ett filnamn som argument, läser in innehållet i filen, och returnerar det som en lista rader. Skriv funktionen så att den rensar bort onödiga nyrader och den första raden som bara är instruktion.
Skriv en funktion is_birch(tree) som givet en sträng som beskriver ett träd som argument för parametern tree returnerar True om trädet är en björk, False för andra träd. Ni måste själva bestämma hur ni avgör om något är en björk, sådana som har ordet "björk" eller "Björk" i sitt svenska trädnamn är ett sätt.
Skriv sedan kod som med hjälp av dessa funktioner beräknar hur många björkar som filen innehåller.

Utveckla er kod med den mindre filen, ni kan sedan kontrollera sedan hur många björkar som förekommer i den större filen.

Uppgift 2: Överskatta antalet björkar

Problem! I stora filen (som är exakt som den är given på Umeå Kommuns sida) finns det ett antal träd som inte har någon information annat än plats. Vi vill inte underskatta hur många björkar det finns i staden. Uppdatera en av era funktioner för att räkna träd utan information om typ som om de vore björkar. Antingen kan inläsningsfunktionen fylla i 'Björk?' eller dylikt som typ för rader där trädet inte har en känd typ, eller så kan er funktion is_birch uppdateras för att ta detta i beräkning. Utan att modifiera resten av programmet, kör det igen för att få en ny siffra på antalet potentiella björkar som kommunen sköter.

Bonusuppgift: Mer problem! Det latinska namnet för rönn är "Sorbus Aucuparia", men det finns två träd i Umeå Kommuns data med det latinska namnet men Björk/Vårtbjörk som svenskt namn. Filtrera bort dessa, antingen genom att kontrollera för alla björkar att de har "Betula" som början på sitt latinska namn, eller genom att ignorera alla träd som har "Sorbus Aucuparia" som sitt latinska namn.

Uppgift 3: Bara de relevanta björkarna

Som stadsbo är det dock förstås inte så relevant med björkar långt bort, om man tittar i filen ser man att det finns björkar listade såväl i Sävar som Hörnefors, och där ute får de faktiskt reda sig själva. Låt oss filtrera vår sökning till de träd som finns i Umeå stad (lite grovt).

Skriv ytterligare två funktioner:

coords(tree) som givet en textsträng på filens format returnerar trädets x- och y-koordinater som en lista innehållande två flyttal.
dist(x1, y1, x2, y2) som returnerar avståndet mellan punkten (x1, y1) och punkten (x2, y2). Dra er här till minnes Pythagoras sats, vi vill alltså räkna ut: // Bild saknas

Notera att roten ur finns i Python som math.sqrt (så importera modulen math först). Den uppmärksamme kanske tycker detta blir ett konstigt mått, jorden är ju rund, och GPS-koordinater är i "grader"? Men Umeå är litet på jorden, så för nu räcker detta som ett grovt avstånd.

Exempelkörningar av funktionerna bör se ut så här (här representerar '>>>' Pythons prompt):

>>> coords("63.82300408270902, 20.269983819258425;Lövträd;Acer Platanoides;Skogslönn;Parkträd;")
[63.82300408270902, 20.269983819258425]
>>> dist(0.0, 2.0, 3.0, 4.0)
3.605551275463989

Notera att dessa returvärden är flyttal, inte strängar!

Använd dessa två funktioner för att räkna ut hur många björkar (med överskattningen från uppgift 2) som ligger inom 0.1 grader (så 0.1 avstånd) från Umeås logiska mittpunkt: fontänen framför MIT-huset, som ligger på koordinaterna (63.820560, 20.305810).

Uppgift 4: Mer struktur

Vi börjar ha en del funktionalitet för träd, dags att strukturera upp det lite! Skapa en klass för att representera träd. Ge den en konstruktor som tar en sträng på samma format som används i filen, och överför funktionerna is_birch, coords och dist till den. Uppdatera dem så att de där det är lämpligt använder attribut i objektet istället för de parametrar de hade i sin ursprungliga version. Fundera på vilka attribut ni vill att klassen skall ha, är det meningsfullt att spara de olika delarna från strängen i olika attribut?

Er klass har alltså formen:

class Tree:
    def __init__(self, tree_str):
        ...

Modifiera er inläsningsfunktion så att den nu producerar en lista av objekt av typen Tree istället.

Om tree är objektet som motsvarar första trädet i lilla filen bör alltså följande metodanrop fungera och ge dessa resultat:

>>> tree.is_birch()
False
>>> tree.dist(63.8204078, 20.3055167)
1766.8253646106925

Uppgift 5: Felhantering kan behövas

Fundera på var felhantering kan behövas i ert program, vad kan gå fel och varför? Vad är en lämplig hantering för hur programmet kan tänkas användas?

Uppgift 6: MIT-huset kanske inte universums centrum

När man tittar på den data vi har inser man att kommunen inte ansvarar för träden på universitetsområdet, närmsta björk från fontänen är en bit bort! Eller, ja, vilken är närmsta björk? Använd funktionerna och klassen ni redan konstruerat på lämpligt sätt för att ta reda på detta! Resultatet av denna uppgift skall alltså vara ett program som skriver ut ett enda träd, det närmaste fontänens koordinater.

Uppgift 7: Mer matematik

Pythagoras sats på en sfär är ju dock inte riktigt rätt, räta linjer kröker sig med jordens yta. Sfärisk geometri är förstås inte hemmaplan för många av oss, men så är det ofta i programmering: vi slår upp formeln, litar på att den stämmer, och implementerar den.

Koordinaterna i filen är i grader, men för trigonometri är det enklare med radianer. Vi behöver inte veta så mycket om dem, men modifiera er coord-funktion (utan att ändra något annat i programmet) så att den istället för  returnerar .
Modifiera sedan er dist-funktion så att den istället för Pythagoras som ovan använder formeln:

Alla funktionerna som krävs finns i biblioteket math, specifikt arccos (cosinus-invers) heter math.acos. Ni kommer troligen vilja bryta upp formeln över flera rader med variabler för de olika delarna för att hålla funktionen läsbar.

Vi behöver inte förstå exakt varför den här formeln är rätt för våra syften här (även om vi kan notera att 6371000 är jordens radie i meter, så det har med saken att göra). Detta gör dock funktioner och kommentarer viktiga, här gömmer vi den här komplicerade formeln i vår dist-funktion, och vi kan skriva en kort kommentar som talar om vad den ska göra, och möjligen var den kommer ifrån. Sedan kan vem som helst arbeta med träden och deras avstånd utan att vara en fena på sfärisk geometri.

Testa er funktion genom att beräkna hur långt bort det närmsta trädet från MIT-husets fontän faktiskt är (rätt svar är ungefär 270 meter, det är inte samma träd som med Pythagoras!).

Uppgift 8: Bonus, allt det andra

Med vår nya avståndsfunktion kan vi, utan att behöva ändra något annat i programmet, nu kontrollera vilken björk som är närmast fontänen. Det visar sig att avstånden är korta nog att det är samma björk! Men vi vet i alla fall hur många meter det är i verkligheten. Men, som utmaning, kan man titta på diverse annat:

Vilka två träd är längst ifrån varandra i databasen? Vilka är närmast?
Hur många av varje sorts träd finns det, sammanställda i en tabell?
Hur skulle man räkna ut den trädtätaste delen av staden?
Finns det ett mönster i vilken typ av träd kommunen väljer som parkträd kontra gatuträd?
Kan ni skriva ett enkelt menysystem för att låta en användare söka i databasen? 
Fotnot om koordinaterna

Notera att koordinaterna som finns i filen och vi jobbar med här alltså är longitud och latitud. Ni kan om ni vill validera era svar söka på dem på Google Maps eller annan karttjänst. T.ex. fontänen vid MIT: https://www.google.com/maps?q=63.820560,20.305810. Ni kan sedan också använda street view för att se om träd ni hittar faktiskt finns och ser ut att vara de ni väntar er.