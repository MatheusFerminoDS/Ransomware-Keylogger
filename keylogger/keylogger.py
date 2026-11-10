from datetime import datetime
from pathlib import Path

# Definir o arquivo onde as entradas serão registradas
arquivo_log = Path("keylogger/registro.txt")

print("=== Simulador didático de Keylogger ===")
print("Digite suas mensagens para registrá-las.")
print("Digite SAIR para encerrar o programa.")

# Iniciar a captura de entradas voluntárias
while True:

    entrada = input("Digite algo: ")

    # Verificar se o usuário deseja encerrar
    if entrada.strip().upper() == "SAIR":
        print("Captura encerrada.")
        break

    # Registrar data e horário
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Salvar a entrada no arquivo
    with arquivo_log.open("a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{horario}] {entrada}\n")

    print("Entrada registrada.")
