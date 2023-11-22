import csv
from datetime import datetime
import pickle

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Barberia:
    def __init__(self):
        self.inventario = {}
        self.cortes = {}
        self.receitas = {}
        self.despesas = {}

    def atualizar_inventario(self, item, quantidade, custo_unitario):
        self.inventario[item] = (quantidade, custo_unitario)

    def adicionar_corte(self, nome_corte, valor_corte):
        self.cortes[nome_corte] = valor_corte

    def adicionar_receita(self, descricao, valor_receita):
        self.receitas[descricao] = valor_receita

    def adicionar_despesa(self, descricao, valor_despesa):
        self.despesas[descricao] = valor_despesa

    def gerar_relatorio(self):
        print('Relatório')
        print('Inventário:')
        for item, info in self.inventario.items():
            print(f'{item}: {info[0]} unidades x R$ {info[1]:.2f}')

        print('\nCortes:')
        for corte, valor in self.cortes.items():
            print(f'{corte}: R$ {valor:.2f}')

        print('\nReceitas:')
        for receita, valor in self.receitas.items():
            print(f'{receita}: R$ {valor:.2f}')

        print('\nDespesas:')
        for despesa, valor in self.despesas.items():
            print(f'{despesa}: R$ {-valor:.2f}')

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Inventário', '', '', ''])
            for item, info in self.inventario.items():
                writer.writerow([item, info[0], info[1], ''])

            writer.writerow(['', '', '', ''])
            writer.writerow(['Cortes', '', '', ''])
            for corte, valor in self.cortes.items():
                writer.writerow([corte, '', '', valor])

            writer.writerow(['', '', '', ''])
            writer.writerow(['Receitas', '', '', ''])
            for receita, valor in self.receitas.items():
                writer.writerow([receita, '', '', valor])

            writer.writerow(['', '', '', ''])
            writer.writerow(['Despesas', '', '', ''])
            for despesa, valor in self.despesas.items():
                writer.writerow([despesa, '', '', -valor])

    def carregar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                if linha[0] == 'Inventário':
                    continue
                elif linha[0] == '':
                    continue
                elif linha[1] == '':
                    self.cortes[linha[0]] = float(linha[3])
                elif linha[3] == '':
                    self.inventario[linha[0]] = (int(linha[1]), float(linha[2]))
                else:
                    self.receitas[linha[0]] = float(linha[3])
                    self.despesas[linha[0]] = -float(linha[3])


class BarberiaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='')
        layout.add_widget(self.label)

        btn_adicionar_inventario = Button(text='Adicionar item ao inventário')
        btn_adicionar_inventario.bind(on_press=self.adicionar_inventario)
        layout.add_widget(btn_adicionar_inventario)

        btn_adicionar_corte = Button(text='Adicionar corte')
        btn_adicionar_corte.bind(on_press=self.adicionar_corte)
        layout.add_widget(btn_adicionar_corte)

        btn_adicionar_receita = Button(text='Adicionar receita')
        btn_adicionar_receita.bind(on_press=self.adicionar_receita)
        layout.add_widget(btn_adicionar_receita)

        btn_adicionar_despesa = Button(text='Adicionar despesa')
        btn_adicionar_despesa.bind(on_press=self.adicionar_despesa)
        layout.add_widget(btn_adicionar_despesa)

        btn_gerar_relatorio = Button(text='Gerar relatório')
        btn_gerar_relatorio.bind(on_press=self.gerar_relatorio)
        layout.add_widget(btn_gerar_relatorio)

        btn_salvar_dados = Button(text='Salvar dados')
        btn_salvar_dados.bind(on_press=self.salvar_dados)
        layout.add_widget(btn_salvar_dados)

        btn_carregar_dados = Button(text='Carregar dados')
        btn_carregar_dados.bind(on_press=self.carregar_dados)
        layout.add_widget(btn_carregar_dados)

        return layout

    def adicionar_inventario(self, instancia):
        item = input('Digite o nome do item: ')
        quantidade = int(input('Digite a quantidade do item: '))
        custo_unitario = float(input('Digite o custo unitário do item: '))
        self.barberia.atualizar_inventario(item, quantidade, custo_unitario)
        self.label.text = f'Item {item} adicionado ao inventário'

    def adicionar_corte(self, instancia):
        nome_corte = input('Digite o nome do corte: ')
        valor_corte = float(input('Digite o valor do corte: '))
        self.barberia.adicionar_corte(nome_corte, valor_corte)
        self.label.text = f'Corte {nome_corte} adicionado'

    def adicionar_receita(self, instancia):
        descricao = input('Digite a descrição da receita: ')
        valor_receita = float(input('Digite o valor da receita: '))
        self.barberia.adicionar_receita(descricao, valor_receita)
        self.label.text = f'Receita {descricao} adicionada'

    def adicionar_despesa(self, instancia):
        descricao = input('Digite a descrição da despesa: ')
        valor_despesa = float(input('Digite o valor da despesa: '))
        self.barberia.adicionar_despesa(descricao, valor_despesa)
        self.label.text = f'Despesa {descricao} adicionada'

    def gerar_relatorio(self, instancia):
        self.barberia.gerar_relatorio()
        self.label.text = 'Relatório gerado'

    def salvar_dados(self, instancia):
        self.barberia.salvar_dados()
        self.label.text = 'Dados salvos'

    def carregar_dados(self, instancia):
        self.barberia.carregar_dados()
        self.label.text = 'Dados carregados'

class Barberia:
    def __init__(self):
        self.inventario = {}
        self.corte = {}
        self.receita = {}
        self.despesa = {}

    def atualizar_inventario(self, item, quantidade, custo_unitario):
        if item in self.inventario:
            self.inventario[item]['quantidade'] += quantidade
            self.inventario[item]['custo_unitario'] = custo_unitario
        else:
            self.inventario[item] = {'quantidade': quantidade, 'custo_unitario': custo_unitario}

    def adicionar_corte(self, nome_corte, valor_corte):
        self.corte[nome_corte] = valor_corte

    def adicionar_receita(self, descricao, valor_receita):
        self.receita[descricao] = valor_receita

    def adicionar_despesa(self, descricao, valor_despesa):
        self.despesa[descricao] = valor_despesa

    def gerar_relatorio(self):
        print('Relatório:')
        print('Inventário:')
        for item, info in self.inventario.items():
            print(f'Item: {item} | Quantidade: {info["quantidade"]} | Custo unitário: {info["custo_unitario"]}')
        print('Cortes:')
        for corte, valor in self.corte.items():
            print(f'Corte: {corte} | Valor: {valor}')
        print('Receitas:')
        for receita, valor in self.receita.items():
            print(f'Receita: {receita} | Valor: {valor}')
        print('Despesas:')
        for despesa, valor in self.despesa.items():
            print(f'Despesa: {despesa} | Valor: {valor}')

    def salvar_dados(self):
        with open('barberia_dados.pickle', 'wb') as arquivo:
            pickle.dump(self, arquivo)

    def carregar_dados(self):
        try:
            with open('barberia_dados.pickle', 'rb') as arquivo:
                barberia_carregada = pickle.load(arquivo)
                self.inventario = barberia_carregada.inventario
                self.corte = barberia_carregada.corte
                self.receita = barberia_carregada.receita
                self.despesa = barberia_carregada.despesa
        except FileNotFoundError:
            print('Não foi possível carregar os dados')

if __name__ == '__main__':
    barberia = Barberia()
    app = BarberiaApp()
    app.run()