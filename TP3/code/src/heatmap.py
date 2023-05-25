'''
    Contains some functions related to the creation of the heatmap.
    check 3
'''
import plotly.express as px
import hover_template


def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.

    heatmap_fig = px.imshow(data,
                            x=data.columns.year.tolist(), 
                            y=data.index.tolist(),
                            labels=dict(color="Trees",x="Year", y="Neighborhood"))
    heatmap_fig.update_traces(hovertemplate=hover_template.get_heatmap_hover_template())
    heatmap_fig.update_layout(dragmode=False)
    heatmap_fig.update_layout(xaxis=dict(tickmode='linear'))
    return heatmap_fig

