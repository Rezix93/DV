'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include our new theme and set the title

    fig.update_layout(
        template=pio.templates['simple_white'],
        dragmode=False,
        barmode='relative'
    )
    
    #setting the tempalte and title
    fig = go.Figure(layout = go.Layout(title="Lines (Count)"))
    #fig.update_layout(template = pio.templates.default, title = "Lines")
    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    

    fig = go.Figure(fig)  # conversion back to Graph Object
    print(data)
    # TODO : Update the figure's data according to the selected mode
    if mode == 'Count':
        ymode = 'PlayerLine'
    else:
        ymode = 'PlayerPercent'

    data_temp = [go.Bar(name = Player, x =  'Act ' + (gp['Act']).apply(str), y=gp[ymode], hovertemplate= get_hover_template(Player,mode)) for Player, gp in data.groupby(by='Player')]
    print("data_temp: " , data_temp)
    fig = go.Figure(data_temp)
    fig.update_layout(barmode='stack', title='Lines of Players in each Act',xaxis={'categoryorder':'category ascending'})
    #barmode group = create them side to side
    #barmode Stack : create them together
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
            
    '''
    print(mode)
    if mode == 'Count':        
        fig.update_yaxes(title_text='Lines (Count)')
    else:
        fig.update_yaxes(title_text='Lines (Percent)')
    # TODO : Update the y axis title according to the current mode