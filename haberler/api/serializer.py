from rest_framework import serializers
from haberler.models import Haber

class HaberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    icerik = serializers.CharField()
    sehir = serializers.CharField()
    aktif = serializers.BooleanField()
    yayin_tarihi = serializers.DateTimeField(read_only=True)
    guncelleme_tarihi = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        return Haber.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

