from app import main
from io import StringIO
from unittest.mock import patch
from datetime import datetime, timedelta
import random
import time
import os
from pathlib import Path

# Po przeniesieniu na maszynę - zmień ścieżki  w testach FALSE

# # POBIERANIE RAPORTU Z RYZYK - TRUE
# @patch('sys.stdout', new_callable=StringIO)
# def test_option_1_positive(mock_stdout):
#     # Ustawienie środowiska testowego
#     with patch('builtins.input', side_effect=['1', '3']):
#         # Uruchomienie funkcji main
#         main()
#         assert 'Log: > Wybrano opcję: Ryzyka - pobieranie raportu' in mock_stdout.getvalue()
#         assert 'Log: >>> Połączono z bazą danych' in mock_stdout.getvalue()
#         assert 'Log: >>>> Dane wyeksportowane do pliku Excel:' in mock_stdout.getvalue()
#         assert 'Log: >>> Nagłówki dodane do kolumn od 28. w pliku Excel' in mock_stdout.getvalue()

#         assert 'Log: > Wybrano opcję: Zakończ działanie' in mock_stdout.getvalue()


# # POBIERANIE RAPORTU Z RYZYK - FALSE
# @patch('sys.stdout', new_callable=StringIO)
# def test_option_1_negative(mock_stdout):
#     # Ustawienie środowiska testowego
#     with patch('builtins.input', side_effect=['1', '3']):
#         today = datetime.now().strftime("%Y%m%d")
#         # Uruchomienie funkcji main
#         main()
#         assert 'Log: > Wybrano opcję: Ryzyka - pobieranie raportu' in mock_stdout.getvalue()
#         assert f'Log: >>> Plik C://Users//izabe//OneDrive//Pulpit//AC_ryzyka//{today}//RaportAcRyzyka_{today}.xlsx już istnieje.' in mock_stdout.getvalue()
#         # assert f'Log: >>> Plik C://Users//robot//Desktop//AC_ryzyka//{today}//RaportAcRyzyka_{today}.xlsx już istnieje.' in mock_stdout.getvalue()

#         assert 'Log: > Wybrano opcję: Zakończ działanie' in mock_stdout.getvalue()


# # POBIERANIE RAPORTU Z HISTORII - TRUE
# @patch('sys.stdout', new_callable=StringIO)
# def test_option_2_1_positive(mock_stdout):
#     # Ustawienie środowiska testowego
#     with patch('builtins.input', side_effect=['2', '1', '3']):
#         # Uruchomienie funkcji main
#         main()
#         # Sprawdź, czy wybrano opcję 2
#         assert 'Log: > Wybrano opcję: Historia Pojazdu' in mock_stdout.getvalue()
#         # Sprawdź, czy połączono z bazą
#         assert 'Log: >>> Połączono z bazą danych' in mock_stdout.getvalue()
#         # Sprawdź, czy dane zapisano do pliku Excel
#         assert 'Log: >>>> Dane wyeksportowane do pliku Excel:' in mock_stdout.getvalue()
#         # Sprawdź, czy dodano nagłówki
#         assert 'Log: >>> Nagłówki dodane do kolumn od 15. w pliku Excel' in mock_stdout.getvalue()
#         # Sprawdź, czy program zakończył działanie
#         assert 'Log: > Wybrano opcję: Zakończ działanie' in mock_stdout.getvalue()

# # POBIERANIE RAPORTU Z HISTORII - FALSE
# @patch('sys.stdout', new_callable=StringIO)
# def test_option_2_1_negative(mock_stdout):
#     # Ustawienie środowiska testowego
#     with patch('builtins.input', side_effect=['2', '1', '3']):
#         today = datetime.now().strftime("%Y%m%d")
#         # Uruchomienie funkcji main
#         main()
#         # Sprawdź, czy wybrano opcję 2
#         assert 'Log: > Wybrano opcję: Historia Pojazdu' in mock_stdout.getvalue()
#         # Sprawdź, czy połączono z bazą
#         assert f'Log: >>> Plik C://Users//izabe//OneDrive//Pulpit//daneABP//{today}//RaportDaneABP_{today}.xlsx już istnieje.' in mock_stdout.getvalue()
#         # assert f'Log: >>> Plik C://Users//robot//Desktop//daneABP//{today}//RaportDaneABP_{today}.xlsx już istnieje.' in mock_stdout.getvalue()
#         # Sprawdź, czy program zakończył działanie
#         assert 'Log: > Wybrano opcję: Zakończ działanie' in mock_stdout.getvalue()


