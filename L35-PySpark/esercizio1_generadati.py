import random
import pandas as pd
from datetime import datetime, timedelta

# Parametri
num_records = random.randint(10, 50)  # Numero casuale di record
accounts = [1001, 1002, 1003, 1004, 1005]  # 5 conti possibili
actions = ["BIN", "BOUT", "CIN", "COUT"]

# Generazione dei dati
data_records = []

start_date = datetime(2024, 1, 1)  # Data iniziale
for _ in range(num_records):
    days_offset = random.randint(0, 365)
    date = start_date + timedelta(days=days_offset)
    
    account = random.choice(accounts)
    action = random.choice(actions)
    
    if action in ["BIN", "CIN"]:
        amount = round(random.uniform(100, 10000), 2)  # Importi positivi
    else:
        amount = round(random.uniform(-10000, -100), 2)  # Importi negativi
    
    data_records.append([date, account, amount, action])

# Creazione DataFrame ordinato per data
df = pd.DataFrame(data_records, columns=["Data", "Conto", "Importo", "Azione"])
df = df.sort_values(by="Data").reset_index(drop=True)

# Salvataggio in un file CSV
csv_file = "./movimenti_bancari.csv"
df.to_csv(csv_file, index=False)

csv_file
