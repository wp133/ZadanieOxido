!!!!!!!!!WAŻNE!!!!!!!!!
W pliku formatting.py jest miejsce na klucz dla API, który usunąłem ze względów bezpieczeństwa. Nie byłem pewien czy to dla Państwa problem, więc wolałem dmuchać na zimne. Oczywiśce z kluczem powinno działać.
!!!!!!!!!!!!!!!!!!!!!!!

Asystent HTML - aplikacja strukturyzująca tekst zadany w pliku txt i tworząca na jego podstawie pliki: artykul.html (bez sekcji <body>) oraz showcase.html (z sekcją <body>).
Zasadnicza część aplikacji tj. kod składa się z dwóch plików .py - gui (interfejs) oraz formatting (wysyłanie promptu).

Asystenta można otworzyć poprzez dwukrotne kliknięcie załączonego pliku wykonywalnego "gui.exe". Deweloper uprzedza, że istnieje niezerowa szansa, że plik ów nie zadziała.
Wówczas zaleca się skompilowanie pliku "gui.py".

Aplikacja posiada własny interefjs graficzny. Przyciskiem "Open text file" można wybrać dowolny plik tekstowy na podstawie którego chcemy stworzyć artykuł. 
Domyślnie wybór proponowanych plików jest zawężony do pliku "Zadanie dla JJunior AI Developera - tresc artykulu" ale można łatwo zamiast tego otworzyć dowolny plik txt zaminiając nazwę pliku na "*".

Przycisk Reset służy do czyszczenia pliku showcase.html. Aplikacja domyślnie pokazuje ostatni otwarty artykuł. Tak, to feature.

#####################
Załączone są tez pliki "requirements.txt" zawierający listę używanych bibliotek (jedna z nich tj. tkinter jest częścią standardowej instalacji Pythona), oraz "image_placeholder.jpg" będący imponującym fajerwerkiem graficznym.
