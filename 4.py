from  datetime import datetime, timedelta

data_hora_atual = datetime.now()

nova_data_hora = data_hora_atual + timedelta(hours=3)



print("Horário após 3 horas:", nova_data_hora)
