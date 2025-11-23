# pessoa.py
from abc import ABC, abstractmethod

# --- Pilares POO: Abstração, Herança e Polimorfismo ---

# 1. Classe Base Abstrata (Abstração)
class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    @abstractmethod
    def exibir_perfil(self):
        """Método abstrato forçando a implementação nas subclasses (Polimorfismo)."""
        pass

# 2. Subclasse Professor (Herança e Polimorfismo)
class Professor(Pessoa):
    def __init__(self, nome, email, especialidade):
        # Herança: Chama o construtor da classe base Pessoa
        super().__init__(nome, email)
        self.especialidade = especialidade
    
    def criar_curso(self, nome_curso, descricao):
        # Lógica de criação de curso (associação com a classe Curso)
        return f"Professor {self.nome} criou o curso: {nome_curso}"

    def exibir_perfil(self):
        """Implementação específica do método abstrato (Polimorfismo)."""
        return f"Perfil do Professor: {self.nome} ({self.especialidade})"

# 3. Subclasse Aluno (Herança e Polimorfismo)
class Aluno(Pessoa):
    def __init__(self, nome, email, matricula):
        # Herança: Chama o construtor da classe base Pessoa
        super().__init__(nome, email)
        self.matricula = matricula
        # Encapsulamento: Lista privada para rastrear cursos
        self.__cursos_inscritos = [] 
    
    def inscrever_curso(self, curso):
        # Associa o aluno ao curso (Associação N:N)
        self.__cursos_inscritos.append(curso)
        print(f"{self.nome} inscrito no curso: {curso.nome}")

    def exibir_perfil(self):
        """Implementação específica do método abstrato (Polimorfismo)."""
        return f"Perfil do Aluno: {self.nome} (Matrícula: {self.matricula})"