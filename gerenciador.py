class GerenciadorCursos:
    # 1. Variável de classe para a instância única (privada)
    __instancia = None

    # 2. Construtor privado para impedir instanciação externa
    def __init__(self):
        if GerenciadorCursos.__instancia is not None:
            raise Exception("Esta classe é um Singleton! Use get_instancia() para acessá-la.")
        else:
            # Atributos internos (privados) para o Encapsulamento
            self.__cursos = []
            self.__usuarios = []
            GerenciadorCursos.__instancia = self
    
    # 3. Método estático para fornecer o acesso global
    @staticmethod
    def get_instancia():
        """Retorna a instância única do Gerenciador."""
        if GerenciadorCursos.__instancia is None:
            GerenciadorCursos() # Cria a primeira e única instância
        return GerenciadorCursos.__instancia

    # Métodos para gerenciar os dados (exemplo)
    def adicionar_curso(self, curso):
        self.__cursos.append(curso)
        print(f"Curso '{curso.nome}' adicionado ao catálogo.")

    def listar_cursos(self):
        return self.__cursos
    
    # Você adicionará métodos para gerenciar usuários aqui...

# Exemplo de uso do Singleton
# gerente = GerenciadorCursos()  # Isso irá gerar um erro!
# gerente1 = GerenciadorCursos.get_instancia()
# gerente2 = GerenciadorCursos.get_instancia()
# print(f"As instâncias são a mesma? {gerente1 is gerente2}")