# Simulação Didática de Ransomware

## 1. Objetivo

Desenvolver uma simulação em Python dos princípios de criptografia e descriptografia de arquivos, utilizando a biblioteca Fernet, em um ambiente de laboratório controlado.

O objetivo é compreender como arquivos podem ser protegidos por criptografia e como recuperá-los utilizando a chave correta.

## 2. Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Cryptography:** biblioteca responsável pelas operações criptográficas.
- **Fernet:** mecanismo de criptografia simétrica autenticada.
- **Pathlib:** biblioteca para manipulação de caminhos e arquivos.

## 3. Funcionamento

O projeto possui dois programas principais:

### 3.1 Criptografia — criptografia_arquivos.py

1. Define o caminho do arquivo de teste.
2. Verifica se o conteúdo original não está vazio.
3. Carrega uma chave existente ou gera uma nova.
4. Criptografa o conteúdo utilizando Fernet.
5. Salva o resultado em um arquivo `.enc`.
6. Realiza uma recuperação em memória para validar a operação.

O arquivo original é preservado.

### 3.2 Descriptografia — descriptografia.py

1. Verifica a existência do arquivo criptografado.
2. Verifica a existência da chave.
3. Carrega a chave armazenada.
4. Lê os dados criptografados.
5. Realiza a descriptografia.
6. Salva o conteúdo recuperado em um arquivo `.txt`.

## 4. Estrutura do laboratório

```text
ransomware/
├── teste_criptografia.py
├── criptografia_arquivos.py
└── descriptografia.py

laboratorio/
├── chave_teste.key
└── arquivos_teste/
    ├── documento.txt
    ├── documento.enc
    └── documento_recuperado.txt
```

## 5. Validação dos resultados

A execução foi realizada no Kali Linux.

O funcionamento foi validado por três verificações:

- Execução bem-sucedida da criptografia.
- Recuperação do conteúdo utilizando a chave armazenada.
- Comparação entre o arquivo original e o recuperado por meio do comando `cmp`.

O comando `cmp` não apresentou diferenças, confirmando que os arquivos eram idênticos byte a byte.

## 6. Segurança da chave criptográfica

A chave é armazenada separadamente no arquivo `chave_teste.key`.

Foi utilizada a permissão `600`, configurada pelo comando:

```bash
chmod 600 laboratorio/chave_teste.key
```

Essa configuração restringe a leitura e escrita ao proprietário do arquivo.

A chave é indispensável para recuperar os dados e não deve ser compartilhada publicamente.

## 7. Considerações de segurança

O exercício demonstra conceitos utilizados em ataques de ransomware, especialmente a criptografia de arquivos e a necessidade de uma chave para recuperação.

Esta implementação é uma simulação didática, não um ransomware operacional.

Ela não possui propagação, exclusão de arquivos originais, criptografia indiscriminada de diretórios ou comunicação com atacantes.

Medidas defensivas importantes incluem backups offline, controle de permissões, antivírus, soluções EDR, monitoramento de alterações em arquivos e conscientização dos usuários.
