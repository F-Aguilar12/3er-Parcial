print("EJERCICIO DE NÓMINA")
#Solicitamos el pago del cliente, utilizamos float para un número con decimales
Pago_diario = float(input("¿Cuál es tu sueldo diario?: "))
#solicitaremos sobre los dias trabajados con "int" ya que sera sin decimales
Dias_lab = int(input("Introduce los dias laborados: "))
#continuamos solicitando informacion para poder recaudar datos para la nomina
Horas_extra = int(input("Introduce las horas extras que laboraste: "))
Horas_extras_pago = Pago_diario/Horas_extra
Dias_faltantes = int(input("¿Cuántos días faltaste?: "))
Faltas = Dias_faltantes*Pago_diario
Descuento_seguro = int(input("¿Cuántas personas tienes aseguradas?: "))
seguro = 3.150%(Pago_diario)*Descuento_seguro
print("Tu sueldo neto es de: ", Pago_diario*Dias_lab+Horas_extras_pago-Faltas-seguro)
