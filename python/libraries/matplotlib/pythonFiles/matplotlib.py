from string import Template

import matplotlib.pyplot as plt
import numpy as np

'''
    Generate 10 rows for 20 values each

    For each row create a different graph
'''


# logging.basicConfig(level=logging.DEBUG)


def generate_rows_of_data() -> np.ndarray:
    """
        Create a set of 10 rows with 20 points
    """
    np.random.seed(0)
    data = np.random.randint(0, 100, size=(10, 20))
    return data


def configure_plot(ax, y_data: list, index_2d: tuple) -> None:
    """
        Create the graphs with the same characteristics

        ax          -- The graph itself
        y_data      -- The data for the y-axis
        index_2d    -- The location in the list when the graph ( ax is stored )

    """

    def generate_string_from_template(index_2d: tuple):
        """
            Create the title for each subplot

            Input
                x: The x coordinate in the subplot array
                y: The y coordinate in the subplot array

            Output
                A string providing the x,y coordinates of the subplot in the array.
        """
        graph_title_template = Template("Subplot[$x, $y]")
        title = graph_title_template.substitute(x=str(index_2d[0]), y=str(index_2d[1]))
        return title

    # Create the title for each plot
    ax.set_title(generate_string_from_template(index_2d))

    # Set the range of the X and Y axis
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 100)

    x_data = range(1, 21)
    ax.plot(x_data, y_data)
    return ax

def plot_all() -> None:
    """
        Plots each row in a separate plot

        Input: A list where each row is plotted in a separate graph
        Output: A collection of graphs
    """
    data_rows = generate_rows_of_data()

    number_of_cols_for_plot = int(len(data_rows) / 2)

    #
    # Create a figure that will contain the subplots
    #    figsize controls the size of the whole figure.  The bigger the
    #            size the subplots that can fit easily into the figure
    #    subtitle -- Sets the title for the total collection of subplots
    fig, axs = plt.subplots(2, number_of_cols_for_plot, figsize=(25.6, 9.6))
    fig.suptitle("All Plots")

    #
    # Retrieve each subplot and configure the graph for it
    #
    for x in range(0, 2):
        for y in range(0, number_of_cols_for_plot):
            ax = axs[x][y]
            data_row = data_rows[x * 5 + y]
            ax = configure_plot(ax, data_row, (x, y))


plot_all()
plt.show()
