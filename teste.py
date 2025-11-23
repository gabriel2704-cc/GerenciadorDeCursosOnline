# teste.py
from gerenciador import GerenciadorCursos
from pessoa import Professor, Aluno
from curso import Curso
from conteudo import ConteudoFactory

def configurar_sistema():
    """Cria e configura instâncias iniciais e demonstra o Singleton."""
    
    # 1. Demonstração do Singleton Pattern
    # Acessa o Gerenciador (Singleton)
    gerenciador = GerenciadorCursos.get_instancia()
    print("--- 1. Configuração do Sistema (Singleton) ---")
    print(f"Instância do Gerenciador: {gerenciador}")
    
    # Tentativa de obter a instância novamente (deve ser a mesma)
    outro_gerenciador = GerenciadorCursos.get_instancia()
    print(f"Instância é a mesma? {gerenciador is outro_gerenciador}\n")

    # 2. Criação de Usuários (Herança)
    print("--- 2. Criação de Usuários (Herança) ---")
    prof_oo = Professor("Vanessa Lago", "vanessa@faculdade.br", "POO e Padrões de Projeto")
    aluno_a = Aluno("João Silva", "joao@aluno.br", "2025001")
    aluno_b = Aluno("Maria Souza", "maria@aluno.br", "2025002")

    print(prof_oo.exibir_perfil())
    print(aluno_a.exibir_perfil())
    print("-" * 30)
    
    return gerenciador, prof_oo, aluno_a, aluno_b

def demonstrar_curso_e_factory(gerenciador, professor, aluno_a, aluno_b):
    """Demonstra o Encapsulamento, Composição e Factory Pattern."""
    
    # 3. Criação do Curso (Associação com Professor)
    curso_too = Curso("Tecnologia Orientada a Objetos", 
                      "Fundamentos e Padrões de Projeto", 
                      professor)
    gerenciador.adicionar_curso(curso_too)

    # 4. Adição de Conteúdo (Factory Pattern e Polimorfismo)
    print("\n--- 4. Adição de Conteúdo (Factory Pattern) ---")
    
    # Professor usa a Factory para criar um Vídeo
    curso_too.adicionar_conteudo(
        tipo='video',
        titulo="Introdução à Herança",
        duracao_min=30,
        link_youtube="youtube.com/heranca_oo" 
    )
    
    # Professor usa a Factory para criar um Artigo
    curso_too.adicionar_conteudo(
        tipo='artigo',
        titulo="Guia de Padrões: Singleton e Factory",
        duracao_min=15,
        num_paginas=8
    )

    # Tentativa de criar conteúdo inválido
    curso_too.adicionar_conteudo(tipo='quiz', titulo="Teste", duracao_min=10)


    # 5. Inscrição de Alunos (Associação N:N)
    print("\n--- 5. Inscrição de Alunos ---")
    aluno_a.inscrever_curso(curso_too)
    aluno_b.inscrever_curso(curso_too)
    
    # 6. Exibição do Curso (Encapsulamento e Polimorfismo)
    print(curso_too.exibir_detalhes())

    # Demonstra o Polimorfismo ao chamar exibir() em diferentes objetos Conteudo
    primeiro_conteudo = curso_too.get_conteudos()[0]
    print(f"Chamada Polimórfica: {primeiro_conteudo.exibir()}")

if __name__ == "__main__":
    gerenciador, prof_oo, aluno_a, aluno_b = configurar_sistema()
    demonstrar_curso_e_factory(gerenciador, prof_oo, aluno_a, aluno_b)