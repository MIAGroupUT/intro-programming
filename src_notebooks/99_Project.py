# # Project
# In dit hoofdstuk werk je met behulp van Python een casus uit met echte patiëntendata. Gebruik hierbij de functies en modules die je eerder in de cursus bent tegengekomen.
#
# ## Inleiding
# Voor patiënten met type 1 of 2 diabetes is het belangrijk dat de bloedglucose goed gereguleerd is want dat beperkt de kans op ontwikkeling van macro- en microvasculaire complicaties. Er zijn meerdere manieren om de bloedglucose te monitoren:
# * **HbA1c:** Dat is een maat voor de hoeveelheid glucose dat zich in de afgelopen 3 maanden heeft opgestapeld in de rode bloedcellen. (Dit is niet hetzelfde als glucoseconcentratie in het bloed.)
# * **Bloedglucosemonitoring (BGM):** Diabeten die insuline gebruiken prikken dagelijks 4 a 6 keer: bij ontbijt, lunch, diner en soms bij de 2 tussendoortjes op een dag, en voor het slapen gaan. Daarnaast prikken ze ook wanneer er symptomen zijn van een hypo- of hyperglycemie. Met die prikken wordt bloedglucose gemeten.
# * Tegenwoordig gebruiken steeds meer diabeten een **continue glucosemeter (CGM)**, die, afhankelijk van het type, iedere 5 of 15 minuten een glucosemeting doet.
#
# Met de komst van de CGM hebben diabeten en hun behandelaren meer inzicht gekregen in de glucoseregulatie. Er zijn op basis daarvan nieuwe klinische CGM-parameters gedefinieerd (zie Tabel 1 en Figuur 1) en de verwachting is dat we daarmee de belangrijke maar moeilijker te bepalen HbA1c kunnen schatten.
# Voor deze opdracht maken we gebruik van open-source data van een studie$^{1}$ die onderzoekt of CGM zonder regelmatige vingerprik net zo veilig is als het gebruik van CGM met regelmatige vingerprik. Dit onderzoek is gedaan bij Type 1 diabetespatiënten. De CGM die de patiënten gebruiken tijdens dit onderzoek bepaalt iedere 5 minuten een glucosewaarde.

#
# **Tabel 1** Gebruikte variabelen en hun eenheid, doel en omschrijving.
# |             | Afkorting |Naam | Definitie | Doel | Eenheid |
# | :----- | :------ | :---- | :---------------- | :------ | :---- |
# | $g_{BGM}$|   BGM   | bloedglucosemonitoring| glucoseconcentratie (op onregelmatige tijden) |-| mmol/L|
# | $g_{CGM}$|   CGM   | continueglucosemonitoring| glucoseconcentratie (gemaakt door een continue glucosemeter) |-| mmol/L|
# | $h$|   HBA1c   | *hemoglobinA1c*| hoeveelheid glucose in bloedcel |-| mmol/L|
# | $h_{CGM}$|   eA1   | *extimated HbA1c*| schatting van HbA1c op basis van gemiddelde CGM |< 53| mmol/L|
# | $a$|   -   | -| - |-| 12.71 mmol/mol|
# | $b$|   -   | -| - |-| 4.70587 L/mol|
# | $p_{TAR}$|   TAR  | *time above range*| percentage van de tijd dat de CGM boven 10 mmol/L is | < 30| % |
# | $p_{TIR}$|   TIR  | *time in range*| percentage van de tijd dat de CGM tussen 3.9 en 10 mmol/L is| > 70| % |
# | $p_{TBR}$|   TBR  | *time below range*| percentage van de tijd dat de CGM onder 3.9 mmol/L is | < 5| % |

# ![My Image](https://surfdrive.surf.nl/files/index.php/s/qFua4yqda63motN/download)    
# **Figuur 1** Voorbeeld van een gestapelde staafdiagram van CGM-waarden (mmol/L) met hun doelen. Zo is in het ideale geval de TIR (percentage van de tijd dat 3.9 <CGM< 10) meer dan 70%. Zie ook tabel 1.

