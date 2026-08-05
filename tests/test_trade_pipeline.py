from engine.trade_pipeline import TradePipeline
from memory.memory_engine import MemoryEngine


def test_trade_pipeline_memory():

    trade = {

        "id": 999,

        "asset": "BTC",

        "market": "CRYPTO",

        "signal": "BUY",

        "entry_price": 64000,

        "exit_price": 65000,

        "quantity": 1,

        "gross_pnl": 1.56,

        "pnl": 1.56,

        "result": "WIN",

        "confidence": 80,

        "status": "CLOSED",

        "exit_reason": "TEST"

    }


    pipeline = TradePipeline()

    pipeline.process(trade)


    memory = MemoryEngine()

    stats = memory.statistics()


    print(stats)


    assert stats["total"] >= 1