# Solicitando dados do veículo

combustivel = float(input("Quantidade de combustível: "))
pneus_calibrados = input("Os pneus estão calibrados? (sim/não)").lower().strip()
documento_ok = input("A documentação está em dia? (sim/não): ").lower().strip()

# Checagem indivídual (Retorna True ou False)
combustivel_suficiente = combustivel >= 10.0
pneus_ok = pneus_calibrados == "sim"
documento_regular = documento_ok == "sim"

# Combinação lógica para liberação da viagem
viagem_liberada = combustivel_suficiente and pneus_ok and documento_ok

# Apresentando o status e liberação da viagem
print("\n-----STATUS DE SEGURANÇA PARA A VIAGEM-----")
print(f"1. Combustível Suficiente (>=10L): {combustivel_suficiente}")
print(f"2. Pneus Calibrados: {pneus_ok}")
print(f"Documentação Regularizada: {documento_regular}")
print(f"\n VIAGEM LIBERADA: {viagem_liberada}")