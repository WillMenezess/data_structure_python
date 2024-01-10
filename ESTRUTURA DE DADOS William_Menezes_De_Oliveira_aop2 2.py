class Aluno:
    CapacidadeNotas = 3

    def __init__(self, nome, matricula):
        self.nome = str(nome)
        self.matricula = str(matricula)
        self.notas = [None] * Aluno.CapacidadeNotas

    def Insere_Notas(self, N1, N2, N3):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
        self.notas = N1, N2, N3

    def Computa_Media(self):
        Media = (self.N1 + self.N2 + self.N3) / 3
        return Media

    def __str__(self):
        return f'\nAluno: {str(self.nome)} \nMatricula: {self.matricula}\nMédia: {Aluno.Computa_Media(self):.0f}\n{"-" * 15}'


class FilaCircular:
    Capacidade = 10

    def __init__(self):
        self.data = [None] * FilaCircular.Capacidade
        self.size = 0
        self.first = -1
        self.last = -1

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def First(self):
        if self.size == 0:
            print(f'A fila está vazia')
            return None
        else:
            return self.data[self.first]

    def enqueue(self, e):
        if (self.last + 1) % FilaCircular.Capacidade == self.first:
            print('A fila está cheia')
        elif self.first == -1:
            self.first = 0
            self.last = 0
            self.data[self.last] = e
            self.size += 1
        else:
            self.last = (self.last + 1) % FilaCircular.Capacidade
            self.data[self.last] = e
            self.size += 1

    def dequeue(self):
        if self.first == -1:
            print('A fila está vazia')
            return None
        elif self.first == self.last:
            temp = self.data[self.first]
            self.first = -1
            self.last = -1
            self.size -= 1
            return temp
        else:
            temp = self.data[self.first]
            self.first = (self.first + 1) % FilaCircular.Capacidade
            self.size -= 1
            return temp


def exibir_fila(FilaCircular):
    fila = FilaCircular
    s = ' '
    if fila.first == -1:
        return f'A fila circular está vazia.\n'
    elif fila.last >= fila.first:
        for i in range(fila.first, fila.last + 1):
            s = s + str(fila.data[i]) + " "
    else:
        for i in range(fila.first, FilaCircular.Capacidade):
            s = s + str(fila.data[i]) + " "
        for i in range(0, fila.last + 1):
            s = s + str(fila.data[i]) + " "
    print(f'[ {s} ]')


print('1) Criar uma lista de 13 alunos(Aluno) com os atributos e computar suas respectivas médias')
print('-' * 100)
Aluno1 = Aluno("William", "01")
Aluno1.Insere_Notas(10, 10, 10)
Aluno2 = Aluno("João", "02")
Aluno2.Insere_Notas(5, 5, 5)
Aluno3 = Aluno("Maria", "03")
Aluno3.Insere_Notas(10, 5, 5)
Aluno4 = Aluno("Joana", "04")
Aluno4.Insere_Notas(8, 5, 2)
Aluno5 = Aluno("Vitor", "05")
Aluno5.Insere_Notas(9, 10, 3)
Aluno6 = Aluno("Abrantes", "06")
Aluno6.Insere_Notas(7, 3, 5)
Aluno7 = Aluno("Andreza", "07")
Aluno7.Insere_Notas(3, 4, 2)
Aluno8 = Aluno("Herica", "08")
Aluno8.Insere_Notas(5, 9, 2)
Aluno9 = Aluno("Luis", "09")
Aluno9.Insere_Notas(5, 10, 10)
Aluno10 = Aluno("Vanessa", "010")
Aluno10.Insere_Notas(10, 9, 5)
Aluno11 = Aluno("Julia", "011")
Aluno11.Insere_Notas(5, 4, 7)
Aluno12 = Aluno("Amauri", "012")
Aluno12.Insere_Notas(5, 10, 10)
Aluno13 = Aluno("Pedro", "013")
Aluno13.Insere_Notas(10, 6, 10)
Lista = [Aluno1, Aluno2, Aluno3, Aluno4, Aluno5, Aluno6, Aluno7, Aluno8, Aluno9, Aluno10, Aluno11, Aluno12, Aluno13]
for i in range(len(Lista)):
    print(Lista[i])

print('2) Criar uma fila(FilaCircular). Inserir na fila os 10 primeiros alunos da lista. Exibir os elementos da fila.(Lembrando que fila cabe no máximo 10 elementos)\n')

Fila = FilaCircular()
Fila.enqueue(Aluno1)
Fila.enqueue(Aluno2)
Fila.enqueue(Aluno3)
Fila.enqueue(Aluno4)
Fila.enqueue(Aluno5)
Fila.enqueue(Aluno6)
Fila.enqueue(Aluno7)
Fila.enqueue(Aluno8)
Fila.enqueue(Aluno9)
Fila.enqueue(Aluno10)
exibir_fila(Fila)
print('-' * 100)

print('3)Tentar Inserir mais um aluno(decimo primeiro aluno da lista) na fila e informar o que acontece\n')
print('Resposta: A fila informa que está cheia e retorna None\n')
print(Fila.enqueue(Aluno11))
print('-' * 100)

print('4)Remover 3 alunos da fila e exibir a fila')
print('Alunos removidos:')
print(Fila.dequeue())
print(Fila.dequeue())
print(Fila.dequeue())
print('-' * 20)
print('Fila Atualizada:')
exibir_fila(Fila)
print('-' * 100)

print('5) Adicionar mais 3 alunos (os 3 últimos da lista) na fila e exibir a fila\n')
Fila.enqueue(Aluno11)
Fila.enqueue(Aluno12)
Fila.enqueue(Aluno13)
exibir_fila(Fila)
