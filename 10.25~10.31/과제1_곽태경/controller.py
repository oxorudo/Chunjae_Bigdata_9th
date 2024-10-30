from db.connector import DBConnector
from settings import DB_SETTINGS, TEMP_PATH
from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.load import loader
from pipeline.remove import remover
from datetime import datetime
from db.pgsql_query import queries


def controller(batch_date):

    table_list = list(queries.keys())

    for table_name in table_list:
        db_obj = DBConnector(**DB_SETTINGS['MYSQL'])

        pandas_df = extractor(db_obj, table_name)


        if len(pandas_df) > 0:

            res = transformer(TEMP_PATH, batch_date, pandas_df, table_name)

            if res is not None and not res.empty:
                db_connector = DBConnector(**DB_SETTINGS['MYSQL'])
                loader(db_connector, pandas_df, table_name)

    remover(TEMP_PATH)


if __name__ == '__main__':
    _date = datetime.now()
    batch_date = _date.strftime('%Y%m%d')
    controller(batch_date)