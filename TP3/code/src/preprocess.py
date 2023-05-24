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
    # using function "to_datetime" to convert dataframe to datetime
    dataframe = pd.read_csv(('./assets/data/arbres.csv'))
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
#   df = dataframe.groupby('Date_Plantation')
#   print(df)
#  return dataframe
# using .loc accessor and a boolean proposition to filter all values between 01/01 untill 12/31 per each year
    dataframe = dataframe.loc[(dataframe['Date_Plantation'] >= ('%d-01-01' % start))
                              & (dataframe['Date_Plantation'] <= ('%d-12-31' % end))]
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
    # firstly,  we group the dataframe by the values in the columns 'Arrond_Nom' and dataframe['Date_Plantation'].dt.year. 
    # so we will have data grouped by the unique combinations of the neighborhood.
    # then with the function '.size()', we calculate the count of each group,
    # representing the number of data within each grouped combination of neighborhood and year
    # finally, ".reset_index(name='Counts')" converts the result grouped into a dataframe and resets the index. 
    # The column containing the counts is named 'Counts'.
    #So we have a data frame that includes the counts of observations for 
    # each combination of neighborhood and year in the original dataframe, providing statistics 
    # of the frequency of tree plantations in different neighborhoods and years.
    
    yearly_df = (dataframe.groupby(['Arrond_Nom',dataframe['Date_Plantation'].dt.year]).size().reset_index(name='Counts'))

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
    
    #creating pivot table from our dataframe: [neighborhoods as rows, years as columns, and the counts of tree plantations as the cell values.]
    
    data = yearly_df.pivot(index='Arrond_Nom', columns='Date_Plantation', values='Counts')
    
    
    #fill the empty cells with zero
    
    data = data.fillna(0)
    
    # rename years columns to be more easily to show
    
    data = data.rename({2010: '2010-12-31', 2011: '2011-12-31', 2012: '2012-12-31', 
                        2013: '2013-12-31', 2014: '2014-12-31', 2015: '2015-12-31', 
                        2016: '2016-12-31', 2017: '2017-12-31', 2018: '2018-12-31', 
                        2019: '2019-12-31', 2020: '2020-12-31'}, axis=1)
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
    return None
