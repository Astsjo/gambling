# Fellog.md

1. Vad gick fel och varför?
    
    Medans jag lade till så att spelet började om och behöll ens poäng så att man kunde fortsätta så gav "cont" (continue) alltid ett True-värde, även om man valde alternativet som borde gjort det till ett False.
2. Hur löste du det?
    
    Innan så hade jag:

        "if cont_choice.lower() == "y" or "yes" or "j" or "ja"
    Men ändringen som behövdes göras var att den kollade varje en åt gången:

        "if (cont_choice.lower() == "y") or (cont_choice.lower() == "yes") or (cont_choice.lower() =="ja") or (cont_choice.lower() == "j"):"

3. Vad kommer du tänka på nästa gång?
    
    Kanske att lära mig "or" bättre, eller andra metoder för att förenkla eller liknande. 
    
<p>

___
<p>

1. Vad gick fel och varför?
    
    Ingen fel hände igentligen, utan jag insåg att det kunde bli ett fel. Den tidigare versionen så kunde poäng-variabeln gå in i negativa värden vilket förstör hela poängen med spelet eftersom om man inte har en begränsning så förlorar man nästan spel-delen med spelet.
2. Hur löste du det?
    
    Jag lade först och främst till en while-loop som körde så länge man hade mer poäng än 0, else gör så att den säger att användaren förlorar för att de inte har några poäng kvar. 
    Sen lade jag till en while-loop i början, den del som användaren väljer sin gissning och hur mycket de lägger på den, och en if-sats på slutet. If-satsen kollar efter att man gjort sina val om ens poäng kommer gå under noll ((poäng - mängd) > 0). Om det gör det så sätter den InvalidNumber till True och loopen börjar om efter att den säger till användaren att de kan inte välja mer än vad de har. Om det inte är under noll så sätter den InvalidNumber till False, loopen avslutas och spelet går vidare som normalt. 
3. Vad kommer du tänka på nästa gång?
    
    Jag vet inte om jag kommer faktiskt att tänka på någonting nästa gång kring det här. Det känns mer som en bug man fixar när man ser den än en man aktivt letar eller tänker på. 
    
<p>

___
<p>

Nytt:

    Lade till en affär-system med uppgraderingar och föremål åt användaren. Just nu finns inte många alternativ och det är alltid samma uppgraderingar.
Logg:

    Ett fel jag hade var att den print-ade mulitplikationsvärdet även om man inte hade råd. Det var så enkelt som att flytta vilken linje den stod på.
    Har även ändrad saker som istället för (y/n) har jag nu [Y/n] som mer följer en standard.
    Ändrade hur vinsten beräknas för att kunna använda nya affären. Istället för bara en fast värde använder den nu variabel.
    Lade till ett till alternativ vid förlust om man hade ett "get out of jail free" kort aktivt som gör så att man inte förlorar några poäng.
        
<p>

___
<p>

Nytt:

    Lade till en "utvecklar loggin" för att kunna använda fusk.
Logg:

    Hittade ett fel som gjorde så att man inte kunde starta om efter att ha 0 poäng kvar. Fixat genom att lägga till raden "cont = False" som stoppar while-loopen. Hittade också ett fel med kortet som gjorde så att den inte försvann när man använde den.
        
<p>

___
<p>

Nytt:

    Lade till ny meny för att göra allternativ istället. Bytt tidigare bitar till funktioner.
Logg:

    Det var problematiskt först att lägga till eftersom en bra del av koden behövdes skriva om för att kunna använda funktioner. Det gick till slut, med problem här och där, som huvudsakligen är löst nu. Förråd fungerar inte än eftersom det inte är tillagt, men härnäst kommer jag updatera det existerande föremålssystemet samt skapa ett nytt förrådsystem åt det.
        
<p>

___
<p>

Nytt:
    
    Föremål är tillbaka och förbättrad! Nu med ett nytt förråd där du kan se vilka föremål du har samt statestik och välja att använda de föremål du har.
Logg:

    Precis som förr var det tidskrävande, men i huvudsak en erfarenhetsproblem. Det mesta satt i antingen typos, slarvfel, eller med funktionerna. Det går aldrig att säga att ett spel är helt bugfri, men den fungerar rätt så stabilt just nu. 