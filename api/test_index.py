import pytest

from index import say_hello, root


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {'message': 'Hello World'}


@pytest.mark.asyncio
async def test_say_hello():
    result = await say_hello("John")
    assert result == {'message': 'Hello John'}
