import os


class DatabaseConfig(object):
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:123456@localhost:3307/mi_dashboard?charset=utf8mb4&collation=utf8mb4_general_ci'
    # SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:123456@mysql:3307/mid_dashboard?charset=utf8mb4&collation=utf8mb4_general_ci'
    print(SQLALCHEMY_DATABASE_URI)
