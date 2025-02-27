# libraries to use
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Return a DataFrame stylized by colormap
def Colormap_player(player_df):
    return player_df.style.format({'GPGR': '{:.2f}', 'APM': '{:.2f}',
                                   'GAR': '{:.2f}',
                                   'TC': '{:.0f}',
                                   'CPM': '{:.2f}'}).background_gradient(
                                    subset=['GPGR', 'APM', 'GAR', 'TC', 'CPM'],
                                    cmap='Pastel2_r')


# Getting Player Stats
def Player_stats(df):
    # GPGR: Goals Per Game Ratio
    df['GPGR'] = df.loc[:, "Goals"] / df.loc[:, "Matches"]
    # Assists Per Match
    df['APM'] = df.loc[:, "Assists"] / df.loc[:, "Matches"]
    # Goals - Assists Ratio
    df['GAR'] = df.loc[:, "Goals"] / df.loc[:, "Assists"]
    # Total contributions (Assists and Goals)
    df['TC'] = df.loc[:, "Assists"] + df.loc[:, "Goals"]
    # Contribution Per Match
    df['CPM'] = df.loc[:, "TC"] / df.loc[:, "Matches"]
    # Replacing "inf", "-inf" and "nan" values with zero
    df.replace([np.inf, -np.inf, np.nan, -np.nan], 0, inplace=True)
    return df


# Bar chart graph
def Player_graph_bar(player1_df, player2_df, seasons):
    plt.subplots(figsize=(15, 5))
    '''Custom column DF(Matches,Goals,Assists,GPGR,APM,GAR,TC,CPM)'''
    column = 'Matches'
    # Stats that don't need to display numbers after the numerical point
    natural_stats = ["Matches", "Goals", "Assists"]
    # Getting the stats by player into an array
    player1 = np.array(player1_df[column])
    player2 = np.array(player2_df[column])
    bar_width = 0.35
    # Number of total seasons
    x = np.arange(len(seasons))

    # Bar for each player
    player1_stats = plt.bar(x - bar_width/2, player1, bar_width,
                            label=player_1, color='skyblue')
    player2_stats = plt.bar(x + bar_width/2, player2, bar_width,
                            label=player_2, color='lightgreen')

    # Displaying numbers above each player bar

    if column in natural_stats:
        for bar in player1_stats:

            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                     f'{bar.get_height():.0f}', ha='center', va='bottom',
                     fontsize=8, rotation=45)

        for bar in player2_stats:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                     f'{bar.get_height():.0f}', ha='center', va='bottom',
                     fontsize=8, rotation=45)

    else:
        for bar in player1_stats:

            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                     f'{bar.get_height():.1f}', ha='center', va='bottom',
                     fontsize=8, rotation=45)

        for bar in player2_stats:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                     f'{bar.get_height():.1f}', ha='center', va='bottom',
                     fontsize=8, rotation=45)

    # Custom labels for chart
    plt.xlabel('Seasons')
    plt.ylabel('Count')
    plt.title(column + ' ' + str('Per Player'))
    plt.xticks(x, seasons)
    plt.legend(title='Players')
    # Rotating the numbers above each chart to visualize better
    plt.xticks(rotation=90)
    return plt.show()


# Pie chart graph
def Player_pie(player1_df, player2_df, seasons):
    # Getting the stats of each player
    '''Custom column DF(Matches,Goals,Assists)'''
    column = "Matches"
    player1 = np.array(player1_df[column])
    player2 = np.array(player2_df[column])
    # List of All Seasons
    seasons = player1_df.loc[:, "Seasons"].unique()
    # Create a figure and a set of subplots
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))  # 1 row, 2 columns

    # Plot the first pie chart
    ax[0].pie(player1, labels=seasons, autopct='%1.1f%%',
              textprops={'size': 'smaller'}, startangle=90,
              colors=sns.color_palette('pastel'), pctdistance=0.6,
              labeldistance=1.15)

    ax[0].set_title(player_1 + " " + column)

    # Plot the second pie chart
    ax[1].pie(player2, labels=seasons, autopct='%1.1f%%',
              textprops={'size': 'smaller'}, startangle=90,
              colors=sns.color_palette('pastel'), pctdistance=0.6,
              labeldistance=1.15)
    ax[1].set_title(player_2 + " " + column)

    # Adjust the padding between and around subplots
    plt.tight_layout()
    return plt.show()


# Plot chart graph
def player_plot(player1_df, player2_df, seasons):
    plt.subplots(figsize=(15, 5))
    '''Custom column DF(Matches,Goals,Assists,GPGR,APM,GAR,TC,CPM)'''
    column = 'CPM'
    # Getting the stats of each player
    player1 = np.array(player1_df[column])
    player2 = np.array(player2_df[column])
    # Plot the two players with a different marker
    plt.plot(player1, marker='o', label=player_1)
    plt.plot(player2, marker='x', label=player_2)
    # Getting seasons fox x ticks
    seasons = player1_df.loc[:, "Seasons"].unique()
    plt.xticks(ticks=range(len(seasons)), labels=seasons)
    plt.title(column + " " + "by player")
    plt.legend(title='Players')

    return plt.show()


# Comparing stats by players
def Player_Comparison(player_1, player_2):
    # Getting the stats of all players icluding GPGR,APM,GAR,TC,CPM
    players = Player_stats(grouped_df)
    # Find 1st player
    player1_df = players[players.loc[:, 'Players'] == player_1]
    # Find 2nd player
    player2_df = players[players.loc[:, 'Players'] == player_2]
    # List of All Seasons
    seasons = player1_df.loc[:, "Seasons"].unique()
    # Merging Player1 and Player2 dataframes
    df_merged = pd.concat([player1_df,
                           player2_df]).sort_values(by='CPM',
                                                    ascending=False)
    # Returning all charts and colormap charts
    Player_graph_bar(player1_df, player2_df, seasons)
    Player_pie(player1_df, player2_df, seasons)
    player_plot(player1_df, player2_df, seasons)

    return Colormap_player(df_merged)


# Reading the csv tha conyains all the data needed
# and Grouping by including Players, teams and seasons
grouped_df = pd.read_csv('Players.csv').groupby(['Players', 'Teams', 'Seasons', 'Position'])[['Matches', 'Goals', 'Assists']].sum().reset_index().sort_values(by='Seasons', ascending=True)

# Global variables to use in the chart functions
global player_1
player_1 = "Sergio Ramos"
global player_2
player_2 = "Virgil van Dijk"

# Showing all charts
Player_Comparison(player_1, player_2)
