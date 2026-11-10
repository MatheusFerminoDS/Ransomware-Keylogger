from cryptography.fernet import Fernet, InvalidToken
from pathlib import Path

# Definir os caminhos
arquivo_criptografado = Path("laboratorio/arquivos_teste/documento.enc")
arquivo_recuperado = Path("laboratorio/arquivos_teste/documento_recuperado.txt")
chave_path = Path("laboratorio/chave_teste.key")

# Verificar se os arquivos necessários existem
if not arquivo_criptografado.exists():
    raise FileNotFoundError("Arquivo criptografado não encontrado.")

if not chave_path.exists():
    raise FileNotFoundError("Chave criptográfica não encontrada.")

# Carregar a chave salva
chave = chave_path.read_bytes()

# Inicializar o mecanismo Fernet
fernet = Fernet(chave)

# Ler os dados criptografados
dados_protegidos = arquivo_criptografado.read_bytes()

# Descriptografar os dados
try:
    dados_recuperados = fernet.decrypt(dados_protegidos)
except InvalidToken:
    raise ValueError("Não foi possível descriptografar. Verifique a chave e o arquivo.")

# Salvar o conteúdo recuperado
arquivo_recuperado.write_bytes(dados_recuperados)

print("Descriptografia realizada com sucesso!")
print(f"Arquivo recuperado: {arquivo_recuperado}")
