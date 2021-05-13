"""Module *plot* various utils for plotting maps of Sri Lanka.

To plot a basic outline map of Sri Lanka with province boundaries,

.. code-block:: python

    >> from geo import geodata
    >> from geo import plot
    >> geodata = geodata.get_region_geodata('LK', 'province')
    >> plot.plot_geodata(geodata)

Similarly, to plot Colombo District with DSD boundaries,

.. code-block:: python

    >> geodata = geodata.get_region_geodata('LK-11', 'dsd')
    >> plot.plot_geodata(geodata)

To add a title, subtitle and footer text to the figure,s

.. code-block:: python

    >> plot.plot_geodata(
        geodata,
        title='Colombo District',
        sub_title='DSD Boundaries',
        footer_text='Data Source: http://www.statistics.gov.lk/',
        label_field_key='id',
    )




"""

import matplotlib.pyplot as plt
BASE_FONT_SIZE = 16


def plot_geodata(
    geodata,
    title='',
    sub_title='',
    footer_text='',
    label_field_key=None,
    region_to_color_map=None,
    func_draw_on_figure=None,
    func_render_region=None,
):
    """Plot region_id."""
    plt.rc('font', family='Futura')

    fig, axis = plt.subplots()

    color = None
    if region_to_color_map:
        color = geodata['id'].map(region_to_color_map)

    geodata.plot(
        ax=axis,
        color=color,
    )

    # sub-region labels
    geodata['center'] = geodata['geometry'].centroid
    geodata_copy = geodata.copy()
    geodata_copy.set_geometry("center", inplace=True)

    if not func_render_region and label_field_key:
        def func_render_region(centroid_x, centroid_y, region_data):
            plt.text(
                centroid_x,
                centroid_y,
                region_data[label_field_key],
                fontsize=5,
                horizontalalignment='center',

            )

    for [centroid_x, centroid_y, region_data] in zip(
        geodata_copy.geometry.x,
        geodata_copy.geometry.y,
        geodata_copy.to_dict('records'),
    ):
        func_render_region(centroid_x, centroid_y, region_data)

    if not func_draw_on_figure:

        def func_draw_on_figure(fig):

            def draw_text(text_x, text_y, text, p_font_size=1):
                fig.text(
                    x=text_x,
                    y=text_y,
                    s=text,
                    fontsize=BASE_FONT_SIZE * p_font_size,
                    horizontalalignment='center',
                )

            draw_text(0.5, 0.94, title, 1)
            draw_text(0.5, 0.90, sub_title, 0.75)
            draw_text(0.5, 0.06, footer_text, 0.5)

    func_draw_on_figure(fig)

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    from geo import geodata
    geodata = geodata.get_region_geodata('LK-11', 'dsd')
    plot_geodata(
        geodata,
        title='Colombo District',
        sub_title='DSD Boundaries',
        footer_text='Data Source: http://www.statistics.gov.lk/',
        label_field_key='hasc',
    )