# ## Opdrachten
#
# :::{admonition} Opdracht 1
# :class: tip
# De gegevens zijn opgeslagen in het bestand `glucosedata.mat` dat je op Canvas kunt vinden. Om MATLAB of `.mat` bestanden in Python te openen kun je de `loadmat` functie van de `scipy.io` module gebruiken. Om de `scipy.io` module te kunnen gebruiken, moet je eerst `scipy` installeren via de volgende code:
#
# ```python
# conda install scipy
# ```
#
# Zoek zelf in de documentatie van SciPy op hoe de `loadmat` functie werkt. Zoals je ziet geeft deze functie een dictionary terug met daarin als key de naam van een variabele en als value de waarde daarvan. Schrijf in onderstaande cell code op de variabele `glucodat` te lezen. 

# +
import scipy.io
import numpy as np
from scipy.io import loadmat

# Laden van het bestand glucosedata.mat met functie loadmat
mat_contents = 

# Laad de variabele glucodat
glucodat = 

# +
import scipy.io
import numpy as np
from scipy.io import loadmat

# Laden van het bestand glucosedata.mat met functie loadmat
mat_contents = loadmat('C:/Users/veerl/Documents/Inleiding Programmeren/tm-introduction-programming/data/glucosedata.mat')

# De variabele glucodat 
glucodat = mat_contents['glucodat']
# -

# :::{admonition} Opdracht 2 
# :class: tip
# Achterhaal wat voor type de variabele `glucodat` is. Hiervoor kun je de `type` functie gebruiken die je eerder hebt geleerd. 
# Als het goed is zie je dat `glucodat` een NumPy structured array is met meerdere fields.  Zo te zien is "ID_293" de ID van de laatste patiënt. Bepaal in onderstaande cell code hoeveel patiënten er in totaal zijn?
# :::

# +
# Your code...

# +
# Type van de variabele glucodat
print(type(glucodat)) 

# Displaying the fields of glucodat
IDs = glucodat.dtype.names

# Het aantal patiënten is gelijk aan het aantal velden (fields) in glucodat
aantal_patienten = len(IDs)
print(f"Het totaal aantal patiënten is: {aantal_patienten}") # In totaal 131 patiënten
# -

# Iedere patiënt heeft een unieke ID. Voor elke patiënt zijn metingen van BGM en CGM en HbA1c opgeslagen. Voor de laatste patiënt is dat: 
#
# |.time|.data|
# | :-----:| :------: |
# |glucodat.ID_293.BGM.time  | glucodat.ID_293.BGM.data|
# |glucodat.ID_293.CGM.time | glucodat.ID_293.CGM.data|
# |glucodat.ID_293.HbA1c.time | glucodat.ID_293.HbA1c.data|
#
# Hier is **time** een vector van tijden, en **data** de bijbehorende meetwaarden. De BGM is vaak gemeten op onregelmatige tijden; de CGM zijn de continue glucosemetingen, meestal regelmatig gemeten. Van de HbA1c is per patiënt maar één meting uitgevoerd, maar de waarde is twee keer opgeslagen. Dat maakt het plotten ervan makkelijk:
# ```python
# import matplotlib.pyplot as plt
# patient_id = 'ID_293'
# time_component= glucodat[patient_id][0,0]['HbA1c'][0,0]['time'][0,0]
# data_component= glucodat[patient_id][0,0]['HbA1c'][0,0]['data'][0,0]
# plt.plot(time_component[0],data_component[0])
# ```
#
# De tijd is in dagen, de glucosedata (BGM, CGM) is in mmol/L, en de HbA1c is in
# mmol/mol. Per patiënt is er 3 maanden aan data geselecteerd. Patiënten hebben verschillende hoeveelheden BGM- en CGM-metingen gedaan. Daardoor is de
# data van iedere patiënt verschillend van lengte.
# Met een for-loop kun je door de patiënten lopen om, vervolgens, per patiënt
# de data te gebruiken: 
#
# ```python
# # Verkrijg een lijst van patient IDs
# IDs = list(IDs)
#
# # Loop door de ID lijst één voor één
# for patient_id in IDs:
#     # Hiermee kan je de data van de ... 
#     CGM_data = glucodat[patient_id][0,0]['CGM'][0,0]['data'][0,0]
#     # Doe iet met CGM       # ... CGM bereiken, en eriets mee doen
# ```
#

