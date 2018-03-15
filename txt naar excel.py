import pandas as pd

"""
Download de transacties bij 'Downloaden transacties' op de website van de Rabobank.
Gebruik bestandsformaat 'Kommagescheiden (.txt)
Run tot slot de code, let op dat je niet al 'transactions.xlsx' met Excel geopend hebt.
"""

df = pd.read_csv('transactions.txt'\
                 , sep=',', header=None, names=['eigenrekening', 'EUR', 'datum', 'CD', 'bedrag',
                                              'tegenrekening', 't.n.v.', 'datum', 'x2', 'x3', 'omschrijving',
                                              'x4', 'x5', 'x6', 'x7', 'x8','transactiereferentie',
                                              'incassantID', 'kenmerk machtiging'],
                 decimal=".")




def export_naar_excel():
    writer = pd.ExcelWriter('transactions.xlsx')
    df1.to_excel(writer, 'Transacties')
    writer.save()


def wijzig_format():
  for i in range(len(df)):
    if df['CD'][i] == 'D':  # 'Af' transactie
      df.set_value([i], 'CD', 'Af')
      df.set_value([i], 'bedrag', -1*df['bedrag'])
    if df['CD'][i] == 'C':  # 'Bij' transactie
      df.set_value([i], 'CD', 'Bij')
    jaar = str(df['datum'][i])[0:4]
    maand = str(df['datum'][i])[4:6]
    dag = str(df['datum'][i])[6:8]
    nieuw_data_format = dag+'-'+maand+'-'+jaar
    df.set_value([i], 'datum', nieuw_data_format)

wijzig_format()

# Maakt een nieuw dataframe met alleen de nuttige informatie
df1 = df[['datum', 't.n.v.', 'tegenrekening', 'omschrijving', 'bedrag']].copy()

export_naar_excel()
