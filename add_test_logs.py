import os
import datetime
import filedate

def create_test_log_files():
    today = datetime.date.today()

    # Tworzenie testowych plików z logami
    for i in range(31, 35):
        log_date = today - datetime.timedelta(days=i)
        log_filename = log_date.strftime('%Y%m%d.log')
        log_filepath = os.path.join('./logs', log_filename)

        with open(log_filepath, 'w') as log_file:
            log_file.write('')

        log_datetime = datetime.datetime.combine(log_date, datetime.time())
        filedate.File(log_filepath).set(created=log_datetime)

create_test_log_files()