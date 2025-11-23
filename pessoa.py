from abc import ABC, abstractmethod

# 1. Classe Base Abstrata (Abstração)
class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    @abstractmethod
    def exibir_perfil(self):
        """Método abstrato para ser implementado pelas subclasses."""
        pass

# 2. Subclasse (Herança)
class Professor(Pessoa):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade
    
    def criar_curso(self, nome_curso, descricao):
        # Neste ponto, precisaremos instanciar um objeto Curso (próxima etapa)
        # Por enquanto, apenas retorna os dados:
        return f"Professor {self.nome} criou o curso: {nome_curso}"

    def exibir_perfil(self):
        """Implementação do método abstrato (Polimorfismo)."""
        return f"Perfil do Professor: {self.nome} ({self.especialidade})"

# 3. Subclasse (Herança)
class Aluno(Pessoa):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula
        self.cursos_inscritos = [] # Encapsulamento
    
    def inscrever_curso(self, curso):
        self.cursos_inscritos.append(curso)
        print(f"{self.nome} inscrito no curso: {curso.nome}")

    def exibir_perfil(self):
        """Implementação do método abstrato (Polimorfismo)."""
        return f"Perfil do Aluno: {self.nome} (Matrícula: {self.matricula})"