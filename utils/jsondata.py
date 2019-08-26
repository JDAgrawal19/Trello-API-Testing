from utils.constants import *

create_org_with_correct_name = {"displayName": "HashedIN", "name":"hashedin_159"}

create_org_incorrect_name_uppercase_letter = {"displayName": "HASHERS", "name": "HASHER546"}

create_org_incorrect_name_special_char = {"displayName": "JDAGRAWAL123", "name": "@#$%^&"}

update_org_correct_display_name = {"displayName": "Jitesh"}

update_org_incorrect_display_name_ends_with_space = {"displayName": "Jitesh "}

update_org_incorrect_display_name_empty = {"displayName": ""}

create_member_or_update_type = {"type": "normal"}

get_boards_data = {"filter": "all"}

create_board_data = {"name": "board_of_hashers", "idOrganization": "put_id_of_org_here"}

create_list_data = {"name": "list_1", "idBoard": "id"}

add_member_in_board = {"type": "normal"}

set_soft_limit_list = {"value": 3}

get_the_board_card_is_on = {"fields": "all"}

get_members_on_card = {"fields":"avatarHash,fullName,initials,username"}
