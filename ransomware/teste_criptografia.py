from cryptography.fernet import Fernet

# Gerar uma chave criptográfica
chave = Fernet.generate_key()

# Criar o mecanismo Fernet
fernet = Fernet(chave)

# Ler o arquivo original
with open("laboratorio/arquivos_teste/documento.txt", "rb") as arquivo:
    conteudo_original = arquivo.read()

# Criptografar o conteúdo
conteudo_criptografado = fernet.encrypt(conteudo_original)

# Descriptografar o conteúdo em memória
conteudo_recuperado = fernet.decrypt(conteudo_criptografado)

# Verificar se os dados foram recuperados corretamente
assert conteudo_original == conteudo_recuperado

print("Criptografia realizada!")
print("Descriptografia realizada!")
print("Integridade dos dados confirmada!")
print("Arquivo original preservado.")
