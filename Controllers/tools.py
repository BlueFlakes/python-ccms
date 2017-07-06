from random import randint

class Tools:

    @staticmethod
    def gen_idx(position):
        types_dict = {"student": "st", "mentor": "mt", "office": "ofc", "manager": "mgr"}
        random_idx = [str(randint(0, 9)) for number in range(4)]

        if position in types_dict:
            idx = types_dict[position] + ''.join(random_idx)
            return idx
