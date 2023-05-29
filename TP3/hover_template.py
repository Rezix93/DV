'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    heatmap_hover_template = "<span style='font-family:Roboto Slab'><b>Neighborhood:</b></span><span style='font-family:Roboto'> %{y}</span>" + "<br><span style='font-family:Roboto Slab'><b>Year:</b></span><span style='font-family:Roboto'> %{x}</span>" + "<br><span style='font-family:Roboto Slab'><b>Trees:</b></span><span style='font-family:Roboto'> %{z}</span><extra></extra>"

    return heatmap_hover_template

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    linechart_hover_template = "<span style='font-family:Roboto Slab'><b>Date:</b></span><span style='font-family:Roboto'> %{x}</span>" + "<br><span style='font-family:Roboto Slab'><b>Trees:</b></span><span style='font-family:Roboto'> %{y}<br /></span><extra></extra>"

    return linechart_hover_template

