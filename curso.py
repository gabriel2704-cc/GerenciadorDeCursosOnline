# Importa as classes necessárias dos outros módulos
from pessoa import Professor
from conteudo import Conteudo, ConteudoFactory # Usaremos a Factory aqui!

class Curso:
    """
    Representa um curso no sistema.
    Demonstra Encapsulamento ao gerenciar a lista de conteúdos.
    """
    def __init__(self, nome: str, descricao: str, professor: Professor):
        # Atributos internos (Encapsulamento)
        self.__nome = nome
        self.__descricao = descricao
        self.__professor = professor 
        self.__conteudo = [] # Lista de objetos Conteudo (Composição)
    
    @property
    def nome(self):
        """Getter para o nome do curso."""
        return self.__nome
    
    @property
    def professor(self):
        """Getter para o professor do curso."""
        return self.__professor

    # Método que usa o Factory Pattern para criar e adicionar conteúdo
    def adicionar_conteudo(self, tipo: str, titulo: str, duracao_min: int, **kwargs):
        """
        Cria um objeto Conteudo usando a Factory e o adiciona ao curso.
        """
        try:
            # Chama a Factory para criar o objeto correto
            novo_conteudo = ConteudoFactory.criar_conteudo(
                tipo=tipo, 
                titulo=titulo, 
                duracao_min=duracao_min, 
                **kwargs
            )
            self.__conteudo.append(novo_conteudo)
            print(f" Conteúdo '{titulo}' ({tipo}) adicionado ao curso '{self.__nome}'.")
        except ValueError as e:
            print(f" Erro ao adicionar conteúdo: {e}")
            
    def get_conteudos(self) -> list[Conteudo]:
        """Retorna a lista de conteúdos do curso."""
        return self.__conteudo
    
    def exibir_detalhes(self):
        detalhes = f"\n--- Detalhes do Curso: {self.__nome} ---\n"
        detalhes += f"Descrição: {self.__descricao}\n"
        detalhes += f"Ministrado por: {self.__professor.nome}\n"
        detalhes += "Conteúdos:\n"
        if self.__conteudo:
            for i, conteudo in enumerate(self.__conteudo):
                detalhes += f"  {i+1}. {conteudo.exibir()}\n" # Demonstra o Polimorfismo
        else:
             detalhes += "  Nenhum conteúdo adicionado ainda.\n"
        return detalhes