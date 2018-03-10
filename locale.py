>>> import locale
>>> import datetime
>>> l = {"en_US","ja_JP","de_DE","fr_FR","en_CA","fr_CA"}
>>> d = datetime.datetime.today()
>>> 
>>> for i in l :
...   print locale.setlocale(locale.LC_ALL, i + ".UTF-8")
...   print " ", locale.format("%d", 123456789, grouping=True)
...   print " ", locale.currency(123456789, grouping=True)
...   print " ", d.strftime("%Y %B %d %A")
... 
en_CA.UTF-8
  123,456,789
  $123,456,789.00
  2018 March 10 Saturday
fr_FR.UTF-8
  123456789
  123 456 789,00 Eu
  2018 mars 10 Samedi
ja_JP.UTF-8
  123,456,789
  ¥123,456,789
  2018 3月 10 土曜日
en_US.UTF-8
  123,456,789
  $123,456,789.00
  2018 March 10 Saturday
de_DE.UTF-8
  123456789
  Eu123.456.789,00
  2018 März 10 Samstag
fr_CA.UTF-8
  123456789
  123 456 789,00 $
  2018 mars 10 Samedi
>>> 
