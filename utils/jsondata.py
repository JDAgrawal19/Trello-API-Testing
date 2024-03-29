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

create_board_without_org_data = {"name": "board of NITR"}

update_board_name = {"name": "board_of_JECRC", "idOrganization": "put_id_of_org_here"}

update_board_name_empty = {"name": "", "idOrganization": "put_id_of_org_here"}

create_list_data = {"name": "List of items", "idBoard": "put_board_id_here"}

create_list_data_with_empty_name = {"name": "  ", "idBoard": "put_board_id_here"}

update_list_name_data ={"name": "List of UI Software"}

move_list_to_new_board_data = {"value": "id_of_new_board"}

data_add_member_in_board = {"type": "normal"}

set_soft_limit_list = {"value": 1}

data_get_the_board_card_is_on = {"fields": "all"}

get_members_on_card = {"fields": "avatarHash,fullName,initials,username"}

create_card_data = {"idList": "put_id_of_list_here", "name": "selenium Card"}

data_add_member_in_card = {"value": "put_id_of_member_here"}

data_archive_or_unarchive_a_list = {"value": "true"}

data_susbscribe_or_unsubscribe_a_list = {"value": "true"}

data_add_comment_to_card = {"text": "This card belongs to JD Agrawal"}

data_add_attachment_to_card = {"name": "facebook URL", "url": "https://www.facebook.com/"}
