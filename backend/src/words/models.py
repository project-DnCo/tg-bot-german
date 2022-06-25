from django.db import models


class Word(models.Model):
    """Model for storing German words"""

    GENDERS = (
        ('der', 'Der'),
        ('die', 'Die'),
        ('das', 'Das'),
    )

    word = models.CharField(max_length=100)
    gender = models.CharField(max_length=3, choices=GENDERS)

    def __str__(self) -> str:
        return f'{self.gender} {self.word}'
