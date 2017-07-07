from random import randint


class Tools:
    """Class with logic for generating users id"""

    @staticmethod
    def gen_idx(position):
        """
        Generate user id
        """

        types_dict = {"student": "st", "mentor": "mt", "office": "ofc", "manager": "mgr"}
        random_idx = [str(randint(0, 9)) for number in range(4)]

        if position in types_dict:
            idx = types_dict[position] + ''.join(random_idx)
            return idx
