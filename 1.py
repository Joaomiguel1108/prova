from datetime import time

data = time(23,53,15)

data_formatada = data.strftime("%H:%M:%S")

print(data_formatada)
