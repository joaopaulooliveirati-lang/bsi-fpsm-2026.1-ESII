```mermaid
  classDiagram
    class Aluno {
      -id: int
      -nome: str
      -plano: str
      -checkins: int
    }
    
    class AlunoRepo {
      +salvar(aluno)
      +buscar_por_nome(nome)
      +listar()
    }
    
    class Notificador {
      +enviar(destinatario, mensagem)
    }
    
    class AcademiaService {
      +matricular(nome, plano)
      +fazer_checkin(nome)
    }
  
    AcademiaService ..> Aluno
    AcademiaService ..> AlunoRepo
    AcademiaService ..> Notificador
  ```