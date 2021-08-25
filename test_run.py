import os
import sqlite3

from budget.common import DateTime
from budget.endpoint import SqliteEndpoint
from budget.models import Operation, data_schema, Account
from budget.models.converter import ModelConverter, RequestType

storage_path = os.path.join(os.getcwd(), '.data/sqlite/budget.db')


def clear_db():
    conn = sqlite3.connect(storage_path)
    with conn:
        tables = conn.execute('SELECT name FROM sqlite_master WHERE type = "table";')
        tables = [name[0] for name in tables.fetchall()]
        print(f'tables to delete: {tables}')
        for table in tables:
            conn.execute(f'DROP TABLE {table};')


def main():
    # clear_db()
    endpoint = SqliteEndpoint(storage_path)
    converter = ModelConverter()
    operation = Operation(
        name='some transaction',
        from_id='',
        to_id='',
        value=0.0,
        pay_date=DateTime(2021, 8, 25),
        start_date=None,
        due_date=None,
        planned_value=None,
        planned=None,
        comment=None,
        tag=None,
    )
    data = converter.convert(operation, SqliteEndpoint, RequestType.INSERT)
    # endpoint.insert(data_schema.operation, data)
    d = endpoint.get(data_schema.operation)
    print(d)


if __name__ == '__main__':
    main()
