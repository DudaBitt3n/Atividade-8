class Pessoa: #informações presentes tanto em estudante como em professor
    def __init__(self, nome, sobrenome, endereco, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.email = email

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome, endereco, email, filiacao, ra, segmento, curso, turma, user, senha):
        super().__init__(nome, sobrenome,endereco, email)
        self.filiacao = filiacao
        self.ra = ra
        self.segmento = segmento
        self.curso = [curso] if isinstance(curso, str) else curso
        self.turma = turma
        self.user = user
        self.__senha = senha
        self.ativo = True

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
        
    def adicionar_curso(self, novo_curso):
        if self.segmento == "Superior":
            if novo_curso not in self.cursos:
                self.cursos.append(novo_curso)
            else:
                print("O aluno já está matriculado neste curso.")
        else:
            print("Alunos do Ensino Médio não podem cursar mais de um curso.")
    
    def transferencia(self, novo_curso):
        if self.segmento == "EM" or "Ensino Médio":
            self.curso = novo_curso
            print (f"Você foi transferido para o curso: {novo_curso}")

        elif self.segmento == "Superior":
            self.curso = novo_curso
            print (f"Você foi transferido para o curso: {novo_curso}")

    def editar_aluno(self, novo_nome, novo_sobrenome, novo_endereco, nova_filiacao, novo_segmento, novo_email): 
        if novo_nome:
            self.nome=novo_nome
        if novo_sobrenome:
            self.sobrenome=novo_sobrenome
        if novo_endereco:
            self.endereco=novo_endereco
        if nova_filiacao:
            self.filiacao=nova_filiacao
        if novo_segmento:
            self.segmento=novo_segmento
        if novo_email:
            self.email=novo_email

    def desativar_estudante(self):
        self.ativa = False
        print(f"O aluno {self.nome} {self.sobrenome} foi desativado.")

    def ativar(self):
        self._ativo = True
        print(f"O aluno {self.nome} {self.sobrenome} foi ativado")

    def __str__(self):
        return f"Estudante: {self.nome} {self.sobrenome}, Curso: {self.curso}, Turma:{self.turma}, Segmento: {self.segmento}, RA:{self.ra}, Email: {self.email}"

class Professor (Pessoa):
    def __init__(self, nome, sobrenome, cpf, formacao, endereco, email, user, senha):
        super().__init__(nome, sobrenome, endereco, email)
        self.cpf = cpf
        self.formacao = formacao
        self.__user = user
        self.__senha = senha
        self.disciplinas = []
        self.turmas = []
        self.segmentos = []
        self.ativa = True

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def user(self):
        return self.__user
    
    @user.setter
    def senha(self, user):
        self.__user = user

    def adicionar_turma(self, turma, curso):
        self.turmas.append(turma)
        self.turmas.append(curso)

    def adicionar_disciplinas(self, disciplina):
        self.disciplinas.append(disciplina)

    def adicionar_segmentos(self, segmento):
        self.segmentos.append(segmento) 

    def editar_professor(self, novo_nome, novo_sobrenome, novo_email, novo_endereco, nova_formacao):
        if novo_nome:
            self.nome = novo_nome
        if novo_sobrenome:
            self.sobrenome = novo_sobrenome
        if novo_email:
            self.email = novo_email
        if novo_endereco:
            self.endereco = novo_endereco
        if nova_formacao:
            self.formacao = nova_formacao

    def desativar_professor(self):
        self.ativa = False
        print(f"Professor {self.nome} {self.sobrenome} foi desativado.")

    def ativar(self):
        self._ativo = True
        print(f"O professor {self.nome} {self.sobrenome} foi ativado")

    def __str__(self):
        return f"Professor: {self.nome} {self.sobrenome}, CPF: {self.cpf}, Formação:{self.formacao}, Disciplina(s):{self.disciplinas}, Turma(s): {self.turmas}, Segmento(s): {self.segmentos}"
    
