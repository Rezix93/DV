'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'])
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    s = str(start) + '-01-01'
    e = str(end) + '-12-31'
    dataframe = dataframe.loc[(dataframe['Date_Plantation'] >= s) & (dataframe['Date_Plantation'] <= e)]
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    dataframe['Counts'] = 0
    yearly_df = dataframe.groupby(['Arrond_Nom', 'Date_Plantation'], as_index=False)['Counts'].count()
    
    neighbourhoods = yearly_df['Arrond_Nom'].unique()
    years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
    for n in neighbourhoods:
        for y in years:
            filtered = yearly_df.loc[(yearly_df['Arrond_Nom'] == n) & (yearly_df['Date_Plantation'].dt.strftime('%Y') == y)]
            sum = filtered['Counts'].sum()
            yearly_df.loc[(yearly_df['Arrond_Nom'] == n) & (yearly_df['Date_Plantation'].dt.strftime('%Y') == y), 'Counts'] = sum

    return yearly_df


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    data = pd.DataFrame(columns=['Arrond_Nom', 'Date_Plantation', 'Counts'])

    years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
    neighbourhoods = yearly_df['Arrond_Nom'].unique()
    for n in neighbourhoods:
        for y in years:
            filtered = yearly_df.loc[(yearly_df['Arrond_Nom'] == n) & (yearly_df['Date_Plantation'].dt.strftime('%Y') == y)]
            if len(filtered) != 0:
                new_row = [n, y, filtered['Counts'].iloc[0]] 
            else:
                new_row = [n, y, 0] 

            data.loc[len(data)] = new_row
    
    data = data.pivot(index='Arrond_Nom', columns='Date_Plantation')['Counts'].fillna(0)
    return data


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    dataframe['Counts'] = 0
    daily_df = dataframe.loc[(dataframe['Arrond_Nom'] == arrond) & (dataframe['Date_Plantation'].dt.strftime('%Y') == str(year))]
    daily_df = daily_df.groupby(pd.Grouper(key='Date_Plantation',freq='1D')).count().reset_index(drop=False, inplace=False)
    daily_df = daily_df.drop(['Arrond', 'Arrond_Nom', 'Longitude','Latitude'], axis=1)
    return daily_df
