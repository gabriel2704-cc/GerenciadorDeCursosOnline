
from abc import ABC, abstractmethod

# 1. Classe Base Abstrata
class Conteudo(ABC):
    def __init__(self, titulo: str, duracao_min: int):
        self.titulo = titulo
        self.duracao_min = duracao_min

    @abstractmethod
    def exibir(self):
        """Método polimórfico que será reescrito."""
        pass

# 2. Subclasses Concretas
class VideoAula(Conteudo):
    def __init__(self, titulo: str, duracao_min: int, link_youtube: str):
        super().__init__(titulo, duracao_min)
        self.link_youtube = link_youtube

    def exibir(self):
        return f"[VÍDEO] {self.titulo} ({self.duracao_min} min). Link: {self.link_youtube}"

class Artigo(Conteudo):
    def __init__(self, titulo: str, duracao_min: int, num_paginas: int):
        super().__init__(titulo, duracao_min)
        self.num_paginas = num_paginas

    def exibir(self):
        return f"[ARTIGO] {self.titulo} ({self.num_paginas} páginas). Tempo estimado: {self.duracao_min} min."
    
# --- Padrão Factory ---
class ConteudoFactory:
    """Implementa o Padrão Factory: cria objetos Conteudo sem expor a lógica de instanciação."""
    
    @staticmethod
    def criar_conteudo(tipo: str, titulo: str, duracao_min: int, **kwargs) -> Conteudo:
        """
        Método da Fábrica: decide qual classe concreta instanciar com base no parâmetro 'tipo'.
        """
        tipo = tipo.lower()
        
        if tipo == 'video':
            link = kwargs.get('link_youtube')
            if not link:
                 raise ValueError("Erro: Conteúdo 'video' requer 'link_youtube'.")
            # Retorna a instância de VideoAula
            return VideoAula(titulo, duracao_min, link)
            
        elif tipo == 'artigo':
            paginas = kwargs.get('num_paginas')
            if paginas is None:
                 raise ValueError("Erro: Conteúdo 'artigo' requer 'num_paginas'.")
            # Retorna a instância de Artigo
            return Artigo(titulo, duracao_min, paginas)
            
        else:
            raise ValueError(f"Tipo de conteúdo desconhecido: {tipo}")