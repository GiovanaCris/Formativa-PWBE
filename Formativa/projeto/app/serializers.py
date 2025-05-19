from rest_framework import serializers
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

        #Criptografar a senha no banco de dados
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

    #Tratação para não criar duas reservas ao mesmo tempo
    # def validate(self,data):
    #     data_inicio = data['data_inicio']
    #     data_termino = data['data_termino']
    #     sala =  data['sala_reservada']

    #     tratativa = ReservaAmbiente.objects.filter(
    #         sala_reservada=sala,
    #         data_inicio__lte=data_termino,
    #         data_termino__gte=data_inicio
    #     )
    #     if self.instance:
    #         tratativa = tratativa.exclude(pk=self.instance.pk)

    #     if tratativa.exists():
    #         raise serializers.ValidationError("Já existe uma reserva nessa sala neste dia e período.")
    #     return data

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