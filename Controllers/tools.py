from random import randint
from Models.student import Student
from Models.mentor import Mentor
from Models.manager import Manager
from Models.office_manager import OfficeManager
from data_manager import DataManager


def gen_idx(position):
    """
    Returns unical id for new user

    Args:
        position: string
    """

    types_dict = {"student": "st", "mentor": "mt", "office": "ofc", "manager": "mgr"}
    random_idx = [str(randint(0, 9)) for number in range(4)]

    if position in types_dict:
        idx = types_dict[position] + ''.join(random_idx)
        is_available = False
        while not is_available:
            is_available = check_idx_availability(idx)
            if not is_available:
                idx = types_dict[position] + ''.join([str(randint(0, 9)) for number in range(4)])
        return idx


def check_idx_availability(idx):
    """
    Returns False if any of users already have given idx.
    Otherwise returns True.

    Args:
        idx: string
    """

    merged_list = Student.student_list + Mentor.mentor_list
    merged_list += Manager.manager_list + OfficeManager.office_managers_list
    for i in range(len(merged_list)):
        merged_list[i] = merged_list[i].idx

    if idx in merged_list:
        return False
    else:
        return True