class Turma:
    def __init__(self, nome, segmento, curso, ano_escolar):
        self.nome = nome
        self.segmento = segmento
        self.curso = curso
        self.ano_escolar = ano_escolar
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        self.ativa = True

    def adicionar_aluno(self, estudante):
        self.alunos.append(estudante)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def validar_turma(self):
        if self.segmento == "EM" and len(self.alunos) < 20:
            raise ValueError("Turma do Ensino Médio deve ter no mínimo 20 alunos.")
        elif self.segmento == "Superior" and len(self.alunos) < 5:
            raise ValueError("Turma do Ensino Superior deve ter no mínimo, 5 alunos.")
        
    def desativar(self):
        self._ativa = False

    def ativar(self):
        self._ativa = True
        
    def excluir_aluno(self, estudante):
            # Verifica se o aluno está na lista e o remove
            if estudante in self.alunos:
                self.alunos.remove(estudante)
                print(f"Aluno {estudante.nome} {estudante.sobrenome} removido com sucesso.")
            else:
                print(f"Aluno {estudante.nome} {estudante.sobrenome} não encontrado na turma.")

    def excluir_professor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            print(f"Professor {professor.nome} {professor.sobrenome} removido com sucesso.")
        else:
            print(f"Professor {professor.nome} {professor.sobrenome} não encontrado na turma.")
    

    def __str__(self):
        nomes_alunos = ", ".join([f"{aluno.nome} {aluno.sobrenome}" for aluno in self.alunos])
        nomes_professores = ", ".join([f"{professor.nome} {professor.sobrenome}" for professor in self.professores])
        return f"Turma: {self.nome} - {self.curso}, Segmento: {self.segmento}, Ano Escolar: {self.ano_escolar}, Alunos: {nomes_alunos}, Professor(es):{nomes_professores}"
    
class Disciplina:
    def __init__(self, nome, id_disciplina, descricao, segmento, professor):
        self.nome = nome
        self.id_disciplina = id_disciplina
        self.descricao = descricao
        self.segmento = segmento
        self.professor = professor
        self.ativa = True
        self.disciplinas = []

    def lista_disciplinas (self, id_disciplina):
        self.disciplinas.append(id_disciplina)

    def adicionar_segmento(self, segmento):
        self.segmentos.append(segmento)

    def editar_disciplina(self, nova_descricao, novos_segmentos, novo_professor):
        if nova_descricao:
            self.descricao = nova_descricao
        if novos_segmentos:
            self.segmentos = novos_segmentos if isinstance(novos_segmentos, list) else [novos_segmentos]
        if novo_professor:
            self.professor = novo_professor
        print("Você editou esta disciplina")

    def desativar_disciplina(self):
        self.ativa = False
        print(f"Disciplina {self.nome} foi desativada.")

    def __str__(self):
        return f"Disciplina: {self.nome}, Segmento(s): {self.segmento}, Descrição: {self.descricao}, Professor: {self.professor}"
 

#Testezinhos
#estudante1 = Estudante("Joao","Silva", "Rua dos Bobos, 0", "maedojoazinho@gmail.com","Dona Fulana", "1234567","EM", "Informática", "202", "joao.silva", "senhadojoao")

#turma1 = Turma("202", "EM", "Eletromecânica", "2° ano")

#professor1 = Professor("José", "Santos", "123.456.789-01","Licenciatura em História", "Rua dos Bobos, 01","josesantos@ifc.edu.br","jose.santos","senhadoze")

#disciplina1 = Disciplina (f"História", 1234, "Descrição da disciplina", "EM", {professor1.nome})

#estudante1.transferencia("Eletromecânica")
#print(estudante1)

#professor1.adicionar_disciplinas(disciplina1.nome)
#professor1.adicionar_segmentos("EM")
#professor1.adicionar_turma(turma1.nome, turma1.curso)
#professor1.editar_professor("Jose", "Souza", "zezao.souza@ifc.edu.br","Rua dos Bobos, 02", "Licenciatura em Historia")
#print(professor1)

#turma1.adicionar_aluno(estudante1)
#turma1.excluir_aluno(estudante1)
#turma1.adicionar_professor(professor1)
#turma1.excluir_professor(professor1)

#turma1.validar_turma()

#print(turma1)

#print(disciplina1)
