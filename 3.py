from datetime import datetime, timedelta


data_hora_atual = datetime.now()


nova_data = data_hora_atual - timedelta(days=10)

print("Data e hora 10 dias atrás:", nova_data.strftime("%D"))
