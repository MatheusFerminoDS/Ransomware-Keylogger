# Ransomware & Keylogger — Python Security Lab

## Sobre o projeto

Projeto independente desenvolvido em Python para explorar conceitos de segurança da informação por meio de simulações controladas de ransomware e keylogger.

As atividades foram realizadas no Kali Linux, em ambiente local e controlado.

## Objetivos

- Compreender os princípios da criptografia simétrica.
- Implementar a criptografia e a descriptografia de arquivos de teste.
- Compreender o funcionamento básico de um programa de registro de entradas.
- Analisar riscos associados a malwares.
- Identificar medidas de prevenção e proteção.

## Tecnologias utilizadas

- Python 3
- Kali Linux
- Biblioteca Cryptography
- Git e GitHub

## Estrutura do projeto

```text
DIO-Ransomware-Keylogger/
├── documentacao/
│   ├── keylogger.md
│   └── ransomware.md
├── evidencias/
├── keylogger/
│   └── keylogger.py
├── laboratorio/
│   └── arquivos_teste/
│       ├── clientes.txt
│       ├── documento.txt
│       └── financeiro.txt
├── ransomware/
│   ├── teste_criptografia.py
│   ├── criptografia_arquivos.py
│   └── descriptografia.py
├── .gitignore
└── README.md
```

## 1. Simulação de Ransomware

Foi desenvolvida uma simulação de criptografia e recuperação de arquivos utilizando a biblioteca Cryptography e o mecanismo Fernet.

O exercício contempla:

- Geração e armazenamento de uma chave criptográfica.
- Leitura de um arquivo de teste.
- Criptografia do conteúdo.
- Armazenamento do resultado em um arquivo `.enc`.
- Descriptografia utilizando a chave correspondente.
- Verificação da integridade do conteúdo recuperado.

O arquivo original é preservado durante o processo.

### Execução

```bash
python ransomware/teste_criptografia.py
python ransomware/criptografia_arquivos.py
python ransomware/descriptografia.py
```

## 2. Simulador Didático de Keylogger

Foi desenvolvido um programa em Python que recebe entradas voluntárias pelo terminal e registra o conteúdo em um arquivo local, acompanhado de data e horário.

O exercício demonstra conceitos de:

- Recebimento de entradas com `input()`.
- Estruturas de repetição.
- Condições de encerramento.
- Registro de data e horário.
- Escrita e armazenamento local de informações.

O programa encerra quando o usuário digita `SAIR`.

**Limitação:** esta implementação é uma simulação didática. Não monitora o teclado globalmente, não captura credenciais, não opera ocultamente e não transmite informações pela rede.

### Execução

```bash
python keylogger/keylogger.py
```

## Instalação e configuração

Clone o repositório e acesse a pasta do projeto:

```bash
git clone URL_DO_REPOSITORIO
cd DIO-Ransomware-Keylogger
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale a dependência:

```bash
python -m pip install cryptography
```

## Segurança e limitações

Todas as atividades foram desenvolvidas em ambiente controlado, utilizando arquivos fictícios.

Esta implementação não possui mecanismos de propagação, exclusão de arquivos originais, execução oculta ou transmissão de dados para terceiros.

A chave criptográfica e os arquivos gerados durante os testes são mantidos localmente e não devem ser publicados no repositório.

## Medidas defensivas

- Backups offline e periódicos.
- Controle de permissões de arquivos.
- Antivírus e soluções EDR.
- Monitoramento de alterações suspeitas em arquivos.
- Atualização de sistemas e aplicações.
- Conscientização dos usuários.

## Documentação

- [Documentação da simulação de Ransomware](documentacao/ransomware.md)
- [Documentação do simulador de Keylogger](documentacao/keylogger.md)

## Autor

MatheusFerminoDS

Projeto independente desenvolvido em Python para explorar conceitos de segurança da informação por meio de simulações controladas de ransomware e keylogger.
