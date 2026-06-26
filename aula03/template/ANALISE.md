# Análise — as 3 responsabilidades da classe `Academia` (v1.0)

**Sua tarefa (Parte 2 da atividade, 0,3):** responder com **suas palavras**
(2–4 frases por item), olhando o arquivo `academia.py` da pasta da aula.
Substitua cada `...` pela sua resposta.

---

## 1. Quais são as 3 responsabilidades grudadas na classe `Academia`?
Escreva no formato "a classe faz **X** e **Y** e **Z**": A classe Academia faz três coisas: calcula as regras do plano (regra) e recebe os inputs e mostra as opções pro usuário (tela) e envia as mensagens de boas vindas (notificação).

> ...

## 2. Aponte, no código, **uma linha** de cada responsabilidade
(diga o número da linha e cole o trecho)Linha de regra: valor = 100.0 | Linha de tela: nome = input("Nome do aluno: ") | Linha de notificação: print(f"[WhatsApp para... ")

- **Regra de negócio** (cálculo / contagem): linha ____ — `...`
- **Tela** (interface com o usuário): linha ____ — `...`
- **Notificação** (aviso ao aluno): linha ____ — `...`

## 3. Como o SRP separa essas responsabilidades?
Diga **em qual componente** cada responsabilidade passa a morar: A regra vai para AcademiaService; a tela vai para a apresentação (cli.py); a notificação vai para o Notificador.

> ...

## 4. Por que ficou melhor? Cite **um** RNF
(manutenibilidade, testabilidade **ou** extensibilidade — veja `docs/requisitos.md`)
e explique em 1–2 frases: A separação melhora a Testabilidade, pois podemos testar o cálculo das mensalidades sem precisar ficar digitando nada no terminal e sem enviar a notificação.

> ...
