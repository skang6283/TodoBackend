from rest_framework import serializers
from todo.models import ( Intermediate, Goal)



class IntermediateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intermediate
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
