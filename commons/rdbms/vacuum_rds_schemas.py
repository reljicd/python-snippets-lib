from typing import List

import fire

from commons.logger.logger import get_logger
from commons.rdbms.set_sequences import SCHEMAS
from commons.rdbms.utils import execute_statement, schema_tables

LOGGER = get_logger(__name__)


def vacuum_schemas(schemas: List = SCHEMAS) -> None:
    for schema in schemas:
        for table in schema_tables(schema):
            vacuum_schema_table(schema, table)


def vacuum_schema_table(schema: str, table: str) -> None:
    LOGGER.info(f'VACUUM {schema}.{table} ...')
    execute_statement(f'VACUUM ANALYSE {schema}.{table}')
    LOGGER.info(f'VACUUM {schema}.{table} done')


if __name__ == '__main__':
    fire.Fire(vacuum_schemas)
