from memory.memory_engine import MemoryEngine


def test_memory_statistics():

    memory = MemoryEngine()

    result = memory.statistics()

    print(result)

    assert "total" in result
    assert "win_rate" in result