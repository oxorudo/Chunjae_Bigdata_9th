import os

def transformer(temp_path, batch_date, df, table_name):
    path = create_path(temp_path, batch_date, table_name)
    res = save_to_file(df, path, table_name)

    return res



def create_path(temp_path, batch_date, table_name):

    _y = batch_date[:4]
    _m = batch_date[4:6]
    _d = batch_date[6:]

    _path = os.path.join(temp_path, table_name, f'yyyy={_y}', f'mm = {_m}', f'dd={_d}')

    return _path


def save_to_file(df, path, table_name):
    if len(df) > 0:
        os.makedirs(path, mode=777)
        save_path = os.path.join(path, f'{table_name}.csv')

        df.to_csv(save_path, index=False)
        return True
    
    else:
        print('empty file')
        return False
    

