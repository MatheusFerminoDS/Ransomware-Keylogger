from cryptography.fernet import Fernet
from pathlib import Path

# Caminhos dos arquivos
original = Path("laboratorio/arquivos_teste/documento.txt")
criptografado = Path("laboratorio/arquivos_teste/documento.enc")
recuperado = Path("laboratorio/arquivos_teste/documento_recuperado.txt")
chave_path = Path("laboratorio/chave_teste.key")

# Ler o arquivo original
conteudo = original.read_bytes()

# Impedir a criptografia de arquivos vazios
if not conteudo:
    raise ValueError("O arquivo original está vazio. Teste cancelado.")

# Criar ou reutilizar a chave criptográfica
if chave_path.exists():
    chave = chave_path.read_bytes()
    print("Chave de laboratório existente carregada.")
else:
    chave = Fernet.generate_key()
    chave_path.write_bytes(chave)
    print("Nova chave criptográfica criada.")

# Criar o mecanismo Fernet
fernet = Fernet(chave)

# Criptografar o conteúdo
dados_protegidos = fernet.encrypt(conteudo)

# Salvar o arquivo criptografado
criptografado.write_bytes(dados_protegidos)

print("Arquivo criptografado e salvo!")

# Descriptografar em memória
dados_recuperados = fernet.decrypt(dados_protegidos)

# Salvar o arquivo recuperado
recuperado.write_bytes(dados_recuperados)

# Verificar integridade
assert original.read_bytes() == recuperado.read_bytes()

print("Arquivo recuperado com sucesso!")
print("Integridade confirmada!")
print("Arquivo original preservado!")
