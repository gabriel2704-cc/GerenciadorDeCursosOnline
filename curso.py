# curso.py
from pessoa import Professor
from conteudo import Conteudo, ConteudoFactory

class Curso:
    """
    Representa um curso no sistema. Demonstra Encapsulamento e Composição.
    """
    def __init__(self, nome: str, descricao: str, professor: Professor):
        # --- Encapsulamento ---
        # Atributos privados controlados por métodos/properties
        self.__nome = nome
        self.__descricao = descricao
        self.__professor = professor 
        # Composição: Lista privada de objetos Conteudo
        self.__conteudo = [] 
    
    # Propriedades (Getters) para acesso controlado
    @property
    def nome(self):
        return self.__nome
    
    @property
    def professor(self):
        return self.__professor

    # Método que usa o Factory Pattern
    def adicionar_conteudo(self, tipo: str, titulo: str, duracao_min: int, **kwargs):
        """
        Cria um objeto Conteudo usando a Factory (desacoplamento) e o adiciona ao curso.
        """
        try:
            # Chama a Factory, não importa se é VideoAula ou Artigo
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
        """Retorna a lista de conteúdos (acesso controlado)."""
        return self.__conteudo
    
    def exibir_detalhes(self):
        detalhes = f"\n--- Detalhes do Curso: {self.__nome} ---\n"
        # ... (Resto do código de exibição)
        detalhes += "Conteúdos:\n"
        if self.__conteudo:
            for i, conteudo in enumerate(self.__conteudo):
                # Polimorfismo em ação: chama o exibir() de VideoAula ou Artigo
                detalhes += f"  {i+1}. {conteudo.exibir()}\n" 
        else:
             detalhes += "  Nenhum conteúdo adicionado ainda.\n"
        return detalhes