# ### Opdracht 3:
# Importeer `random` en gebruik de functie `random.sample()` om drie willekeurige patiënten te selecteren. Maak vervolgens in één figuur drie subplots (voor elke patiënt een subplot), en zet per patiënt in één subplot:
# 1. de CGM van de patiënt als functie van tijd,
# 2. de BGM van de patiënt als functie van tijd (gebruik stem in plaats van plot om het verschil met CGM beter te zien),
# 3. de gemiddelde bloedglucoseconcentratie g (mmol/L) van de patiënt geschat a.d.h.v. opgestapelde glucose in bloedcellen $h$ = HbA1c als
# <br>
# $g = \frac{h − a}{b}$
# <br>
# met $a$ = 12.71mmol/mol en $b$ = 4.70587L/mol.
#
# Voeg zinvolle titels, labels en legenda toe.

# +
# Your code...

# +
import matplotlib.pyplot as plt
import numpy as np
import random

# Definieer de parameters voor de schatting van de gemiddelde bloedglucoseconcentratie
a = 12.71  # mmol/mol
b = 4.70587  # L/mol

# Kies drie willekeurige patiënten
selected_patients=random.sample(IDs,3)

# Loop door de geselecteerde patiënten
plt.figure(figsize=(15, 5 * len(selected_patients)))

for i, patient_id in enumerate(selected_patients, start=1):
    # Haal de CGM, BGM en HbA1c data op voor de huidige patiënt
    CGM_time = glucodat[patient_id][0, 0]['CGM'][0, 0]['time'][0, 0]
    CGM_data = glucodat[patient_id][0, 0]['CGM'][0, 0]['data'][0, 0]

    BGM_time = glucodat[patient_id][0, 0]['BGM'][0, 0]['time'][0, 0]
    BGM_data = glucodat[patient_id][0, 0]['BGM'][0, 0]['data'][0, 0]

    HbA1c_time = glucodat[patient_id][0, 0]['HbA1c'][0, 0]['time'][0, 0]
    HbA1c_data = glucodat[patient_id][0, 0]['HbA1c'][0, 0]['data'][0, 0]

    # Plot alle waarden van de huidige patiënt in één subplot
    plt.subplot(len(selected_patients), 1, i)

    # Plot de CGM van de patiënt als functie van tijd
    plt.plot(CGM_time, CGM_data, label='CGM')
    
    # Plot de BGM van de patiënt als functie van tijd (gebruik stem)
    #plt.stem(bgm_time, bgm_data, label='BGM',linefmt ='pink',markerfmt ='D')
    plt.plot(BGM_time, BGM_data, label='BGM')
    
    # Bereken de geschatte gemiddelde bloedglucoseconcentratie g
    g_estimate = HbA1c_data - a / b

    # Plot de geschatte gemiddelde bloedglucoseconcentratie
    plt.plot(HbA1c_time[0], g_estimate[0], label='Gemiddelde glucoseconcentratie')

    # Zet labels en titel
    plt.title('Patient {}'.format(patient_id))
    plt.xlabel('Tijd(dagen)')
    plt.ylabel('Concentratie (mmol/L)')
    plt.legend()

plt.tight_layout()
plt.show()




# -

# ### Opdracht 4
# Wat valt je op aan de verschillende plots? Zijn er verschillen tussen patiënten?

# Jouw antwoord

# * Beschrijf verschil tussen de geschatte gemiddelde glucose concentratie en CGM en BGM: de De gemiddelde glucoseconcentratie geschat aan de hand van de opgestapelde glucose in de rode bloedcellen is significant hoger dan gemeten met CGM en BGM.
# * Beschrijf verschillen tussen CGM en BGM. De CGM toont meer uitschieters dan de BGM. BGM heeft ook minder meetpunten dat CGM.
# * Beschrijf verschillen tussen de patiënten. Bijvoorbeeld de verschillen tussen de lengte van de data. 

