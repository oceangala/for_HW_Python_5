import model
import view


def stаrt():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл сохранён')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                search = view.search_text()
                view.find_contacts(pb, 'Ничего не найдено', search)
            case 5:
                contact = view.add_contact()
                model.add_contact(contact)
            case 6:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите индекс изменяемого контакта')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} изменён')
            case 7:
                index = view.input_index('Введите индекс удаляемого контакта: ')
                model.del_contact(pb, index)
                view.show_message("Контакт удалён")
            case 8:
                view.show_message('До свидания')
                break
