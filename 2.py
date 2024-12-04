from datetime import datetime, timedelta


data_hora_atual = datetime.now()


nova_data = data_hora_atual + timedelta(days=5)

print(nova_data.strftime("%D"))
