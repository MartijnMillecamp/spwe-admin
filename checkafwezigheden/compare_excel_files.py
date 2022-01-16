def compare_excel_files(df_aanwezig, df_verwacht, dag):
    df_aanwezig.columns= df_aanwezig.columns.str.lower()
    df_verwacht.columns= df_verwacht.columns.str.lower()
    print(df_verwacht)
    df_verwacht_vandaag = df_verwacht[['klas', 'naam & voornaam', dag]]
    df_verwacht_vandaag.dropna(inplace=True)

    # Creeer id
    df_verwacht['id'] = df_verwacht['naam & voornaam'] + df_verwacht['klas']
    df_aanwezig['id'] = df_aanwezig['client_name'] + df_aanwezig['division_descr']

    ################################################################################
    # Korte versie om iedereen te vinden die verwacht werd, maar niet aanwezig was #
    ################################################################################

    # Maak een lijst van alle leerlingen die aanwezig zijn
    AanwezigList = df_aanwezig['id'].to_list()

    # Zoek alle leerlingen die niet in die lijst zitten
    NietAanwezigDF = df_verwacht.loc[df_verwacht['id'].isin(AanwezigList) == False]

    return NietAanwezigDF