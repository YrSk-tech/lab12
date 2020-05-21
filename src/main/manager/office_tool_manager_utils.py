from src.main.model.sort_type import SortType
from src.main.model.ruler import Ruler
from src.main.model.brand import Brand
from src.main.model.colour import Colour


class OfficeToolManagerUtils:

    @staticmethod
    def sort_by_price_in_uah(input_tool_list, input_sort_type):
        """
        Testing sorter by price in UAH
        >>> test_ruler_list = [test_ruler1,test_ruler2,test_ruler3]
        >>> OfficeToolManagerUtils.sort_by_price_in_uah(test_ruler_list, SortType(1))
        >>> print(test_ruler_list[0].price_in_uah)
        80
        >>> print(test_ruler_list[2].price_in_uah)
        200
        """
        if input_sort_type == SortType(1):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.price_in_uah)
        elif input_sort_type == SortType(2):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.price_in_uah, reverse=True)
        else:
            print("cant be sorted by price in uah")

    @staticmethod
    def sort_by_weight_in_grams(input_tool_list, input_sort_type):

        """
        Testing sorter by weight in grams
        >>> test_ruler_list = [test_ruler1, test_ruler2, test_ruler3]
        >>> OfficeToolManagerUtils.sort_by_weight_in_grams(test_ruler_list, SortType(2))
        >>> print(test_ruler_list[0].weight_in_grams)
        31
        >>> print(test_ruler_list[2].weight_in_grams)
        20
        """
        if input_sort_type == SortType(1):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.weight_in_grams)
        elif input_sort_type == SortType(2):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.weight_in_grams, reverse=True)
        else:
            print("cant be sorted by weight in grams")


if __name__ == '__main__':
    import doctest

    test_ruler1 = Ruler("Ukraine", 110, Brand.axent, Colour(1), 210, 20, 20)
    test_ruler2 = Ruler("Germany", 200, Brand.buromax, Colour(3), 330, 30, 30)
    test_ruler3 = Ruler("Poland", 80, Brand.levenhuk, Colour(1), 120, 31, 10)
    doctest.testmod(verbose=True)

