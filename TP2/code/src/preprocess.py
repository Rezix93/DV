'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    #print(my_df)
    my_df_plus_plyerInformation = my_df.groupby('Act')['Player'].value_counts().reset_index(name='PlayerLine')
    my_df_plus_plyerInformation['sum'] = my_df_plus_plyerInformation.groupby('Act')['PlayerLine'].transform('sum')
    my_df_plus_plyerInformation['PlayerPercent'] = round(my_df_plus_plyerInformation['PlayerLine'] / my_df_plus_plyerInformation['sum'] *100,2)



    return my_df_plus_plyerInformation


def add_new_row(group):
    #new_row = pd.DataFrame({'Group': [group['Group'].iloc[0]], 'Value': [group['Value'].sum()]})
    OtherPlayerLine = group.head(1)["sum"] - group.head(1)["sum_first_fives"]
    print(OtherPlayerLine,group.head(1)["sum_first_fives"])
    OtherPlayerPercent = round(OtherPlayerLine / group.head(1)["sum"] *100,2)
    #new_row = {'Act': group.head(1)["Act"], 'Player': 'OTHER' ,'PlayerLine' :  OtherPlayerLine , 'PlayerPercent' : OtherPlayerPercent}
   
    new_row = pd.DataFrame({ 'Act': group.head(1)["Act"], 'Player': 'OTHER','PlayerLine' :  OtherPlayerLine , 'PlayerPercent' : OtherPlayerPercent})
    #print (new_row)
    #group = group.append(new_row, ignore_index=True)
    
    group = pd.concat([group, new_row])

    # Drop the 'sum' and 'sum_first five' columns
    columns_to_drop = ['sum', 'sum_first_fives']
    group = group.drop(columns=columns_to_drop)
    #print("add new row", group)
    
    df_sorted = group.groupby('Act').apply(lambda x: x.sort_values('PlayerLine'))

    return df_sorted

def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    #print('replace_others' , my_df)
    first_fives_player_each_Act = my_df.groupby('Act').head(5)
    first_fives_player_each_Act['sum_first_fives'] = first_fives_player_each_Act.groupby('Act')['PlayerLine'].transform('sum')

    first_fives_player_each_Act = first_fives_player_each_Act.groupby('Act').apply(add_new_row).reset_index(drop=True)
    #print(x)
    #first_fives_player_each_Act = pd.concat([first_fives_player_each_Act,x])

    return first_fives_player_each_Act


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    my_df['Player'].str.capitalize()
    #print (my_df)
    return my_df
