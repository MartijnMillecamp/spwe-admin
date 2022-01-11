def compare_excel_files(AanwezigDF, VerwachtDF):
    # Creeer id
    VerwachtDF['id'] = VerwachtDF['naam'] + VerwachtDF['voornaam'] + VerwachtDF['klas']
    AanwezigDF['id'] = AanwezigDF['naam'] + AanwezigDF['voornaam'] + AanwezigDF['klas']

    ################################################################################
    # Korte versie om iedereen te vinden die verwacht werd, maar niet aanwezig was #
    ################################################################################

    # Maak een lijst van alle leerlingen die aanwezig zijn
    AanwezigList = AanwezigDF['id'].to_list()

    # Zoek alle leerlingen die niet in die lijst zitten
    NietAanwezigDF = VerwachtDF.loc[VerwachtDF['id'].isin(AanwezigList) == False]

    return NietAanwezigDF