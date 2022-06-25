from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import random

from .serializers import WordSerializer
from .models import Word


class RandomWordAPIView(APIView):
    def get(self, *args, **kwargs):
        all_words = Word.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializer(random_word)
        return Response(serialized_random_word.data)


class NextWordAPIView(APIView):
    def get(self, request, pk):
        next_word = Word.objects.filter(pk__gt=pk).first()
        if next_word is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialized_next_word = WordSerializer(next_word)
        return Response(serialized_next_word.data)
