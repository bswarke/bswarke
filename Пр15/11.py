from datetime import datetime

date_obj = datetime.strptime("2024-12-31", "%Y-%m-%d")
print(f"Day: {date_obj.day}, Month: {date_obj.month}, Year: {date_obj.year}")
