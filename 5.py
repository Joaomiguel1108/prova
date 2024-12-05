from datetime import datetime, timedelta


data_hora_atual = datetime.now()


nova_data_hora = data_hora_atual - timedelta(minutes=30)



print("Horário 30 minutos atrás:", nova_data_hora)
