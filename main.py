from BLL.Services.CommandService.CommandService import CommandService
from BLL.Services.InputService.InputService import InputService
from BLL.Services.PickleFileService.PickleFileService import PickleFileService
from BLL.Services.RecordService.RecordService import RecordService
from DAL.FileManagers.PickleFileManager.PickleFileManager import PickleFileManager
from DAL.Storages.AddressBookStorage import AddressBookStorage
from DAL.Exceptions.AlreadyExistException import AlreadyExistException
from DAL.Exceptions.ExitBotException import ExitBotException
from DAL.Exceptions.InvalidException import InvalidException
from DAL.Exceptions.NotFoundException import NotFoundException

def main():
    book_storage = AddressBookStorage()
    record_service = RecordService(book_storage)
    file_manager = PickleFileManager()
    file_service = PickleFileService(file_manager, book_storage)
    command_service = CommandService(record_service, file_service)
    input_service = InputService(command_service)

    print('\n🤖 Welcome to the Assistant Bot!')
    print("Type 'help' to see available commands.\n")

    try:
        latest_file_name = file_service.get_latest_file_name()
        if latest_file_name:
            file_service.load_by_name(latest_file_name)
            print(f"📂 Loaded last saved state from '{latest_file_name}'")
        else:
            print("📂 No saved state found, starting with empty address book.")
    except Exception as e:
        print(f"⚠️ Could not load previous state: {e}")

    while True:
        try:
            user_input = input('Enter a command: ')

            if not user_input:
                continue

            print(input_service.handle(user_input))

        except InvalidException as ic:
            print(ic)
            continue
        except AlreadyExistException as aee:
            print(aee)
        except NotFoundException as nf:
            print(nf)
        except KeyboardInterrupt:
            try:
                input_service.handle('exit')
            except ExitBotException as eb:
                print(eb)
            break
        except ExitBotException as eb:
            print(eb)
            break
        except Exception as ex:
            print(f'💥 Unexpected error: {ex}')
            break

if __name__ == "__main__":
    main()
