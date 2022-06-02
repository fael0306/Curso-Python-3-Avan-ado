fotosagatha = {"Rafael","Rafaela","Sandra","Adriano","Alícia","Diego","Gabriel","Gui","Josi1","Josi2","Júnior","Mãe","Pai","Roland","Lourdes","Lourdes","Tio Rafael"}
mabame = {"Rafael","Adriano","Carla","Gabriel","Mãe","Nilza","Pai"}
maedeutsch = {"Rafael","Adriano","Diego","Gabriel","Mãe","Pai"}
trioparadadura = {"Rafael","Mãe","Pai"}
fammanteigabrde = {"Rafael","Adriano","Diego","Gabriel","Josi2","Júnior","Nilza","Rafaela","Lourdes","Tio Rafael","João Gabriel","Mãe"}
familiatrololo = {"Rafael","Gabriel","Mãe","Pai"}

grupoideal = sorted(fotosagatha | mabame | maedeutsch | trioparadadura | fammanteigabrde | familiatrololo)

print("")

for i in grupoideal: print(i)
print("\nQuantidade de pessoas: ",len(grupoideal))
