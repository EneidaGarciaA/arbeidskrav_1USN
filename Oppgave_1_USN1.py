"""utregningen av utgifter av besinbil vs elbil. Jeg bruker eb for elbil, og bb for bensinbil"""
"""utregningen av utgifter av besinbil vs elbil. Jeg bruker eb for elbil, og bb for bensinbil"""

"""starter med å regne ut utgiftene til elbil"""

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

"""her regnes ut kostnadene for bensinbil"""
forsikring_bb= 7500
drifstoff_bb= 1* kjørelengde

#Bomavgift til bensinbil
bomavgift_bb = 0.3* kjørelengde

print ("Felles kostnader traffikkforsikring elbil og bensinbil:", trafikkforsikring_avgift, "kroner.")
print("Pris strøm elbil:", strompris_bruk_eb, "kroner.")
print("Pris bomavgift elbil:", bom_avgift_eb, "kroner.")
print("De årlige kostnadene på elbil er:" , total_kostnader_eb , "kroner.")
print("Pris på drifstoff bensinbil:", drifstoff_bb, "kroner.")
print ("Pris på bomavgift bensinbil:", bomavgift_bb, "kroner.")

#totalkostnadene på bensinbil når den har kjørt 10000 km
total_kostnader_bb = forsikring_bb + trafikkforsikring_avgift + drifstoff_bb + bomavgift_bb
print("De årlige kostnader på bensinbil er:" , total_kostnader_bb, "kroner.")

#diferanse på kostnadene til elbil og bensinbil. Jeg skriver en kommentar som konklusjon til hva som er billigst
årlig_kostnadsdifferanse = round( total_kostnader_bb - total_kostnader_eb)
print ("Bensinbil er",  årlig_kostnadsdifferanse, "kroner dyrere enn elbil.")























print("Prisen på strøm elbil er:", strompris_bruk_eb, "kroner")
print ("Trafikkforsikring for elbil og bensinbil er:" , trafikkforsikring_avgift, "kroner")
print("Bomavgift på elbil:" , bom_avgift_eb, "kroner")

print("De årlige kostnadene på elbil er:" , total_kostnader_eb , "kroner.")
print ("Bomavgiften på bensinbil er:", bomavgift_bb, "kroner")
print("De årlige kostnader på bensinbil er:" , total_kostnader_bb, "kroner")
print ("Bensinbil er",  årlig_kostnadsdifferanse, "kroner dyrere enn elbil.")