# **HbA1c vs klinische CGM parameters:** Nu gaan we HbA1c vergelijken met een paar klinische CGM-parameters. We onderscheiden vier parameters (per patiënt):
# * ***eA1c*** In opdracht 3 schatten we een gemiddelde glucoseconcentratie $g$ uit $h$ = HbA1c volgens de formule $g = \frac{h − a}{b}$. Omgekeerd kunnen we uit het gemiddelde $g_{cgm}$ van de CGM-metingen van de patiënt de  $h$ = HbA1c schatten volgens <br>
# <br>
# $h_{CGM} = a +b\overline{g}_{cgm}$       (mmol/mol)
# <br>
# <br>
# met $a$ = 12.71 mmol/mol en $b$ = 4.70587L/mol. Deze hCGM wordt eA1c genoemd (voor “estimated HbA1c”).
# * ***TAR***: Dit is het percentage samples van CGM hoger dan 10.0 mmol/L.
# * ***TIR***: Dit het percentage samples van CGM tussen de 3.9 en 10.0 mmol/L.
# * ***TBR***: Dit is het percentage samples van CGM kleiner dan 3.9 mmol/L.

# ### Opdracht 5:
# Maak een Python functie *Gluc_param* die voor een gegeven CGM signaal (van een patiënt) alle 4 parameters (eA1c, TAR, TIR, TBR) bepaalt.

# +
# Your code...

# +
def Gluc_param(CGM_signaal):
    # Constants voor de eA1c berekening
    a = 12.71
    b = 4.70587

    # Bereken eA1c
    eA1c = a + b * CGM_signaal.mean()

    # Bereken TAR, TIR, TBR percentages # KLOPT DIT OF MOET HET DELEN DOOR HET TOTAAL AANTAL SIGNALEN ZIJN
    tar_percentage = (CGM_signaal > 10.0).mean() * 100
    tir_percentage = ((CGM_signaal >= 3.9) & (CGM_signaal <= 10.0)).mean() * 100
    tbr_percentage = (CGM_signaal < 3.9).mean() * 100

    return eA1c, tar_percentage, tir_percentage, tbr_percentage

# Voorbeeldgebruik:
# Selecteer 1 patiënt
select_ID='ID_293'
CGM_signaal = glucodat[select_ID][0, 0]['CGM'][0, 0]['data'][0, 0]

# Roep de functie aan
eA1c, tar, tir, tbr = Gluc_param(CGM_signaal)

# Toon de resultaten
print(f"eA1c: {eA1c} mmol/mol")
print(f"TAR: {tar}%")
print(f"TIR: {tir}%")
print(f"TBR: {tbr}%")
# -

# De streefwaarde van HbA1c voor diabetespatiënten is < 53 mmol/mol. Voor de sommige patiënten is deze streefwaarde lastig te behalen. Nu willen we kijken hoe de verschillende HbA1c streefwaarden zich verhouden tot de CGM-parameters (eA1c, TAR, TIR, TBR). We onderscheiden drie groepen:
#
# |||
# | :-----:| :------: |
# |Patiëntgroep 1:  |  laag: HbA1c ≤ 53|
# |Patiëntgroep 2: |  midden: 53 < HbA1c < 63|
# |patiëntgroep 3: |  hoog: HbA1c ≥ 63|

# ### Opdracht 6: 
# Maak een *stacked bar chart*, waarbij de drie verschillende patiëntgroepen naast elkaar op de x-as staan, en, per patiëntgroep de gemiddelde TBR, TIR en TAR voor de patiëntgroep op elkaar gestapeld staan, een beetje zoals in Figuur 1. 
# <br>
# Hints: (i) Gebruik een for-loop om deze klinische parameters te bepalen
# voor alle patiënten en opslaan in één vector/matrix. (ii) Gebruik dezelfde for-loop om een vector met verschillende nummers voor de verschillende groepen te creeëren. (iii) Bereken de gemiddelde TBR, TIR en TAR, voor de verschillende groepen. (iv.) Maak een bar-graph met de functie **bar**. 

# +
# Your code...

# +
# 1: Sla alle klinische parametrs op in één matrix
Gluc_parameters=np.zeros((4,len(IDs)))
patient_groep = np.zeros(len(IDs))

