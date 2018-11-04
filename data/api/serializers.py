from rest_framework import serializers

from .models import Areas, Base, Curso, Docentes, Infra

class AreasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Areas
        fields = (
            'id_area','sigla_area', 'area_atua',
            'equi_area','obs_area'
        )
            
class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Base
        fields = (
            'id_base', 'campus_base', 'eixo',
            'tipo_curso', 'curso_base', 'tipo_oferta',
            'dis_oferta', 'modalidade', 'turno',
            'semestre_inicio', 'periocidade_curricular',
            'periocidade_ingresso', 'situacao_oferta',
            'situacao_ppc', 'fomento', 'local_curso',
            'cargahora_base', 'fase_semestre', 'qtd_vagas',
            'duracao_semestre', 'semana_semestre', 'observacao',
            'qtd_turmas', 'cargahora_fase', 'cargahora_minima',
            'fech', 'fec'
        )

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id_curso', 'nome_curso', 'fec_curso',
            'cargahora_curso', 'cargahora_cursointegrado',
            'eixo_tecnologico', 'tipo_curso', 'obs_curso'
        )

class DocentesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Docentes
        fields = (
            'id_docente', 'campus_docente', 'nome_docente',
            'area_docente', 'desc_area', 'regime_trabalho',
            'fg_fcc', 'cont_docente', 'docente_integral',
            'docente_equi', 'obs_docente'
        )

class InfraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Infra
        fields = (
            'id_infra', 'campus_infra', 'situacao_infra',
            'tipo_espaco', 'nome_espaco', 'capacidade_esp'
        )


