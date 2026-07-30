"""
Database Manager
Single Entry Point
"""

from database.database import initialize_database

from memory.memory_database import initialize_memory

from memory.market_memory import initialize_market_memory

from analytics.journal_database import create_journal_table


class DatabaseManager:

    @staticmethod
    def initialize():

        initialize_database()

        initialize_memory()

        initialize_market_memory()

        create_journal_table()

        print("DATABASE INITIALIZED")