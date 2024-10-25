import unittest
from add_test_logs import create_test_log_files
from app import main
from unittest.mock import patch
from io import StringIO
from datetime import datetime, timedelta
import random
import time

# Po przeniesieniu na maszynę - zmień ścieżki  w testach FALSE

class TestMain(unittest.TestCase):
    # # POBIERANIE RAPORTU Z RYZYK - TRUE
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_option_1_positive(self, mock_stdout):
    #     # Ustawienie środowiska testowego
    #     with patch('builtins.input', side_effect=['1', '3']):
    #         # Uruchomienie funkcji main
    #         main()

    #         # Sprawdź, czy wybrano opcję 1
    #         self.assertIn('Log: > Wybrano opcję: Ryzyka - pobieranie raportu', mock_stdout.getvalue())
    #         # Sprawdź, czy połączono z bazą
    #         self.assertIn('Log: >>> Połączono z bazą danych', mock_stdout.getvalue())
    #         # Sprawdź, czy dane zapisano do pliku Excel
    #         self.assertIn('Log: >>>> Dane wyeksportowane do pliku Excel:', mock_stdout.getvalue())
    #         # Sprawdź, czy dodano nagłówki
    #         self.assertIn('Log: >>> Nagłówki dodane do kolumn od 28. w pliku Excel', mock_stdout.getvalue())
            
    #         # Sprawdź, czy program zakończył działanie
    #         self.assertIn('Log: > Wybrano opcję: Zakończ działanie', mock_stdout.getvalue())


    # # POBIERANIE RAPORTU Z RYZYK - FALSE
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_option_1_negative(self, mock_stdout):
    #     # Ustawienie środowiska testowego
    #     with patch('builtins.input', side_effect=['1', '3']):
    #         today = datetime.now().strftime("%Y%m%d")
    #         # Uruchomienie funkcji main
    #         main()

    #         # Sprawdź, czy wybrano opcję 1
    #         self.assertIn('Log: > Wybrano opcję: Ryzyka - pobieranie raportu', mock_stdout.getvalue())
    #         # Sprawdź, czy połączono z bazą
    #         self.assertIn(f'Log: >>> Plik C://Users//izabe//OneDrive//Pulpit//AC_ryzyka//{today}//RaportAcRyzyka_{today}.xlsx już istnieje.', mock_stdout.getvalue())
    #         # self.assertIn(f'Log: >>> Plik C://Users//robot//Desktop//AC_ryzyka//{today}//RaportAcRyzyka_{today}.xlsx już istnieje.', mock_stdout.getvalue())
            
    #         # Sprawdź, czy program zakończył działanie
    #         self.assertIn('Log: > Wybrano opcję: Zakończ działanie', mock_stdout.getvalue())


    # # POBIERANIE RAPORTU Z HISTORII - TRUE
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_option_2_1_positive(self, mock_stdout):
    #     # Ustawienie środowiska testowego
    #     with patch('builtins.input', side_effect=['2', '1', '3']):
    #         # Uruchomienie funkcji main
    #         main()

    #         # Sprawdź, czy wybrano opcję 2
    #         self.assertIn('Log: > Wybrano opcję: Historia Pojazdu', mock_stdout.getvalue())
    #         # Sprawdź, czy połączono z bazą
    #         self.assertIn('Log: >>> Połączono z bazą danych', mock_stdout.getvalue())
    #         # Sprawdź, czy dane zapisano do pliku Excel
    #         self.assertIn('Log: >>>> Dane wyeksportowane do pliku Excel:', mock_stdout.getvalue())
    #         # Sprawdź, czy dodano nagłówki
    #         self.assertIn('Log: >>> Nagłówki dodane do kolumn od 15. w pliku Excel', mock_stdout.getvalue())
            
    #         # Sprawdź, czy program zakończył działanie
    #         self.assertIn('Log: > Wybrano opcję: Zakończ działanie', mock_stdout.getvalue())


    # # POBIERANIE RAPORTU Z HISTORII - FALSE
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_option_2_1_negative(self, mock_stdout):
    #     # Ustawienie środowiska testowego
    #     with patch('builtins.input', side_effect=['2', '1', '3']):
    #         today = datetime.now().strftime("%Y%m%d")
    #         # Uruchomienie funkcji main
    #         main()

    #         # Sprawdź, czy wybrano opcję 2
    #         self.assertIn('Log: > Wybrano opcję: Historia Pojazdu', mock_stdout.getvalue())
    #         # Sprawdź, czy połączono z bazą
    #         self.assertIn(f'Log: >>> Plik C://Users//izabe//OneDrive//Pulpit//daneABP//{today}//RaportDaneABP_{today}.xlsx już istnieje.', mock_stdout.getvalue())
    #         # self.assertIn(f'Log: >>> Plik C://Users//robot//Desktop//daneABP//{today}//RaportDaneABP_{today}.xlsx już istnieje.', mock_stdout.getvalue())
            
    #         # Sprawdź, czy program zakończył działanie
    #         self.assertIn('Log: > Wybrano opcję: Zakończ działanie', mock_stdout.getvalue())


    # GENERATOR DAT DO TESTÓW
    def setUp(self):
        self.today = datetime.today()
        self.random_dates = set()
        while len(self.random_dates) < 4:
            self.days_ago = random.randint(4, 60)
            self.random_dates.add((self.today - timedelta(days=self.days_ago)).strftime('%Y%m%d'))
        self.two_days_ago = (self.today - timedelta(days=2)).strftime('%Y%m%d')
        self.yesterday = (self.today - timedelta(days=1)).strftime('%Y%m%d')
        self.today = self.today.strftime('%Y%m%d')
        self.weekend_dates = [self.two_days_ago, self.yesterday, self.today]


    # POBIERANIE 4 LOSOWYCH RAPORTÓW Z HISTORII + SCALANIE
    @patch('sys.stdout', new_callable=StringIO)
    def test_option_2_random_dates(self, mock_stdout):
        today = datetime.now().strftime("%Y%m%d")
        # Ustawienie środowiska testowego dla pobierania raportów
        for date in self.random_dates:
            with self.subTest(date=date):
                inputs = ['2', '2', date, '3']
                with patch('builtins.input', side_effect=inputs):
                    # Uruchomienie funkcji main
                    main()

                    # Sprawdź, czy wybrano opcję 2
                    self.assertIn('Log: > Wybrano opcję: Historia Pojazdu', mock_stdout.getvalue())
                    # Sprawdź, czy wybrano opcję 2:2
                    self.assertIn('Log: >> Wybrano opcję: Pobieranie raportu ze wskazanej daty', mock_stdout.getvalue())

                    # Sprawdź, czy połączono z bazą
                    self.assertIn('Log: >>> Połączono z bazą danych', mock_stdout.getvalue())
                    # Sprawdź, czy dane zapisano do pliku Excel
                    self.assertIn('Log: >>>> Dane wyeksportowane do pliku Excel:', mock_stdout.getvalue())
                    # Sprawdź, czy dodano nagłówki
                    self.assertIn('Log: >>> Nagłówki dodane do kolumn od 15. w pliku Excel', mock_stdout.getvalue())
                
                # Sprawdź, czy program zakończył działanie
                self.assertIn('Log: > Wybrano opcję: Zakończ działanie', mock_stdout.getvalue())

        # Opóźnienie scalania
        time.sleep(30)

        # Ustawianie ścieżek z losowymi datami
        random_paths = []
        for date in self.random_dates:
            random_paths.append(f'C://Users//izabe//OneDrive//Pulpit//daneABP//{date}//RaportDaneABP_{date}.xlsx')
            # random_paths.append(f'C://Users//robot//Desktop//daneABP//{date}//RaportDaneABP_{date}.xlsx')

        # Ustawienie środowiska testowego dla scalania raportów
        inputs = ['2', '3', '2', '4'] + random_paths + ['3']
        with patch('builtins.input', side_effect=inputs):
            # Uruchomienie funkcji main
            main()

            # Sprawdź, czy wybrano opcję 2
            self.assertIn('Log: > Wybrano opcję: Historia Pojazdu', mock_stdout.getvalue())
            # Sprawdź, czy wybrano opcję 3
            self.assertIn('Log: >> Wybrano opcję: Scalanie raportów', mock_stdout.getvalue())
            # Sprawdź, czy wybrano opcję 2
            self.assertIn('Log: >>> Wybrano opcję: Scalanie wskazanych raportów', mock_stdout.getvalue())
            # Sprawdź, czy wybrano opcję 2
            self.assertIn(f'Log: >>>> Scalone pliki zostały przeniesione do folderu C://Users//izabe//OneDrive//Pulpit//daneABP//{today},a scalony plik został nazwany RaportDaneABP_{today}.xlsx.', mock_stdout.getvalue())
            # self.assertIn(f'Log: >>>> Scalone pliki zostały przeniesione do folderu C://Users//robot//Desktop//daneABP//{today},a scalony plik został nazwany RaportDaneABP_{today}.xlsx.', mock_stdout.getvalue())

            # Sprawdź, czy program zakończył działanie
            self.assertIn('Log: > Wybrano opcję: Zakończ działanie', mock_stdout.getvalue())


    # # ZAKONCZENIE PROGRAMU Z USUNIĘCIEM UTWOROZNYCH PLIKÓW LOG
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_exit_on_option_3(self, mock_stdout):
    #     # Utworzenie plików testowych
    #     create_test_log_files()

    #     # Ustawienie środowiska testowego
    #     with patch('builtins.input', return_value='3'):
    #         # Uruchomienie funkcji main
    #         main()

    #         # Sprawdź, czy program zakończył działanie
    #         self.assertIn('Log: > Wybrano opcję: Zakończ działanie', mock_stdout.getvalue())

    #         # Sprawdź, czy nie zostały wyświetlone żadne błędy
    #         self.assertEqual(mock_stdout.getvalue().count('Error'), 0)
    
if __name__ == '__main__':
    unittest.main()