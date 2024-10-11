import random
import pandas as pd
from datetime import datetime, timedelta

num_records = random.randint(100, 500)
conti = [123, 234, 345, 545, 678]
azioni = ['BIN', 'BOUT', 'CIN', 'COUT']

rows = []

start_date = datetime(2024, 1, 1)
for _ in range(num_records):
    days_offset = random.randint(0, 365)
    date = start_date + timedelta(days=days_offset)

    cc = random.choice(conti) 
    act = random.choice(azioni) 
    mov = round(random.uniform(100, 1000), 2)

    if act in ['BOUT', 'COUT']:
        mov = -mov
    
    rows.append( [date, cc, mov, act] )

df = pd.DataFrame(rows, columns=["Data", "Conto", "Importo", "Azione"])
df = df.sort_values(by="Data").reset_index(drop=True)

df.to_csv("movimenti_bancari.csv", index=False)