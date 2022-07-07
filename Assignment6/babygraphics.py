import tkinter
import babynames
import babygraphicsgui as gui

# Provided constants to load and draw the baby data
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    # >>> round(get_x_coordinate(1000, 0), 1)
    20.0
    # >>> round(get_x_coordinate(1000, 2), 1)
    180.0
    # >>> round(get_x_coordinate(1000, 11), 1)
    900.0
    """
    coordinate_x = GRAPH_MARGIN_SIZE + year_index * (width / GRAPH_MARGIN_SIZE + 1.5 * GRAPH_MARGIN_SIZE)
    return coordinate_x


def get_y_coordinate(height, rank):
    if rank == 1000:
        coordinate_y = WINDOW_HEIGHT - GRAPH_MARGIN_SIZE
    else:
        difference = height / MAX_RANK
        coordinate_y = GRAPH_MARGIN_SIZE + ((rank - 1) * difference)
    return coordinate_y


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas
    width = canvas.winfo_width()  # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas

    hrz_line_top = canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, WINDOW_WIDTH, GRAPH_MARGIN_SIZE)
    hrz_line_bottom = canvas.create_line(GRAPH_MARGIN_SIZE, WINDOW_HEIGHT - GRAPH_MARGIN_SIZE, WINDOW_WIDTH,
                                         WINDOW_HEIGHT - GRAPH_MARGIN_SIZE)

    for i in range(GRAPH_MARGIN_SIZE, (WINDOW_WIDTH - (4 * GRAPH_MARGIN_SIZE)), 4 * GRAPH_MARGIN_SIZE):
        vertical_line = canvas.create_line(i, 0, i, WINDOW_WIDTH)

    for y in range(len(YEARS)):
        year = YEARS[y]
        txt = canvas.create_text(GRAPH_MARGIN_SIZE + (y * (4 * GRAPH_MARGIN_SIZE)) + TEXT_DX,
                                 WINDOW_HEIGHT - GRAPH_MARGIN_SIZE,
                                 text=f'{year}',
                                 anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dictionary of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        name_data (dictionary): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot
    """
    draw_fixed_lines(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    for names in lookup_names:
        # Create Rank and Year data for names
        year_data = []
        rank_data = []
        for info in name_data[names]:
            year = info
            rank = name_data[names][info]
            year_data.append(year)
            rank_data.append(rank)

        for i in range(len(YEARS)):
            if YEARS[i] not in year_data:
                year_data.insert(i, YEARS[i])
                rank_data.insert(i, MAX_RANK)

        # Create X and Y coordinate list related with name
        x_coordinate_year = []
        y_coordinate_rank = []
        for i in range(len(year_data)):
            x = get_x_coordinate(WINDOW_WIDTH, i)
            x_coordinate_year.append(x)
            y = get_y_coordinate(WINDOW_HEIGHT, rank_data[i])
            y_coordinate_rank.append(y)

        # Coloring lines for GUI
        if len(lookup_names) <= len(COLORS):
            ind = lookup_names.index(names)
            color = COLORS[ind]
        else:
            ind = lookup_names.index(names) % len(COLORS)
            color = COLORS[ind]

        # Draw lines on canvas
        for m in range(len(x_coordinate_year) - 1):
            canvas.create_line(x_coordinate_year[m], y_coordinate_rank[m], x_coordinate_year[m + 1],
                               y_coordinate_rank[m + 1], width=LINE_WIDTH, fill=color)

        # Draw names and ranks on canvas
        for n in range(len(x_coordinate_year)):
            if rank_data[n] == 1000:
                rank_data[n] = '*'
                text_for = f'{names} {rank_data[n]}'
                canvas.create_text(x_coordinate_year[n], y_coordinate_rank[n], text=text_for, fill=color,
                                   anchor=tkinter.SW,
                                   )
            else:
                text_for = f'{names} {rank_data[n]}'
                canvas.create_text(x_coordinate_year[n], y_coordinate_rank[n], text=text_for, fill=color,
                                   anchor=tkinter.SW)


def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names Solution')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, name_data, draw_names, babynames.search_names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
