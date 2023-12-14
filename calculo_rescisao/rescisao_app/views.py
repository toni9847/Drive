# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Funcionario
from .forms import FuncionarioForm
from datetime import datetime, timedelta

def calcular_rescisao(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    hoje = datetime.now().date()

    # Calcule o tempo de serviço em anos, meses e dias
    tempo_servico = hoje - funcionario.admissao
    anos_servico = tempo_servico.days // 365
    meses_servico = (tempo_servico.days % 365) // 30
    dias_servico = (tempo_servico.days % 365) % 30

    # Cálculos específicos para cada tipo de rescisão
    if  'demissao_sem_justa_causa':
        saldo_salario = funcionario.salario
        ferias_vencidas = calcular_ferias_vencidas(funcionario, hoje)
        ferias_proporcionais = calcular_ferias_proporcionais(funcionario, hoje)
        decimo_terceiro = calcular_decimo_terceiro(funcionario, hoje)
        aviso_previo = calcular_aviso_previo(funcionario, hoje)
        multa_fgts = calcular_multa_fgts(funcionario)

    elif 'demissao_com_justa_causa':
        saldo_salario = funcionario.salario
        ferias_vencidas = calcular_ferias_vencidas(funcionario, hoje)
        decimo_terceiro = calcular_decimo_terceiro(funcionario, hoje)
        aviso_previo = 0  # Não há aviso prévio em demissão com justa causa

    elif 'pedido_demissao':
        saldo_salario = funcionario.salario
        decimo_terceiro = calcular_decimo_terceiro(funcionario, hoje)
        ferias_vencidas = calcular_ferias_vencidas(funcionario, hoje)
        ferias_proporcionais = calcular_ferias_proporcionais(funcionario, hoje)
    
    # Resultado dos cálculos
    resultado = {
        'saldo_salario': saldo_salario,
        'ferias_vencidas': ferias_vencidas,
        'ferias_proporcionais': ferias_proporcionais,
        'decimo_terceiro': decimo_terceiro,
        'aviso_previo': aviso_previo,
        'multa_fgts': multa_fgts,
        # Adicione mais resultados conforme necessário...

    }
# Funções de cálculo específicas
def calcular_ferias_vencidas(funcionario, data_rescisao):
    # Implemente a lógica de cálculo para férias vencidas
    if data_rescisao >= funcionario.admissao + timedelta(days=365):
        # Calcula a proporção de férias vencidas
        anos_trabalhados = (data_rescisao - funcionario.admissao).days // 365
        ferias_vencidas = anos_trabalhados * 30  # Supondo 30 dias de férias por ano
        return ferias_vencidas
    else:
        return 0
    

def calcular_ferias_proporcionais(funcionario, data_rescisao):
    # Implemente a lógica de cálculo para férias proporcionais
    # Calcula a proporção de férias proporcionais
    meses_trabalhados = (data_rescisao - funcionario.admissao).days // 30
    ferias_proporcionais = meses_trabalhados * 2.5  # Supondo 2.5 dias de férias por mês
    return ferias_proporcionais
    

def calcular_decimo_terceiro(funcionario, data_rescisao):
    # Implemente a lógica de cálculo para o décimo terceiro
    # Calcula o décimo terceiro proporcional
    meses_trabalhados = (data_rescisao - funcionario.admissao).days // 30
    decimo_terceiro = (funcionario.salario / 12) * (meses_trabalhados / 12)
    return decimo_terceiro
    

def calcular_aviso_previo(funcionario, data_rescisao):
    # Implemente a lógica de cálculo para o aviso prévio
    # Calcula o aviso prévio proporcional
    anos_trabalhados = (data_rescisao - funcionario.admissao).days // 365
    if anos_trabalhados < 1:
        aviso_previo = funcionario.salario  # Aviso prévio de 30 dias
    else:
        aviso_previo = funcionario.salario * (anos_trabalhados + 1)  # Aviso prévio de 30 dias a cada ano trabalhado
    return aviso_previo
    

def calcular_multa_fgts(funcionario):
    # Implemente a lógica de cálculo para a multa do FGTS
     # Calcula a multa do FGTS (40% sobre o valor total depositado)
    multa_fgts = funcionario.salario * 0.4
    return multa_fgts
    
    return render(request, 'rescisao_app/calculo_rescisao.html', {'funcionario': funcionario, 'resultado': resultado})  
