from abc import ABC, abstractmethod

# Classe Base Abstrata para Abstração
class Conteudo(ABC):
    def __init__(self, titulo: str, duracao_min: int):
        self.titulo = titulo
        self.duracao_min = duracao_min

    @abstractmethod
    def exibir(self):
        """Método polimórfico para visualização do conteúdo."""
        pass

# Subclasse (Herança e Polimorfismo)
class VideoAula(Conteudo):
    def __init__(self, titulo: str, duracao_min: int, link_youtube: str):
        super().__init__(titulo, duracao_min)
        self.link_youtube = link_youtube

    def exibir(self):
        return f"[VÍDEO] {self.titulo} ({self.duracao_min} min). Link: {self.link_youtube}"

# Subclasse (Herança e Polimorfismo)
class Artigo(Conteudo):
    def __init__(self, titulo: str, duracao_min: int, num_paginas: int):
        super().__init__(titulo, duracao_min)
        self.num_paginas = num_paginas

    def exibir(self):
        return f"[ARTIGO] {self.titulo} ({self.num_paginas} páginas). Tempo estimado: {self.duracao_min} min."
    

# A Fábrica de Conteúdos (Factory Pattern)
class ConteudoFactory:
    """Responsável por criar objetos Conteudo (VideoAula ou Artigo)."""
    
    @staticmethod
    def criar_conteudo(tipo: str, titulo: str, duracao_min: int, **kwargs) -> Conteudo:
        """
        Recebe o tipo de conteúdo e os dados, e retorna a instância correta.
        """
        tipo = tipo.lower()
        
        if tipo == 'video':
            # Video requer o link_youtube (dado passado via kwargs)
            link = kwargs.get('link_youtube')
            if not link:
                 raise ValueError("Erro: Conteúdo 'video' requer 'link_youtube'.")
            return VideoAula(titulo, duracao_min, link)
            
        elif tipo == 'artigo':
            # Artigo requer o num_paginas (dado passado via kwargs)
            paginas = kwargs.get('num_paginas')
            if paginas is None:
                 raise ValueError("Erro: Conteúdo 'artigo' requer 'num_paginas'.")
            return Artigo(titulo, duracao_min, paginas)
            
        else:
            raise ValueError(f"Tipo de conteúdo desconhecido: {tipo}")