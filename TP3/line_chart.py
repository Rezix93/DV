'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.

    fig = px.line(x=[0,0], y=[0,0])
    fig.add_annotation(text='No data to display.<br> Select a cell in the heatmap for more information.', xref='paper', yref='paper', showarrow=False) # src to center the text: https://codepen.io/etpinard/pen/WpmNEo
    fig.update_layout(dragmode = False, xaxis = {'visible': False, 'showticklabels': False}, yaxis = {'visible': False, 'showticklabels': False})
                      
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    #src: https://plotly.com/python/shapes/#:~:text=Drawing%20shapes%20with%20a%20Mouse%20on%20Cartesian%20plots,-introduced%20in%20plotly&text=You%20can%20create%20layout%20shapes,'%20%2C%20or%20'drawrect'%20.
    # https://plotly.com/python/reference/layout/annotations/?_gl=1*izjhis*_ga*MTYwNTY0NjA2My4xNjg1MjgwOTUz*_ga_6G7EE0JNSC*MTY4NTI5NjE1My42LjEuMTY4NTMwMDcwMS4wLjAuMA..#layout-annotations-items-annotation-xref
    fig.add_shape(type='rect', x0=0, y0=0.875, x1=1, y1=0.125, xref='x domain', yref='y domain', fillcolor=THEME['pale_color'], line_color = THEME['pale_color'])
    return fig



def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    if len(line_data) == 1:
        fig = px.scatter(line_data, x = "Date_Plantation", y = "Counts")
    else:
        fig = px.line(line_data, x = "Date_Plantation", y = "Counts")
    
    fig.update_layout(title = f"Trees planted in {arrond} in {year}", xaxis_title = "Date", yaxis_title = "Trees", xaxis={'tickformat': '%d %b'})

    fig.update_traces(
    hovertemplate=hover_template.get_linechart_hover_template()
                      )
        

    return fig
