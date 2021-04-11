from rest_framework import generics
from todo.models import (Intermediate, Goal)
from .serializers import (
                        IntermediateSerializer,
                        GoalSerializer
                        )


class IntermediateList(generics.ListCreateAPIView):
    queryset = Intermediate.objects.all()
    serializer_class = IntermediateSerializer

class IntermediateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intermediate.objects.all()
    serializer_class = IntermediateSerializer


class GoalList(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
