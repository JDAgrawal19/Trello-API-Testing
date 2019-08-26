trello_api_key = "45d2ae9092edd498b1612e585642c9da"

trello_access_token = "3f79ac95ee4c809acb11557eca9d75c3d94285439a7cf632695b43d52b1aee52"

path_data_json_file = "/home/jitesh_dhoot/mycode_api_test/data/data.json"

OAUTH_DATA = {"key": trello_api_key, "token": trello_access_token}

member1 = "ashusingla3"

member2 = "ankitpoonia3"

url_create_organization = "https://api.trello.com/1/organizations"

url_delete_organization = "https://api.trello.com/1/organizations/{id}"

url_update_organization = "https://api.trello.com/1/organizations/{id}"

url_get_members_of_organization = "https://api.trello.com/1/organizations/{id}/members"

url_add_memeber_in_organization = "https://api.trello.com/1/organizations/{id}/members/{idMember}"

url_remove_member_from_organization = "https://api.trello.com/1/organizations/{id}/members/{idMember}"

url_remove_member_from_org_and_all_boards = "https://api.trello.com/1/organizations/{id}/members/{idMember}/all"

url_get_boards_of_organization = "https://api.trello.com/1/organizations/{id}/boards"

url_create_board = "https://api.trello.com/1/boards/"

url_delete_board = "https://api.trello.com/1/boards/{id}"

url_add_member_in_board = "https://api.trello.com/1/boards/{id}/members/{idMember}"

url_remove_member_from_board = "https://api.trello.com/1/boards/{id}/members/{idMember}"

url_get_members_from_board =  "https://api.trello.com/1/boards/{id}/members"

url_update_board_field = "https://api.trello.com/1/boards/{id}"

url_create_list_on_board = "https://api.trello.com/1/lists"

url_update_list_field = "https://api.trello.com/1/lists/{id}"

url_rename_a_list =  "https://api.trello.com/1/lists/{id}/name"

url_get_board_a_list_is_on = "https://api.trello.com/1/lists/{id}/cards"

url_move_list_to_new_board = "https://api.trello.com/1/lists/id/idBoard"

url_set_soft_limit_number_of_cards = "https://api.trello.com/1/lists/{id}/softLimit"

url_get_cards_in_list = "https://api.trello.com/1/lists/{id}/cards"

url_create_new_card = "https://api.trello.com/1/cards"

url_add_member_to_card = "https://api.trello.com/1/cards/{id}/{idMembers}"

url_delete_card = "https://api.trello.com/1/cards/id"

url_remove_member_from_card = "https://api.trello.com/1/cards/{id}/idMembers/{idMember}"