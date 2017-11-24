from django import forms
from .models import EmpresarialQuest
from django.utils import timezone
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput



class EmpresarialQuestForm(forms.ModelForm):

    cliente  = forms.CharField(label = "1) Cliente", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    risco_cep  = forms.CharField(label = "1) Endereço completo com CEP do risco e da matriz.", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    area_predios  = forms.CharField(label = "2) Metragem quadrada construída de cada prédio.", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    valor_estoque  = forms.CharField(label = "3) Qual o valor de estoque? (acabado ou insumo por local).", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    valor_maquinas  = forms.CharField(label = "4) Qual o valor de máquinas, móveis e utensílios em cada prédio? (ou ao todo se não for possível).", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc_vizinhanca  = forms.CharField(label = "5) Qual a vizinhança? (favor detalhar as atividades, distancia, etc..)", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    quant_extintores  = forms.CharField(label = "6) Fotos Aéreas, Projetos, Alvarás, Licenças, etc.., (favor enviar em arquivo)", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc_distrib_ext  = forms.CharField(label = "7) Quantidade de extintores?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc_hidrant  = forms.CharField(label = "8) Como ficam distribuídos.", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    cor_dutos  = forms.CharField(label = "9) Possui hidrantes, como ficam distribuídos?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    duto_ferro_aco  = forms.CharField(label = "10) Os dutos são pintados de vermelho? Os dutos são de ferro ou aço?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    quant_lt_reserv_incend  = forms.CharField(label = "11) Qual a quantidade de água (litros) no reservatório de incêndio?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    quant_agua_consum_local  = forms.CharField(label = "12) Qual a quantidade de água para consumo do local?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    para_raio_mod  = forms.CharField(label = "13) A empresa possui sistema de para-raios instalado? Qual o modelo?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    brigada_incendio  = forms.CharField(label = "14) Tem brigada de incêndio? Quantos homens e quais seus recursos?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc_material_protecao  = forms.CharField(label = "15) Outro material protecional? Descreva", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    dist_bombeiros  = forms.CharField(label = "16) Qual a distância do Corpo de Bombeiro?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    cameras_cftv  = forms.CharField(label = "17) Possui câmeras de CFTV? Quantas?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    onde_grava_img  = forms.CharField(label = "18) Onde são gravadas as imagens?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    vigilancia  = forms.CharField(label = "19) Possui vigilância 24h? Quantos homens a cada turno?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    empr_ext_monit  = forms.CharField(label = "20) Tem empresa externa de monitoramento?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    aluguel_predio  = forms.CharField(label = "21) Há aluguel de alguma parte ou prédio?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    valor_aluguel  = forms.CharField(label = "22) Qual valor do aluguel mensal?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    somatorio_desp_fixa  = forms.CharField(label = "23) Qual o somatório das despesas fixas? (folha, alugueis, contratos de manutenção e serviços gerais, etc.) MENSAL.", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    faturamento_mensal  = forms.CharField(label = "24) Qual o faturamento mensal dos últimos 12 meses?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    carga_luz_rua_emp  = forms.CharField(label = "25) Qual a carga de luz que entra da rua na empresa?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    quant_transformadores  = forms.CharField(label = "26) Quantos transformadores existem? Onde ficam? ", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    transf_carga_dist  = forms.CharField(label = "27) Os transformadores reduzem a energia de qual carga (rua) para quantos volts?  Qual a distribuição interna?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc_geradores  = forms.CharField(label = "28) Há geradores? Quantos e qual a capacidade? Funcionam a diesel? Quantos litros? Como armazenamo diesel?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    desc_inst_eletrica  = forms.CharField(label = "29) Toda a parte elétrica é isolada? Os fios ficam organizados, separados e  em dutos especiais?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    manutencao  = forms.CharField(label = "30) Qual a manutenção (interna, externa e periodicidade)? Quem faz?  ", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    padrao_quadro_luz  = forms.CharField(label = "31) O quadro de luz é no padrão ABNT (Fundo de Aço, limpo, organizado)?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    data_fund_emp  = forms.CharField(label = "32) Qual a data de fundação da empresa?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    atividade_princ_cliente  = forms.CharField(label = "33) Suas atividades e principais clientes?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    historico_acidente  = forms.CharField(label = "34) Qual a história de acidentes? Qual valor de prejuízo de cada um destes acidentes? O que foi feito para evitar novos acidentes?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    cob_ultimo_seguro  = forms.CharField(label = "35) Qual o valor e coberturas do último seguro (mandar cópia da apólice se for possível)?", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    seguro_negado  = forms.CharField(label = "36) Já teve alguma proposta de seguro negada, ou participou de algum processo de cotação nos últimos 06 meses?", widget=forms.TextInput(attrs={'class' : 'form-control'}))


    class Meta:
        model = EmpresarialQuest
        fields = (
        "cliente",
       "risco_cep",
       "area_predios",
       "valor_estoque",
       "valor_maquinas",
       "desc_vizinhanca",
       "quant_extintores",
       "desc_distrib_ext",
       "desc_hidrant",
       "cor_dutos",
       "duto_ferro_aco",
       "quant_lt_reserv_incend",
       "quant_agua_consum_local",
       "para_raio_mod",
       "brigada_incendio",
       "desc_material_protecao",
       "dist_bombeiros",
       "cameras_cftv",
       "onde_grava_img",
       "vigilancia",
       "empr_ext_monit",
       "aluguel_predio",
       "valor_aluguel",
       "somatorio_desp_fixa",
       "faturamento_mensal",
       "carga_luz_rua_emp",
       "quant_transformadores",
       "transf_carga_dist",
       "desc_geradores",
       "desc_inst_eletrica",
       "manutencao",
       "padrao_quadro_luz",
       "data_fund_emp",
       "atividade_princ_cliente",
       "historico_acidente",
       "cob_ultimo_seguro",
       "seguro_negado",
        "insert_date",
        )
