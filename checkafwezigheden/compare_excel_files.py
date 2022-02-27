import pandas as pd
def compare_excel_files(df_aanwezig, df_verwacht):
    df_aanwezig.columns= df_aanwezig.columns.str.lower()
    df_verwacht.columns= df_verwacht.columns.str.lower()
    

    ################################################################################
    # Korte versie om iedereen te vinden die verwacht werd, maar niet aanwezig was #
    ################################################################################

    # Maak een lijst van alle leerlingen die aanwezig zijn
    AanwezigList = df_aanwezig['client_no'].to_list()
    VerwachtList = df_verwacht['nummer'].to_list()
    print(len(AanwezigList), len(VerwachtList))

    # Zoek alle leerlingen die niet in die lijst zitten
    CorrectAanwezigDF = df_verwacht.loc[df_verwacht['nummer'].isin(AanwezigList) == True]
    NietAanwezigDF = df_verwacht.loc[df_verwacht['nummer'].isin(AanwezigList) == False]
    OnverwachtAanwezigDF = df_aanwezig.loc[df_aanwezig['client_no'].isin(VerwachtList) == False]
    return CorrectAanwezigDF, NietAanwezigDF, OnverwachtAanwezigDF

if __name__ == "__main__":
    df_verwacht = pd.read_excel('./checkafwezigheden/planning_elke_dag.xlsx', sheet_name='donderdag', usecols=['Klas', 'Naam', 'Voornaam', 'Nummer'])
    df_aanwezig = pd.read_excel('./checkafwezigheden/msAttendance_test.xls', sheet_name=0)
    [correct, stout, vreemd] = compare_excel_files(df_aanwezig, df_verwacht)
    print(stout)
