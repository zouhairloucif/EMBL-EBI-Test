# serializers.py

from rest_framework import serializers

from .models import Molecule, Activity, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = '__all__'


class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    target = TargetSerializer(read_only=True, many=False, source='target_id')

    class Meta:
        model = Activity
        fields = ('type', 'units', 'value', 'relation', 'target_id', 'target', 'molecule_id')
