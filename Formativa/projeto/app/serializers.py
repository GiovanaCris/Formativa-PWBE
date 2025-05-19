from rest_framework import serializers
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

    def validate(self,data):
        data_inicio = data['data_inicio']
        data_termino = data['data_termino']
        periodo = data['periodo']
        sala =  data['sala_reservada']

        tratativa = ReservaAmbiente.objects.filter(
            sala_reservada=sala,
            periodo=periodo,
            data_inicio__lte=data_termino,
            data_termino__gte=data_inicio
        )
        if self.instance:
            tratativa = tratativa.exclude(pk=self.instance.pk)

        if tratativa.exists():
            raise serializers.ValidationError("Já existe uma reserva nessa sala neste dia e período.")
        return data

class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'tipo': self.user.tipo
        }
        return data
    
class ReservaSalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

    def validate_nome(self, value):
        if Sala.objects.filter(nome__iexact=value).exists():
            raise serializers.ValidationError("Já existe uma sala com esse nome!") #Tratação para não criar duas salas com o mesmo nome
        return value