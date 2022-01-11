def compare_excel_files(df_aanwezig, df_verwacht):
    df_aanwezig.columns= df_aanwezig.columns.str.lower()
    df_verwacht.columns= df_verwacht.columns.str.lower()

    # Creeer id
    df_verwacht['id'] = df_verwacht['naam'] + df_verwacht['voornaam'] + df_verwacht['klas']
    df_aanwezig['id'] = df_aanwezig['naam'] + df_aanwezig['voornaam'] + df_aanwezig['klas']

    ################################################################################
    # Korte versie om iedereen te vinden die verwacht werd, maar niet aanwezig was #
    ################################################################################

    # Maak een lijst van alle leerlingen die aanwezig zijn
    AanwezigList = df_aanwezig['id'].to_list()

    # Zoek alle leerlingen die niet in die lijst zitten
    NietAanwezigDF = df_verwacht.loc[df_verwacht['id'].isin(AanwezigList) == False]

    return NietAanwezigDF