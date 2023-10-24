class SistemaBarbearia:
    def __init__(self):
        self.inventario = {}
        self.cortes_do_dia = {}
        self.receitas = 0
        self.despesas = 0

    def atualizar_inventario(self, item, quantidade, custo_unitario):
        if item in self.inventario:
            self.inventario[item]['quantidade'] += quantidade
        else:
            self.inventario[item] = {'quantidade': quantidade, 'custo_unitario': custo_unitario}

    def adicionar_corte(self, nome_corte, valor):
        if nome_corte in self.cortes_do_dia:
            self.cortes_do_dia[nome_corte] += valor
        else:
            self.cortes_do_dia[nome_corte] = valor

    def adicionar_receita(self, descricao, valor):
        self.receitas += valor
        if descricao in self.cortes_do_dia:
            self.cortes_do_dia[descricao] += valor
        else:
            self.cortes_do_dia[descricao] = valor

    def adicionar_despesa(self, descricao, valor):
        self.despesas += valor

    def calcular_lucro(self):
        lucro = self.receitas - self.despesas
        return lucro

    def gerar_relatorio(self):
        print("\nRelatório:")
        print("\nCortes do Dia:")
        self._print_table(self.cortes_do_dia)

        print("\nInventário:")
        self._print_table(self.inventario, headers=["Item", "Quantidade", "Custo Unitário"])

        print("\nReceitas Totais: R$", self.receitas)
        print("Despesas Totais: R$", self.despesas)
        print("Lucro Total: R$", self.calcular_lucro())

    def _print_table(self, data, headers=None):
        if headers:
            print(f"{headers[0]:<20} | {headers[1]:<12} | {headers[2]:<16}")
            print("-" * 50)
        for item, info in data.items():
            print(f"{item:<20} | {info.get('quantidade', 0):<12} | R${info.get('custo_unitario', 0):.2f}")


def main():
    barbearia = SistemaBarbearia()

    while True:
        print("\nSistema Barbearia")
        print("1. Atualizar Inventário")
        print("2. Adicionar Corte do Dia")
        print("3. Adicionar Receita")
        print("4. Adicionar Despesa")
        print("5. Gerar Relatório")
        print("6. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            item = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade: "))
            custo_unitario = float(input("Digite o custo unitário: "))
            barbearia.atualizar_inventario(item, quantidade, custo_unitario)
        elif escolha == '2':
            nome_corte = input("Digite o nome do corte: ")
            valor = float(input("Digite o valor do corte: "))
            barbearia.adicionar_corte(nome_corte, valor)
        elif escolha == '3':
            descricao = input("Digite a descrição da receita: ")
            valor = float(input("Digite o valor da receita: "))
            barbearia.adicionar_receita(descricao, valor)
        elif escolha == '4':
            descricao = input("Digite a descrição da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            barbearia.adicionar_despesa(descricao, valor)
        elif escolha == '5':
            barbearia.gerar_relatorio()
        elif escolha == '6':
            break
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    main()