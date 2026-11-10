# Simulador Didático de Keylogger

## 1. Objetivo

Desenvolver um programa em Python que demonstre, em ambiente controlado, o recebimento, registro e armazenamento local de entradas fornecidas voluntariamente pelo usuário.

## 2. Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **datetime:** biblioteca para registrar data e horário das entradas.
- **pathlib:** biblioteca para manipulação de caminhos e arquivos.

## 3. Funcionamento

O programa apresenta um campo de entrada no terminal e aguarda o usuário digitar uma mensagem.

Cada entrada é registrada em um arquivo chamado `registro.txt`, acompanhada da data e do horário.

O programa continua solicitando entradas até que o usuário digite `SAIR`.

## 4. Estrutura do código

| Recurso | Finalidade |
|---|---|
| `input()` | Receber entradas do usuário |
| `while True` | Manter o programa em execução |
| `if` | Verificar a condição de encerramento |
| `strip()` | Remover espaços externos |
| `upper()` | Padronizar letras maiúsculas |
| `break` | Encerrar o laço |
| `datetime.now()` | Obter data e horário |
| `open("a")` | Abrir o arquivo para acrescentar registros |
| `write()` | Gravar as entradas |

## 5. Resultado do teste

O programa foi executado no Kali Linux e recebeu uma entrada de teste.

Exemplo do conteúdo gerado em `keylogger/registro.txt`:

```text
[09/11/2026 21:17:48] teste
```

O encerramento automático também foi validado utilizando a palavra `sair`.

## 6. Limitações da implementação

Esta implementação é uma simulação didática, não um keylogger global.

- Registra somente entradas fornecidas voluntariamente no próprio terminal.
- Não monitora o teclado em outros programas.
- Não captura senhas ou credenciais.
- Não executa ocultamente.
- Não transmite informações pela rede.

## 7. Considerações de segurança

Um keylogger malicioso pode capturar informações sensíveis sem o conhecimento do usuário. Por isso, mecanismos de proteção incluem soluções antivírus e EDR, controle de permissões, monitoramento de processos e conscientização dos usuários.

Este exercício demonstra os princípios básicos de entrada, armazenamento e registro de informações em Python, mantendo a execução em ambiente controlado.