for i, patient_id in enumerate(IDs):
    # Hiermee kan je de data van de ... 
    CGM_signaal = glucodat[patient_id][0,0]['CGM'][0,0]['data'][0,0]
    eA1c, tar, tir, tbr = Gluc_param(CGM_signaal)
    # Sla de parameters op in de matrix
    Gluc_parameters[:, i] = [eA1c, tar, tir, tbr]

# 2: Maak een vector met verschillende nummers voor de verschillende groepen
# Onderverdeel in patiëntgroepen op basis van eA1c
patient_groepen = np.where(Gluc_parameters[0, :] <= 53, 0, np.where(Gluc_parameters[0, :] < 63, 2, 1)) # Let op dat 
#je de middelste groep niet definieërd maar wel op plek 1 in de matrix zet!!

# 3: Bereken de gemiddelde TBR, TIR en TAr voor de verschillende groepen
# Lijsten voor het opslaan van gemiddelde waarden per groep
# bepaal de posities dat patient_groepen is gelijk aan groep 0
# Lijst met posities van elke patiëntgroep
posities_groepen = [np.where(patient_groepen == i)[0] for i in range(3)]

# Bereken gemiddelde waarden per groep
gemiddelde_tar = [np.mean(Gluc_parameters[1,posities]) for posities in posities_groepen]
gemiddelde_tir = [np.mean(Gluc_parameters[2,posities]) for posities in posities_groepen]
gemiddelde_tbr = [np.mean(Gluc_parameters[3,posities]) for posities in posities_groepen]

# Toon de resultaten
print("Gemiddelde TBR, TIR en TAR per patiëntgroep:")
print("Patiëntgroep 0 (Laag):")
print(f"TBR: {gemiddelde_tbr[0]}, TIR: {gemiddelde_tir[0]}, TAR: {gemiddelde_tar[0]}")
print("Patiëntgroep 1 (Midden):")
print(f"TBR: {gemiddelde_tbr[1]}, TIR: {gemiddelde_tir[1]}, TAR: {gemiddelde_tar[1]}")
print("Patiëntgroep 2 (Hoog):")
print(f"TBR: {gemiddelde_tbr[2]}, TIR: {gemiddelde_tir[2]}, TAR: {gemiddelde_tar[2]}")

# 4: Maak een bar-graph

# Patiëntgroepnamen
groepen = ['Laag', 'Midden', 'Hoog']

# Breedte van de bars
bar_breedte = 0.35

# Positie op de x-as voor elke groep
posities = np.arange(len(groepen))

# Maak de stacked bar chart
fig, ax = plt.subplots()
bar_tbr = ax.bar(posities - bar_breedte/2, gemiddelde_tbr, bar_breedte, label='TBR')
bar_tir = ax.bar(posities - bar_breedte/2, gemiddelde_tir, bar_breedte, label='TIR', bottom=gemiddelde_tbr)
bar_tar = ax.bar(posities - bar_breedte/2, gemiddelde_tar, bar_breedte, label='TAR', bottom=np.array(gemiddelde_tbr) + np.array(gemiddelde_tir))

# Voeg labels, titels en legenda toe
ax.set_xlabel('Patiëntgroepen')
ax.set_ylabel('Percentage')
ax.set_title('Gemiddelde TBR, TIR en TAR per patiëntgroep')
ax.set_xticks(posities)
ax.set_xticklabels(groepen)
ax.legend()

# Toon de plot
plt.show()


# -

# ### Opdracht 7:
# Wat valt op aan de resultaten? Welke groepen behalen de CGM parameterdoelen (zoals beschreven in Figuur 1).

# Jouw uitleg

# Een aantal zaken vallen op:
# * De groep TIR is percentueel het hoogste in de Lage en hoge groep. In de 'Midden' groep is TAR percentueel het hoogst.
# * Geen enkele groep behaald alle doelen. De groep 'Laag' wijkt wel het minste af. Alleen de TBR is hier 0.2% te hoog. 
# * Alleen de groep 'Laag' behaald een TIR > 70%. 
# * Opvallend dat de groep 'Midden' een hoger percentage TAR heeft dan de groep 'Hoog'. 

