    Sistema de Gerenciamento de Cursos Online (E-Learning)
Este projeto implementa um sistema de gerenciamento de cursos online em Python, aplicando os quatro pilares da Programação Orientada a Objetos (POO) e dois Padrões de Projeto (Factory e Singleton).

     Objetivo
O objetivo principal é simular as interações básicas de uma plataforma de e-learning, como a criação de usuários, a estruturação de cursos e a adição de diferentes tipos de conteúdo, focando na aplicação de design patterns para garantir modularidade e flexibilidade.

     Modelagem UML (Diagrama de Classes)
O sistema foi planejado utilizando o Diagrama de Classes UML.
![DiagramaUML](https://github.com/user-attachments/assets/be937203-96c1-47d9-be39-a8b511e95173)


     Aplicação dos Pilares da POO
O projeto demonstra os pilares da POO nas seguintes classes:

Abstração: As classes Pessoa e Conteudo (ambas abstratas) definem a estrutura essencial, escondendo os detalhes de como um usuário ou um item de curso funciona internamente.

Herança:

Professor e Aluno herdam de Pessoa.

VideoAula e Artigo herdam de Conteudo.

Polimorfismo: O método exibir() é definido na classe Conteudo e é implementado de forma diferente em VideoAula e Artigo.

Encapsulamento: A classe Curso e GerenciadorCursos usam atributos internos protegidos, garantindo que o acesso e a modificação de dados internos sejam feitos apenas através de métodos públicos.

     Padrões de Projeto Aplicados
1. Factory Pattern (Obrigatório)
Classe: ConteudoFactory

Explicação: É usado para criar instâncias de VideoAula ou Artigo. O código cliente pede um tipo de conteúdo para a Fábrica, e ela retorna o objeto concreto correto, eliminando a dependência direta nas subclasses.

2. Singleton Pattern (Adicional)
Classe: GerenciadorCursos

Explicação: Garante que haja apenas uma instância dessa classe em todo o sistema. Ele atua como o catálogo central, onde todas as listas de cursos e usuários são armazenadas e acessadas globalmente.

     Instruções para Execução e Testes
O projeto é executado através do script principal main.py, que simula a configuração do sistema, a criação de usuários e a adição de conteúdo.

Pré-requisitos
Python 3.x

Estrutura de Arquivos
GerenciadorDeCursosOnline/
├── gerenciador.py
├── pessoa.py
├── conteudo.py
├── curso.py
└── main.py 
Como Rodar
Clone o repositório (ou use a cópia local já existente).

Execute o script principal:
python main.py


