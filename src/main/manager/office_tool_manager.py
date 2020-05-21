
from src.main.model.brand import Brand
from src.main.model.colour import Colour
from src.main.model.ruler import Ruler


class OfficeToolManager:

    def __init__(self, office_tool_list):
        self.office_tool_list = office_tool_list

    def find_by_colour(self, input_colour):

        """
        Testing search method by colour
        >>> print(len(office_tool_manager.find_by_colour(Colour(1))))
        2
        >>> print(len(office_tool_manager.find_by_colour(Colour(3))))
        1
        """
        result_list = []
        for office_tool in self.office_tool_list:
            if office_tool.colour == input_colour:
                result_list.append(input_colour)
        return result_list


if __name__ == '__main__':
    import doctest

    ruler1 = Ruler("Ukraine", 110, Brand.axent, Colour(1), 30, 100, 20)
    ruler2 = Ruler("Germany", 200, Brand.buromax, Colour(3), 10, 80, 30)
    ruler3 = Ruler("Poland", 80, Brand.levenhuk, Colour(1), 120, 31, 10)
    otm = OfficeToolManager(office_tool_list=[
        ruler1,
        ruler2,
        ruler3])

    doctest.testmod(verbose=True, extraglobs={'office_tool_manager': otm})