# **Moving average:** Het is je wellicht opgevallen dat de CGM-metingen als functie van tijd enorm fluctueren. Door de metingen te middelen over tijd ontstaat er een langzaam variërende functie van tijd, en die zegt vermoedelijk meer over HbA1c. Het langzaam variërende signaal construeren we met een “moving averaging” filter van orde $M$. Dat is een filter dat op basis van metingen $x_{1},x_{1},...,x_{n}$ het signaal $y_{1},y_{1},...,y_{n}$ bepaalt volgens de regel
# <br>
# <br>
# $y_{k}=\frac{1}{M+1}(x_{k},x_{k-1},...,x_{k-M}),   k=1,..,n$                                 
# <br>
# <br> Het getal $M$ wordt de "orde" van het filter genoemd. 
#

# ### Opdracht 8:
# Maak een Python functie movingav.m met syntax y=movingav(x,M) die uit een vector $x$ een vector $y$ bepaalt zoals gedefinieerd in (1). [Hint: Gebruik `np.convolve()` in mode=`same`]

# +

def movingav(x, M):
    """
    x: input vector
    M: orde van het filter

    Returns:
    y: output vector na toepassing van moving average filter
    """
    # Controleer of de orde M geldig is
    if M < 0:
        raise ValueError('Orde M moet een niet-negatief geheel getal zijn.')

    # Bepaal de coëfficiënten van het moving average filter
    b = np.ones(M + 1) / (M + 1)

    # Pas het filter toe op de inputvector x
    y = np.convolve(x, b, mode='same')

    return y


# -

# ### Opdracht 9:
# Controleer deze functie met onderstaande code, en leg uit waarom de plot klopt. 
# ```python
# x = np.array([0, 1, 1, 1, 1, 1])
# t = np.array([0, 1, 2, 3, 4, 5]);
# M = 2
# y = movingav(x, M)
# print(y)
#
# plt.stem(t,y) # ook wel "lollipop plot" genoemd
# plt.show()
# ```

# +
# Your code... + uitleg

# +
# Controle code
x = np.array([0, 1, 1, 1, 1, 1])
t = np.array([0, 1, 2, 3, 4, 5])
M = 2
y = movingav(x, M)
print(y)

plt.stem(t,y) # ook wel "lollipop plot" genoemd
plt.show()
# -

# Het filter heeft een windowsize van M + 1 oftewel 2 + 1 = 3. Het filter start in t=0 oftewel x=0 en omvat, met een windowsize van 3, de waarde x=0 en x=1. Om een output y van dezelfde lengte als input x te generen wordt een extra 0 toegevoegd. De berekening is nu als volgt: 1/3*(0 + 0 + 1) =  1/3. Vervolgens verschuift het filter 1 positie en wordt de volgende berekening uitgevoerd: 1/3*(0 + 1 +1) = 2/3. Etc. 

# ### Opdracht 10:
# Selecteer drie patiënten, en, per patiënt, maak een figuur met daarin een plot van de:
# * ongefilterde CGM data,
# * gefilterde CGM data (dus bepaald m.b.v. movingav)
# * de geschatte gemiddelde bloedglucoseconcentratie $g$ bepaald op basis van de HbA1c gegevens (zoals in opdracht 3(3))
#

# +
# Your code...

# +
# Kies drie willekeurige patiënten
selected_patients=random.sample(IDs,3)

# Bepaal filter orde
M=2

# Loop door de geselecteerde patiënten
plt.figure(figsize=(15, 5 * len(selected_patients)))

for i, patient_id in enumerate(selected_patients, start=1):
    # Haal de CGM, BGM en HbA1c data op voor de huidige patiënt
    CGM_time = glucodat[patient_id][0, 0]['CGM'][0, 0]['time'][0, 0]
    CGM_data = glucodat[patient_id][0, 0]['CGM'][0, 0]['data'][0, 0]
    
    flattened_cgm_data = CGM_data.flatten()
    CGM_filt = movingav(flattened_cgm_data, M)

    HbA1c_time = glucodat[patient_id][0, 0]['HbA1c'][0, 0]['time'][0, 0]
    HbA1c_data = glucodat[patient_id][0, 0]['HbA1c'][0, 0]['data'][0, 0]

    # Plot alle waarden van de huidige patiënt in één subplot
    plt.subplot(len(selected_patients), 1, i)

    # Plot de CGM van de patiënt als functie van tijd
    plt.plot(CGM_time, CGM_data, label='CGM')
    
    # Plot de BGM van de patiënt als functie van tijd (gebruik stem)
    plt.plot(CGM_time, CGM_filt, label='Gefilterd CGM')
    
    # Bereken de geschatte gemiddelde bloedglucoseconcentratie g
    g_estimate = HbA1c_data - a / b

    # Plot de geschatte gemiddelde bloedglucoseconcentratie
    plt.plot(HbA1c_time[0], g_estimate[0], label='Gemiddelde glucoseconcentratie')

    # Zet labels en titel
    plt.title('Patient {}'.format(patient_id))
    plt.xlabel('Tijd(dagen)')
    plt.ylabel('Concentratie (mmol/L)')
    plt.legend()

