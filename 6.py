from datetime import datetime


data_str = "2024-12-03"

data_obj = datetime.strptime(data_str, "%Y-%m-%d")


print("Objeto datetime:", data_obj)
