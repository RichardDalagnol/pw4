from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = [
			'nome',
			'email',
			'data_nascimento',
			'endereco',
			'numero',
			'complemento',
			'bairro',
			'cidade',
			'uf',
			'telefone',
			'celular',
			'rg',
			'cpf',
		]