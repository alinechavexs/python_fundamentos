# Carregando os logs do sistema
log_sistema = "ERRO: Falha de comunicação no sensor 04"

# Verifica se a palavra "ERRO" está presente no log
tem_erro = "ERRO" in log_sistema
print(f"Falha detectada no log? {tem_erro}")

sem_critico = "CRÍTICO" not in log_sistema
print(f"Sem nível crítico? {sem_critico}")

