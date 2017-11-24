from django.db import models
from django.utils import timezone
# Create your models here.

class EmpresarialQuest(models.Model):
    #client = models.ForeignKey('cliente.sss')
    cliente = models.CharField(max_length=200, null=False)
    risco_cep = models.CharField(max_length=8, null=False)
    area_predios = models.CharField(max_length=200, null=False)
    valor_estoque = models.CharField(max_length=200, null=False)
    valor_maquinas = models.CharField(max_length=200, null=False)
    desc_vizinhanca = models.CharField(max_length=300, null=False)


    quant_extintores = models.CharField(max_length=100, null=False)
    desc_distrib_ext = models.CharField(max_length=200, null=False)
    desc_hidrant = models.CharField(max_length=200, null=False)
    cor_dutos = models.CharField(max_length=200, null=False)
    duto_ferro_aco = models.CharField(max_length=200, null=False)
    quant_lt_reserv_incend = models.CharField(max_length=100, null=False)
    quant_agua_consum_local = models.CharField(max_length=100, null=False)
    para_raio_mod = models.CharField(max_length=100, null=False)
    brigada_incendio = models.CharField(max_length=100, null=False)
    desc_material_protecao = models.CharField(max_length=100, null=False)
    dist_bombeiros = models.CharField(max_length=100, null=False)


    cameras_cftv = models.CharField(max_length=100, null=False)
    onde_grava_img = models.CharField(max_length=200, null=False)
    vigilancia = models.CharField(max_length=200, null=False)
    empr_ext_monit = models.CharField(max_length=200, null=False)


    aluguel_predio = models.CharField(max_length=100, null=False)
    valor_aluguel = models.CharField(max_length=200, null=False)
    somatorio_desp_fixa = models.CharField(max_length=200, null=False)
    faturamento_mensal = models.CharField(max_length=200, null=False)


    carga_luz_rua_emp = models.CharField(max_length=100, null=False)
    quant_transformadores = models.CharField(max_length=200, null=False)
    transf_carga_dist = models.CharField(max_length=200, null=False)
    desc_geradores = models.CharField(max_length=200, null=False)
    desc_inst_eletrica = models.CharField(max_length=200, null=False)
    manutencao = models.CharField(max_length=100, null=False)
    padrao_quadro_luz = models.CharField(max_length=100, null=False)


    data_fund_emp = models.CharField(max_length=15, null=False)
    atividade_princ_cliente = models.CharField(max_length=500, null=False)
    historico_acidente = models.CharField(max_length=500, null=False)
    cob_ultimo_seguro = models.CharField(max_length=200, null=False)
    seguro_negado = models.CharField(max_length=200, null=False)
    insert_date = models.DateTimeField(
            blank=True, null=True)
    self.published_date = timezone.now()
    def __str__(self):
        return self.cliente
