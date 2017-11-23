from django import forms
from .models import EmpresarialQuest
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput



class EmpresarialQuestForm(forms.ModelForm):


    risco_cep  = forms.CharField(label = "1) Endereço completo com CEP do risco e da matriz.", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    area_predios  = forms.CharField(label = "2) Metragem quadrada construída de cada prédio.", widget=forms.TextInput(attrs={'size': '70'}))
    valor_estoque  = forms.CharField(label = "3) Qual o valor de estoque? (acabado ou insumo por local).", widget=forms.TextInput(attrs={'size': '70'}))
    valor_maquinas  = forms.CharField(label = "4) Qual o valor de máquinas, móveis e utensílios em cada prédio? (ou ao todo se não for possível).", widget=forms.TextInput(attrs={'size': '70'}))
    desc_vizinhanca  = forms.CharField(label = "5) Qual a vizinhança? (favor detalhar as atividades, distancia, etc..)", widget=forms.TextInput(attrs={'size': '70'}))
    quant_extintores  = forms.CharField(label = "6) Fotos Aéreas, Projetos, Alvarás, Licenças, etc.., (favor enviar em arquivo)", widget=forms.TextInput(attrs={'size': '70'}))
    desc_distrib_ext  = forms.CharField(label = "1) Quantidade de extintores?", widget=forms.TextInput(attrs={'size': '70'}))
    desc_hidrant  = forms.CharField(label = "2) Como ficam distribuídos.", widget=forms.TextInput(attrs={'size': '70'}))
    cor_dutos  = forms.CharField(label = "3) Possui hidrantes, como ficam distribuídos?", widget=forms.TextInput(attrs={'size': '70'}))
    duto_ferro_aco  = forms.CharField(label = "4) Os dutos são pintados de vermelho? Os dutos são de ferro ou aço?", widget=forms.TextInput(attrs={'size': '70'}))
    quant_lt_reserv_incend  = forms.CharField(label = "5) Qual a quantidade de água (litros) no reservatório de incêndio?", widget=forms.TextInput(attrs={'size': '70'}))
    quant_agua_consum_local  = forms.CharField(label = "6) Qual a quantidade de água para consumo do local?", widget=forms.TextInput(attrs={'size': '70'}))
    para_raio_mod  = forms.CharField(label = "7) A empresa possui sistema de para-raios instalado? Qual o modelo?", widget=forms.TextInput(attrs={'size': '70'}))
    brigada_incendio  = forms.CharField(label = "8) Tem brigada de incêndio? Quantos homens e quais seus recursos?", widget=forms.TextInput(attrs={'size': '70'}))
    desc_material_protecao  = forms.CharField(label = "9) Outro material protecional? Descreva", widget=forms.TextInput(attrs={'size': '70'}))
    dist_bombeiros  = forms.CharField(label = "10) Qual a distância do Corpo de Bombeiro?", widget=forms.TextInput(attrs={'size': '70'}))
    cameras_cftv  = forms.CharField(label = "1) Possui câmeras de CFTV? Quantas?", widget=forms.TextInput(attrs={'size': '70'}))
    onde_grava_img  = forms.CharField(label = "2) Onde são gravadas as imagens?", widget=forms.TextInput(attrs={'size': '70'}))
    vigilancia  = forms.CharField(label = "3) Possui vigilância 24h? Quantos homens a cada turno?", widget=forms.TextInput(attrs={'size': '70'}))
    empr_ext_monit  = forms.CharField(label = "4) Tem empresa externa de monitoramento?", widget=forms.TextInput(attrs={'size': '70'}))
    aluguel_predio  = forms.CharField(label = "1) Há aluguel de alguma parte ou prédio?", widget=forms.TextInput(attrs={'size': '70'}))
    valor_aluguel  = forms.CharField(label = "2) Qual valor do aluguel mensal?", widget=forms.TextInput(attrs={'size': '70'}))
    somatorio_desp_fixa  = forms.CharField(label = "3) Qual o somatório das despesas fixas? (folha, alugueis, contratos de manutenção e serviços gerais, etc.) MENSAL.", widget=forms.TextInput(attrs={'size': '70'}))
    faturamento_mensal  = forms.CharField(label = "4) Qual o faturamento mensal dos últimos 12 meses?", widget=forms.TextInput(attrs={'size': '70'}))
    carga_luz_rua_emp  = forms.CharField(label = "1) Qual a carga de luz que entra da rua na empresa?", widget=forms.TextInput(attrs={'size': '70'}))
    quant_transformadores  = forms.CharField(label = "2) Quantos transformadores existem? Onde ficam? ", widget=forms.TextInput(attrs={'size': '70'}))
    transf_carga_dist  = forms.CharField(label = "3) Os transformadores reduzem a energia de qual carga (rua) para quantos volts?  Qual a distribuição interna?", widget=forms.TextInput(attrs={'size': '70'}))
    desc_geradores  = forms.CharField(label = "4) Há geradores? Quantos e qual a capacidade? Funcionam a diesel? Quantos litros? Como armazenamo diesel?", widget=forms.TextInput(attrs={'size': '70'}))
    desc_inst_eletrica  = forms.CharField(label = "5) Toda a parte elétrica é isolada? Os fios ficam organizados, separados e  em dutos especiais?", widget=forms.TextInput(attrs={'size': '70'}))
    manutencao  = forms.CharField(label = "6) Qual a manutenção (interna, externa e periodicidade)? Quem faz?  ", widget=forms.TextInput(attrs={'size': '70'}))
    padrao_quadro_luz  = forms.CharField(label = "7) O quadro de luz é no padrão ABNT (Fundo de Aço, limpo, organizado)?", widget=forms.TextInput(attrs={'size': '70'}))
    data_fund_emp  = forms.CharField(label = "1) Qual a data de fundação da empresa?", widget=forms.TextInput(attrs={'size': '70'}))
    atividade_princ_cliente  = forms.CharField(label = "2) Suas atividades e principais clientes?", widget=forms.TextInput(attrs={'size': '70'}))
    historico_acidente  = forms.CharField(label = "3) Qual a história de acidentes? Qual valor de prejuízo de cada um destes acidentes? O que foi feito para evitar novos acidentes?", widget=forms.TextInput(attrs={'size': '70'}))
    cob_ultimo_seguro  = forms.CharField(label = "4) Qual o valor e coberturas do último seguro (mandar cópia da apólice se for possível)?", widget=forms.TextInput(attrs={'size': '70'}))
    seguro_negado  = forms.CharField(label = "5) Já teve alguma proposta de seguro negada, ou participou de algum processo de cotação nos últimos 06 meses?", widget=forms.TextInput(attrs={'size': '70'}))


    class Meta:
        model = EmpresarialQuest
        fields = (
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
        )
