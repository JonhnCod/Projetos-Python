segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400
resto = segundos % 86400
horas = (resto) // 3600
minutos = ((resto)% 3600)//60
segundofinal = ((resto)% 3600)%60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundofinal,"segundos.")

