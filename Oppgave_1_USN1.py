"""Utregningen av utgifter av besinbil vs elbil. Jeg bruker eb for elbil, og bb for bensinbil"""
"""Starter med å regne ut utgiftene til elbil"""

#antar en kjørelengde på 10000 km til både elbil og bensinbil
kjørelengde = 10000
#felles verdi for trafikforsikring for elbil og bensinbil
trafikkforsikring_avgift = round(8.38 * 365)
#prisen til forsikring elbil
forsikring_eb= 5000

#variabelkostnader elbil, prisen på strøm når den har kjørt 10000 km
strompris_bruk_eb = 0.2 * kjørelengde * 2

#bomavgift elbil
bom_avgift_eb = 0.1 * kjørelengde

#her regnes totalkostnadene til elbil.Jeg ønsket en tekst som svar i tillegg til prisen
total_kostnader_eb= forsikring_eb + trafikkforsikring_avgift + strompris_bruk_eb + bom_avgift_eb

"""Her regnes ut kostnadene for bensinbil"""
forsikring_bb= 7500
drifstoff_bb= 1* kjørelengde

#Bomavgift til bensinbil
bomavgift_bb = 0.3* kjørelengde

total_kostnader_bb = forsikring_bb + trafikkforsikring_avgift + drifstoff_bb + bomavgift_bb
#diferanse på kostnadene til elbil og bensinbil
årlig_kostnadsdifferanse = round( total_kostnader_bb - total_kostnader_eb)

print ("Trafikkforsikring for elbil og bensinbil er:" , trafikkforsikring_avgift, "kroner")
print("Prisen på strøm elbil er:", strompris_bruk_eb, "kroner")
print("Bomavgift på elbil:" , bom_avgift_eb, "kroner")
print("De årlige kostnadene på elbil er:" , total_kostnader_eb , "kroner.")

print("De årlige kostnader på bensinbil er:" , total_kostnader_bb, "kroner")
print ("Bomavgiften på bensinbil er:", bomavgift_bb, "kroner")
print("De årlige kostnader på bensinbil er:" , total_kostnader_bb, "kroner")
print("Årlig kostnadsdifferanse mellom bensin bil og elbil er:", årlig_kostnadsdifferanse, "kroner.")

#Jeg skriver en kommentar som konklusjon til hva som er billigst
print ("Bensinbil er",  årlig_kostnadsdifferanse, "kroner dyrere enn elbil.")