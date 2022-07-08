def CalcularNomina(salario, bonoc, auxt):
    salarioE = salario + bonoc + auxt
    return salarioE

def nominaTotal(listaEmpleados, retencion):
    total = 0
    for empleado in listaEmpleados:
        salario = empleado["SALARIO"]
        bonoc = empleado["BONOC"]
        auxt = empleado["AUXT"]
        total += CalcularNomina(salario, bonoc, auxt)
    
    return total * (1 - retencion / 100) 

import json
with open("salarios.json") as file:
    empresa = json.load(file)
print(nominaTotal(empresa["NOMINA"],10))
