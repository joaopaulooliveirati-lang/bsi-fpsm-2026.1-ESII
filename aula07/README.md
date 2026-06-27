# Aula 7 — Testes automatizados

Sistema de hoje: um **placar de futebol** ⚽. A **teoria** e a **atividade** completas estão no **SIGAA** — esta aula é **assíncrona**.

## O que tem aqui
```
aula07/
├── placar.py         ← a função resultado() que você vai testar (NÃO mexa nela)
├── partida.py        ← exemplo da teoria: serviço com dependência injetável
└── test_placar.py    ← 1 teste de exemplo + um # TODO (a sua tarefa, Parte B)
```

## Como rodar os testes
No terminal do Codespaces (o `pytest` já vem instalado):
```bash
cd aula07
pytest
```
Você verá **`1 passed`**. Depois de completar a Parte B (o teste do empate), verá **`2 passed`**.

## A tarefa (resumo)
Complete, em `test_placar.py`, **um teste para o empate** (`resultado(1, 1) == "empate"`). O passo a passo está na **Parte B** (SIGAA).
