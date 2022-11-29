"""Example."""

from utils.xmlx import _

from geo import alt

BOX_PER_GEO = 800
DIM_PER_BOX = 1000 / BOX_PER_GEO


def get_altitude_matrix(min_latlng, max_latlng):
    min_lat, min_lng = min_latlng
    max_lat, max_lng = max_latlng

    lat_span, lng_span = max_lat - min_lat, max_lng - min_lng
    print(f'{lat_span=}, {lng_span=}')

    n_x = (int)(lng_span * BOX_PER_GEO)
    n_y = (int)(lat_span * BOX_PER_GEO)
    print(f'{n_x=}, {n_y=}')

    altitude_matrix = []
    for i_x in range(n_x):
        print(i_x, n_x, end="\r")
        lng = min_lng + i_x / BOX_PER_GEO
        altitude_matrix_row = []
        for i_y in range(n_y):
            lat = min_lat + i_y / BOX_PER_GEO
            try:
                altitude = alt.get_altitude([lat, lng])
            except BaseException:
                altitude = 0
            altitude_matrix_row.append(altitude)
        altitude_matrix.append(altitude_matrix_row)
    return altitude_matrix


def get_color_from_altitude(altitude):
    if altitude < 1:
        return "red"
    if altitude < 2:
        return "orange"
    if altitude < 5:
        return "yellow"
    if altitude < 10:
        return "green"
    return "darkgreen"


def render_map(altitude_matrix):
    n_x = len(altitude_matrix)
    n_y = len(altitude_matrix[0])
    width, height = n_x * DIM_PER_BOX, n_y * DIM_PER_BOX

    rendered_boxes = []
    for i_x in range(n_x):
        for i_y in range(n_y):
            altitude = altitude_matrix[i_x][i_y]

            color = get_color_from_altitude(altitude)
            rendered_boxes.append(
                _(
                    'rect',
                    None,
                    dict(
                        x=i_x * DIM_PER_BOX,
                        y=(n_y - i_y - 1) * DIM_PER_BOX,
                        width=DIM_PER_BOX,
                        height=DIM_PER_BOX,
                        fill=color,
                        stroke="none",
                    ),
                )
            )
    svg = _('svg', rendered_boxes, dict(width=width, height=height))
    svg_file = "src/geo/examples/example4.svg"
    svg.store(svg_file)


if __name__ == '__main__':
    altitude_matrix = get_altitude_matrix(
        # [5.9, 79.5],
        # [9.9, 81.9],
        # [8.95, 79.65],
        # [9.13, 80.00],
        [6.881322, 79.824786],
        [6.956815, 79.924865],
    )
    render_map(altitude_matrix)
