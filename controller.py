import model
import view


def start():
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()
        if user_choice > 8 or user_choice < 1:
            view.error_enter()
        else:
            match user_choice:
                case 1:
                    phone_book = model.get_phone_book()
                    view.show_contacts(phone_book)
                case 2:
                    model.open_phone_book()
                    view.load_success()
                case 3:
                    model.save_phone_book()
                    view.save_success()
                case 4:
                    new = list(view.new_contact())
                    model.update_phone_book(new)
                case 5:
                    cha = view.info_cha_na()
                    cha1 = list(view.change_cont())
                    model.change_person(cha, cha1, contact=cha1)
                case 6:
                    dele = view.delete_contact()
                    model.delete_cont(dele)
                    view.info_fall_del()
                case 7:
                    search = view.find_contact()
                    result = model.search_contact(search)
                    view.show_contacts(result)