plt.tight_layout()
plt.show()

# -

# ### Opdracht 11: 
# Maak plaatjes met verschillende orde $M$ van het moving average filter. Filter bijvoorbeeld ook eens met grote orders, bijvoorbeeld het aantal samples voor een dag, of voor een week. Je mag er vanuit gaan dat de samplefrequentie 5/min is. Wat valt je op voor verschillende filter ordes?

# +
# Your code... + uitleg

# +
# Selecteer één willekeurige patiënt 
patient_id='ID_293'

# Gebruik meerdere ordes
dag_samp= round(24*60*0.2) # (uren*minuten*1/samp_freq)
week_samp= round(7*24*60*0.2) # (dagen*uren*minuten*1/samp_freq)
M_select=np.array([2,dag_samp,week_samp])

# Loop door de geselecteerde patiënten
plt.figure(figsize=(15, 5 * len(M_select)))

for i, M in enumerate(M_select, start=1):
    # Haal de CGM, BGM en HbA1c data op voor de huidige patiënt
    CGM_time = glucodat[patient_id][0, 0]['CGM'][0, 0]['time'][0, 0]
    CGM_data = glucodat[patient_id][0, 0]['CGM'][0, 0]['data'][0, 0]
    
    flattened_cgm_data = CGM_data.flatten()
    CGM_filt = movingav(flattened_cgm_data, M)

    HbA1c_time = glucodat[patient_id][0, 0]['HbA1c'][0, 0]['time'][0, 0]
    HbA1c_data = glucodat[patient_id][0, 0]['HbA1c'][0, 0]['data'][0, 0]

    # Plot alle waarden van de huidige patiënt in één subplot
    plt.subplot(len(M_select), 1, i)

    # Plot de CGM van de patiënt als functie van tijd
    plt.plot(CGM_time, CGM_data, label='CGM')
    
    # Plot de BGM van de patiënt als functie van tijd (gebruik stem)
    plt.plot(CGM_time, CGM_filt, label='Gefilterd CGM')
    
    # Bereken de geschatte gemiddelde bloedglucoseconcentratie g
    g_estimate = HbA1c_data - a / b

    # Plot de geschatte gemiddelde bloedglucoseconcentratie
    plt.plot(HbA1c_time[0], g_estimate[0], label='Gemiddelde glucoseconcentratie')

    # Zet labels en titel
    plt.title('Patient {}'.format(patient_id))
    plt.xlabel('Tijd(dagen)')
    plt.ylabel('Concentratie (mmol/L)')
    plt.legend()

plt.tight_layout()
plt.show()

# -

# Door een grotere orde (M) van het movingaverage filter wordt het sterk flunctuerende CGM signaal meer gemiddeld en dus vlakker. 

# ## Referenties
# **[1]**: *Aleppo G, Ruedy KJ, Riddlesworth TD, Kruger DF, Peters AL, Hirsch I, et al. REPLACE-BG: A Randomized Trial Comparing Continuous Glucose Monitoring With and Without Routine Blood Glucose Monitoring in Adults With Well-Controlled Type 1 Diabetes. Diabetes Care [Internet]. 2017 Apr 1 [cited 2021 Oct 4];40(4):538–45. Available from: https://care.diabetesjournals.org/content/40/4/538. Dataset beschikbaar vanaf: https://public.jaeb.org/datasets/diabetes.*


