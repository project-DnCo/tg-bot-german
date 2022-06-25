import aiohttp

import typing

from .local_settings import WORDS_API_URL_NEXT, WORDS_API_URL_RANDOM


async def get_random_word() -> dict[str, typing.Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_RANDOM) as response:
            return await response.json()


async def get_next_word(pk: int) -> dict[str, typing.Any] | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{WORDS_API_URL_NEXT}{pk}/') as response:
            if response.status == 200:
                return await response.json()
            return None
