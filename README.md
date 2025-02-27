# Soccer-Player-Analysis

Analyzing soccer stats comparing two soccer players. The data includes stats from season 2025 to 2024.

## Libraries to use


```bash
pip install pandas
python -m pip install -U matplotlib
pip install numpy
pip install seaborn
```


## Players data
The list of the players into the data CSV; these names are allowed to be used in the global variables.
```bash
Sergio Ramos
Nacho Fernandez
Virgil van Dijk
Jose Gimenez
Joseph Gomez
Harry Maguire
Jules Kounde
John Stones
Josko Gvardiol
Nathan Ake
Manuel Akanji
Eric Dier
Dayot Upamecano
Matthijs de Ligt
Eric Garcia
Inigo Martinez
Clement Lenglet
Ronald Araujo
Andreas Christensen
Pau Cubarsi
Lisandro Martinez
Leny Yoro
Jonny Evans
Gabriel
Ben White
Chris Smalling
Nicolas Otamendi
Lewis Dunk
Ezri Konsa
Marc Guehi
Robin Le Normand
Sergi Roberto
Joao Cancelo
Andrew Robertson
Trent Alexander-Arnold
Kyle Walker
Hector Bellerin
David Alaba
Lucas Vazquez
Luke Shaw
Alex Sandro
Danilo
Nahuel Molina
Daley Blind
Miguel Gutierrez
Raphael Guerreiro
Alex Balde
Ferland Mendy
Diogo Dalot
Oleksandr Zinchenko
Theo Hernandez
Jesus Navas
Juan Miranda
Lionel Messi
Cristiano Ronaldo
Neymar
Kylian Mbappe
Mohamed Salah
Antoine Griezmann
Thomas Muller
Roberto Firmino
Kai Havertz
Christopher Nkunku
Iago Aspas
Gerard Moreno
Joao Felix
Paulo Dybala
Karim Benzema
Harry Kane
Robert Lewandowski
Alvaro Morata
Erling Haaland
Romelu Lukaku
Jamie Vardy
Julian Alvarez
Timo Werner
Lautaro Martinez
Divock Origi
Vitor Roque
Gabriel Jesus
Victor Osimhen
Olivier Giroud
Ivan Toney
Joselu
Vinicius Junior
Angel Di Maria
Heung Min Son
Raheem Sterling
Riyad Mahrez
Sadio Mane
Bernardo Silva
Leroy Sane
Inaki Williams
Ferran Torres
Marcus Rashford
Bukayo Saka
Alejandro Garnacho
Jadon Sancho
Cody Gakpo
Diogo Jota
Antony
Jack Grealish
Phil Foden
Jeremy Doku
Richarlison
Federico Chiesa
Alexis Sanchez
Juan Cuadrado
Joaquin Correa
Dejan Kulusevski
Thomas Lemar
Angel Correa
Christian Pulisic
Kingsley Coman
Lamine Yamal
Raphinha
Ansu Fati
Samuel Chukwueze
Rafael Leao
Noah Okafor
Leandro Trossard
Reiss Nelson
Matteo Politano
Khvicha Kvaratskhelia
Pedro Rodriguez
Marcus Thuram
Eberechi Eze
Alex Baena
Nico Williams
Mikel Oyarzabal
Paul Pogba
Ilkay Gundogan
Luka Modric
Koke
koke
Jude Bellingham
Frenkie de Jong
Alexis Mac Allister
Pedri
Mateo Kovacic
Bruno Fernandes
Mason Mount
Arthur
Axel Witsel
Rodrigo De Paul
Leon Goretzka
Konrad Laimer
Jamal Musiala
Gavi
Fermin Lopez
Pablo Torre
Eduardo Camavinga
Yacine Adli
Scott McTominay
Jorginho
Leandro Paredes
Adrien Rabiot
Kobbie Mainoo
Dani Olmo
Fabian Ruiz
Joshua Kimmich
Casemiro
Kalvin Phillips
Rodri
Oriol Romeu
Thomas Partey
Declan Rice
```
## Usage

```python
# returns the stats by each player from the dataframe
Player_stats(df)

# returns a dataframe with a colormap
Colormap_player(player_df)

# plots two bar charts 
Player_graph_bar(player1_df, player2_df, seasons)
'''To obtain a chart with different stats, change the vale of column
   (Matches,Goals,Assists)'''
column = "Matches"

# Plot chart graph  
player_plot(player1_df, player2_df,seasons):
    '''Allowed column values (Matches,Goals,Assists,GPGR,APM,GAR,TC,CPM)'''
    column = 'CPM'

# Global variables to use in the chart functions
'''You can change the name of the players here, review the "Players data" section'''
global player_1
player_1 = "Sergio Ramos"
global player_2
player_2 = "Virgil van Dijk"

# Grouping players stats

''' Reading the csv tha conyains all the data needed
and Grouping by including Players, teams and seasons (You could only include Players to get the total stats by player)'''

grouped_df = pd.read_csv('Players.csv').groupby(['Players','Position'])[['Matches', 'Goals', 'Assists']].sum().reset_index().sort_values(by='Seasons', ascending=True)
```


## Files

To see all the columns in the csv, go to the Players.csv file.

## More information
This project idea, was taken from here
[Original idea](https://www.kaggle.com/code/desalegngeb/english-premier-league-players-statistics)
