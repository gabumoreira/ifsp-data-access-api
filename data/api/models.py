# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Areas(models.Model):
    id_area = models.AutoField(primary_key=True)
    sigla_area = models.CharField(max_length=15)
    area_atua = models.CharField(max_length=255)
    equi_area = models.CharField(max_length=45)
    obs_area = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'areas'


class Base(models.Model):
    id_base = models.AutoField(primary_key=True)
    campus_base = models.CharField(max_length=45)
    eixo = models.CharField(max_length=45)
    tipo_curso = models.CharField(max_length=45)
    curso_base = models.CharField(max_length=255)
    tipo_oferta = models.CharField(max_length=45)
    dis_oferta = models.CharField(max_length=45)
    modalidade = models.CharField(max_length=45)
    turno = models.CharField(max_length=45)
    semestre_inicio = models.CharField(max_length=45)
    periocidade_curricular = models.CharField(max_length=45)
    periocidade_ingresso = models.CharField(max_length=45)
    situacao_oferta = models.CharField(max_length=45)
    situacao_ppc = models.CharField(max_length=45)
    fomento = models.CharField(max_length=45)
    local_curso = models.CharField(max_length=45)
    cargahora_base = models.CharField(max_length=45)
    fase_semestre = models.CharField(max_length=45)
    qtd_vagas = models.CharField(max_length=45)
    duracao_semestre = models.CharField(max_length=45)
    semana_semestre = models.CharField(max_length=45)
    observacao = models.CharField(max_length=255, blank=True, null=True)
    qtd_turmas = models.CharField(max_length=45)
    cargahora_fase = models.CharField(max_length=45)
    cargahora_minima = models.CharField(max_length=45)
    fech = models.CharField(max_length=45, blank=True, null=True)
    fec = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nome_curso = models.CharField(max_length=255)
    fec_curso = models.CharField(max_length=45, blank=True, null=True)
    cargahora_curso = models.CharField(max_length=45, blank=True, null=True)
    cargahora_cursointegrado = models.CharField(max_length=45, blank=True, null=True)
    eixo_tecnologico = models.CharField(max_length=45, blank=True, null=True)
    tipo_curso = models.CharField(max_length=45, blank=True, null=True)
    obs_curso = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class Docentes(models.Model):
    id_docente = models.AutoField(primary_key=True)
    campus_docente = models.CharField(max_length=45)
    nome_docente = models.CharField(max_length=255)
    area_docente = models.CharField(max_length=45)
    desc_area = models.CharField(max_length=255)
    regime_trabalho = models.CharField(max_length=30)
    fg_fcc = models.CharField(max_length=30)
    cont_docente = models.CharField(max_length=45)
    docente_integral = models.CharField(max_length=15)
    docente_equi = models.CharField(max_length=15)
    obs_docente = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'docentes'


class Infra(models.Model):
    id_infra = models.AutoField(primary_key=True)
    campus_infra = models.CharField(max_length=45)
    situacao_infra = models.CharField(max_length=45)
    tipo_espaco = models.CharField(max_length=45)
    nome_espaco = models.CharField(max_length=255)
    capacidade_esp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'infra'
