# Diagnóstico do Sistema de Empréstimo — João Paulo

---

## Problema 1 — O sistema aceita empréstimo com zero dias

- **O que a documentação diz:** Nos requisitos (RN02), está escrito que o prazo mínimo para um empréstimo deve ser de pelo menos 1 dia. Faz sentido, já que não existe empréstimo de zero dias.
- **O que o código faz:** Olhando no método `registrar()`, ele recebe o número de dias e já calcula direto a data de devolução, sem conferir se o valor informado é válido. Dá pra passar 0, -1, qualquer coisa.
- **Por que é um problema:** Se alguém digitar 0 dias, o empréstimo vai ter a data de devolução igual ao dia de hoje, e já vai aparecer como atrasado no dia seguinte. Isso não deveria ser possível.
- **(Já documentado? Não — eu que encontrei)**

---

## Problema 2 — Quando não tem atraso, o sistema não fala nada

- **O que a documentação diz:** No caso de uso UC03, passo 4, diz que quando não houver empréstimos em atraso, o sistema deveria mostrar a mensagem "Nenhum empréstimo em atraso".
- **O que o código faz:** O método `listar_atrasados()` simplesmente percorre a lista e imprime só os que estão atrasados. Se nenhum estiver atrasado, ele não imprime nada — fica em branco.
- **Por que é um problema:** Quem está usando não tem como saber se deu tudo certo e não tem atrasos ou se aconteceu algum problema. A tela fica em branco e isso confunde.
- **(Já documentado? Não — eu que encontrei)**

---

## Problema 3 — Não aparece confirmação quando registra um empréstimo

- **O que a documentação diz:** O requisito de interface RI02 pede que toda operação feita com sucesso mostre uma mensagem de confirmação clara para o usuário. O caso de uso UC01 também fala que o sistema deve exibir a data de devolução prevista.
- **O que o código faz:** Quando o empréstimo é registrado, a única coisa que aparece na tela é `[EMAIL] fulano@email.com — empréstimo até 2025-04-10`. Essa mensagem é a simulação do e-mail, não é uma confirmação para quem está operando o sistema.
- **Por que é um problema:** O atendente fica sem saber se realmente gravou o empréstimo ou não. A mensagem de e-mail não serve como confirmação porque é direcionada ao cliente, não ao operador do sistema.
- **(Já documentado? Não — eu que encontrei)**

---

## Problema 4 — Digitar opção errada no menu não mostra erro

- **O que a documentação diz:** O requisito RI03 diz que toda operação inválida deve mostrar uma mensagem de erro descritiva, sem fechar o sistema. O RNF02 também fala que mensagens de erro devem ser claras.
- **O que o código faz:** No `main()`, o menu só trata as opções 1, 2, 3 e 0. Se a pessoa digitar 9, "abc" ou qualquer outra coisa, o sistema simplesmente ignora e mostra o menu de novo, sem falar nada.
- **Por que é um problema:** O usuário não recebe nenhum aviso de que errou. Parece que o sistema travou ou que a opção não funcionou. Deveria aparecer algo como "Opção inválida, tente novamente".
- **(Já documentado? Não — eu que encontrei)**

---

## Problema 5 — O cálculo de multa está repetido em dois lugares

- **O que a documentação diz:** A própria equipe reconheceu esse problema na Tabela de Dívida Técnica do `projeto.md`, item DT04: "Cálculo de multa duplicado em dois métodos".
- **O que o código faz:** O mesmo bloco de código que calcula a multa com base no tipo de equipamento (notebook = R$10, projetor = R$15, cabo = R$2) aparece tanto no `devolver()` quanto no `listar_atrasados()`. É copia e cola.
- **Por que é um problema:** Se alguém precisar mudar o valor de uma multa, tem que lembrar de alterar nos dois métodos. Se esquecer de um, o sistema vai mostrar valores diferentes dependendo de onde consultar — um baita problema.
- **(Já documentado? Sim — DT04)**

---

## Problema 6 — E-mail e lógica de negócio estão tudo junto

- **O que a documentação diz:** A Tabela de Dívida Técnica no `projeto.md`, item DT03, aponta que a "Notificação misturada com lógica de negócio" é um problema de alta prioridade. A decisão DP03 também reconhece que usaram `print()` como substituto de e-mail.
- **O que o código faz:** Nos três métodos principais (`registrar()`, `devolver()` e `listar_atrasados()`), a linha que simula o envio de e-mail está grudada no meio do código de negócio, sem nenhuma separação.
- **Por que é um problema:** Se um dia o sistema precisar mandar e-mail de verdade, ou usar WhatsApp, vai ter que mexer dentro dos métodos de negócio. Também não dá para testar a lógica sem "disparar" o e-mail falso junto.
- **(Já documentado? Sim — DT03)**

---

## Problema 7 — Os dados ficam em variáveis globais, fora da classe

- **O que a documentação diz:** A Tabela de Dívida Técnica no `projeto.md`, item DT02, reconhece que as "Variáveis globais acessadas diretamente pela classe" são um problema de alta prioridade. O diagrama de classes do projeto também anota essa dependência.
- **O que o código faz:** As listas `equipamentos` e `emprestimos_registrados` são declaradas fora da classe `Sistema`, soltas no início do arquivo. A classe acessa e modifica essas listas diretamente, sem receber elas como parâmetro.
- **Por que é um problema:** Se alguém tentar criar dois sistemas ao mesmo tempo (por exemplo, para testes), os dois vão compartilhar os mesmos dados. Isso também faz com que não dê para testar os métodos isoladamente, violando o que o requisito RNF04 (testabilidade) pede.
- **(Já documentado? Sim — DT02)**
