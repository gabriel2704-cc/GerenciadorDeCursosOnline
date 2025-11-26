# gerenciador.py

class GerenciadorCursos:
    # --- Padrão Singleton ---
    # 1. Variável de classe para a instância única (privada)
    __instancia = None

    # 2. Construtor modificado para impedir instanciação direta
    def __init__(self):
        # Garante que só será instanciado uma vez
        if GerenciadorCursos.__instancia is not None:
            raise Exception("Esta classe é um Singleton! Use get_instancia() para acessá-la.")
        else:
            # --- Encapsulamento ---
            # Atributos privados para centralizar todos os dados do sistema
            self.__cursos = [] 
            self.__usuarios = [] 
            GerenciadorCursos.__instancia = self
    
    # 3. Método estático para fornecer o acesso global
    @staticmethod
    def get_instancia():
        """Retorna a instância única do Gerenciador (Singleton Access Point)."""
        if GerenciadorCursos.__instancia is None:
            GerenciadorCursos() # Cria a primeira e única instância
        return GerenciadorCursos.__instancia

    # Métodos de gerenciamento (Encapsulamento)
    def adicionar_curso(self, curso):
        self.__cursos.append(curso)
        print(f"Curso '{curso.nome}' adicionado ao catálogo.")
    #garante que, não importa quantas vezes ele seja chamado, 
    # ele sempre retorna a mesma e única instância que já está criada, 
    # atuando como o ponto de acesso global e seguro para o catálogo."

    def listar_cursos(self):
        return self.__cursos
    
    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' registrado.")