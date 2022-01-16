import pandas as pd
def compare_excel_files(df_aanwezig, df_verwacht, dag):
    df_aanwezig.columns= df_aanwezig.columns.str.lower()
    df_verwacht.columns= df_verwacht.columns.str.lower()
    df_verwacht_vandaag = df_verwacht[['klas', 'naam & voornaam', dag]]
    df_verwacht_vandaag.dropna(inplace=True)

    # Creeer id
    df_verwacht_vandaag['id'] = df_verwacht_vandaag['naam & voornaam'] + df_verwacht_vandaag['klas']
    df_aanwezig['id'] = df_aanwezig['client_name'] + df_aanwezig['division_descr']

    ################################################################################
    # Korte versie om iedereen te vinden die verwacht werd, maar niet aanwezig was #
    ################################################################################

    # Maak een lijst van alle leerlingen die aanwezig zijn
    AanwezigList = df_aanwezig['id'].to_list()
    VerwachtList = df_verwacht_vandaag['id'].to_list()

    # Zoek alle leerlingen die niet in die lijst zitten
    NietAanwezigDF = df_verwacht_vandaag.loc[df_verwacht_vandaag['id'].isin(AanwezigList) == False]
    NietAanwezigDF.drop('id', axis=1, inplace=True)

    return NietAanwezigDF

if __name__ == "__main__":
    df_verwacht = pd.read_excel('./checkafwezigheden/ReportMiddagmalenKeuzelijst.xls', sheet_name=0, header=2, skiprows=[0,1], usecols=['Klas', 'Naam & Voornaam', 'Maandag', 'Dinsdag', 'Donderdag', 'Vrijdag'])
    df_aanwezig = pd.read_excel('./checkafwezigheden/test_compare_excel.xls')
    niet_aanwezig = compare_excel_files(df_aanwezig, df_verwacht, 'maandag')
    print(niet_aanwezig)