# GENERATOR DAT DO TESTÓW
def setup_function():
    global today, random_dates, two_days_ago, yesterday, weekend_dates
    today = datetime.today()
    random_dates = set()
    while len(random_dates) < 4:
        days_ago = random.randint(4, 60)
        random_dates.add((today - timedelta(days=days_ago)).strftime('%Y%m%d'))
    two_days_ago = (today - timedelta(days=2)).strftime('%Y%m%d')
    yesterday = (today - timedelta(days=1)).strftime('%Y%m%d')
    today = today.strftime('%Y%m%d')
    weekend_dates = [two_days_ago, yesterday, today]


# POBIERANIE 4 LOSOWYCH RAPORTÓW Z HISTORII + SCALANIE
@patch('sys.stdout', new_callable=StringIO)
def test_option_2_random_dates(mock_stdout):
    setup_function()
    # Ustawienie środowiska testowego dla pobierania raportów
    for date in random_dates:
        inputs = ['2', '2', date, '3']
        with patch('builtins.input', side_effect=inputs):
            # Uruchomienie funkcji main
            main()
            # Sprawdź, czy wybrano opcję 2
            assert 'Log: > Wybrano opcję: Historia Pojazdu' in mock_stdout.getvalue()
            # Sprawdź, czy wybrano opcję 2:2
            assert 'Log: >> Wybrano opcję: Pobieranie raportu ze wskazanej daty' in mock_stdout.getvalue()
            # Sprawdź, czy połączono z bazą
            assert 'Log: >>> Połączono z bazą danych' in mock_stdout.getvalue()
            # Sprawdź, czy dane zapisano do pliku Excel
            assert 'Log: >>>> Dane wyeksportowane do pliku Excel:' in mock_stdout.getvalue()
            # Sprawdź, czy dodano nagłówki
            assert 'Log: >>> Nagłówki dodane do kolumn od 15. w pliku Excel' in mock_stdout.getvalue()
            # Sprawdź, czy program zakończył działanie
            assert 'Log: > Wybrano opcję: Zakończ działanie' in mock_stdout.getvalue()
    # Opóźnienie scalania
    time.sleep(15)
    # Ustawianie ścieżek z losowymi datami
    random_paths = []
    for date in random_dates:
        random_paths.append(fr"C:\Users\izabe\OneDrive\Pulpit\daneABP\{date}\RaportDaneABP_{date}.xlsx")
        # random_paths.append(f'C:\Users\robot\Desktop\daneABP\{date}\RaportDaneABP_{date}.xlsx')

    # Ustawienie środowiska testowego dla scalania raportów
    inputs = ['2', '3', '2', '4'] + random_paths + ['3']
    with patch('builtins.input', side_effect=inputs):
        # Uruchomienie funkcji main
        main()
        # Sprawdź, czy wybrano opcję 2
        assert 'Log: > Wybrano opcję: Historia Pojazdu' in mock_stdout.getvalue()
        # Sprawdź, czy wybrano opcję 3
        assert 'Log: >> Wybrano opcję: Scalanie raportów' in mock_stdout.getvalue()
        # Sprawdź, czy wybrano opcję 2
        assert 'Log: >>> Wybrano opcję: Scalanie wskazanych raportów' in mock_stdout.getvalue()
        # Sprawdź, czy wybrano opcję 2
        assert f'Log: >>>> Scalone pliki zostały przeniesione do folderu C://Users//izabe//OneDrive//Pulpit//daneABP//{today},a scalony plik został nazwany RaportDaneABP_{today}.xlsx.' in mock_stdout.getvalue()
        # assert f'Log: >>>> Scalone pliki zostały przeniesione do folderu C://Users//robot//Desktop//daneABP//{today},a scalony plik został nazwany RaportDaneABP_{today}.xlsx.' in mock_stdout.getvalue()