# 🤖 GOIT PYCORE HW-08 — Assistant Bot with Persistent Pickle Storage  
# 🧠 GOIT PYCORE HW-08 — Асистент-Бот із постійним збереженням через Pickle

---

## 🇬🇧 English Description

### 📘 Overview
This project implements a **command-line Assistant Bot** for managing an **address book**.  
The bot supports adding, editing, and deleting contacts, managing birthdays,  
and automatically saving/loading data using **`pickle` serialization**.  
When restarted, it restores the last saved session automatically.

---

### 🚀 Key Features

- 🗂️ **Address Book** with full CRUD functionality  
- 📞 Multiple phone numbers per contact  
- 🎂 Birthday management and upcoming reminders  
- 💾 Data persistence using `pickle` (auto-save and manual save)  
- 🧠 Auto-loads last autosave file on startup  
- 🧾 File operations (save, load, delete, list)  
- 🧪 Full test coverage with `pytest`  
- ⚙️ Modular **Clean Architecture**: BLL / DAL separation  

---

### 🧩 Architecture Overview

The project follows **Clean Architecture**, dividing logic into:
- **BLL (Business Logic Layer)** — services, command handlers, input logic  
- **DAL (Data Access Layer)** — entities, exceptions, storages, and file management  
- **Tests** — organized into categories (AddressBook, Bot, File, Helper)  

```
📦 goit-pycore-hw-08
┣━━ main.py                          # Application entry point
┣━━ data/                            # Pickle saves
┣━━ BLL/
┃   ┣━━ Services/                    # Business logic layer
┃   ┣━━ Decorators/                  # Command error handler
┃   ┗━━ Helpers/                     # Utility functions
┣━━ DAL/
┃   ┣━━ Entities/                    # Core domain models (Record, Name, Phone)
┃   ┣━━ Exceptions/                  # Custom exception classes
┃   ┣━━ FileManagers/                # Pickle file manager
┃   ┗━━ Storages/                    # Address book in-memory storage
┣━━ Tests/                           # Pytest-based test suite
┃   ┣━━ BotTests/
┃   ┣━━ FileTests/
┃   ┗━━ AddressBookManagementTests/
┗━━ .gitignore
```

---

### 💬 Available Commands

| Command | Description |
|----------|-------------|
| `hello` | Greets the user |
| `add-contact [name] [phone]` | Adds a new contact |
| `add-phone [name] [new_phone]` | Adds another phone to a contact |
| `add-birthday [name] [dd.mm.yyyy]` | Adds or updates a birthday |
| `show-birthday [name]` | Displays a contact’s birthday |
| `upcoming-birthdays` | Shows birthdays for the next 7 days |
| `show-all-contacts` | Lists all contacts |
| `delete-contact [name]` | Deletes a contact |
| `save [name]` | Saves current state (creates timestamped `.pkl`) |
| `load [name]` | Loads state from a pickle file |
| `show-all-files` | Lists all saved files |
| `delete-file [name]` | Deletes a specific file |
| `help` | Displays all available commands |
| `exit` / `close` | Exits the bot (asks for autosave) |

---

### 🧪 Testing

Run all tests:
```bash
pytest -v
```

Run specific test groups:
```bash
pytest Tests/FileTests/test_pickle_file_service.py -v
pytest Tests/BotTests/test_end_to_end_bot_flow.py -v
```

All tests are organized by functional area:
- `AddressBookManagementTests` — CRUD and record handling  
- `BotTests` — command flow and full interaction  
- `FileTests` — serialization and persistence checks  

---

### ⚙️ Installation & Run

```bash
git clone https://github.com/<your-username>/goit-pycore-hw-08.git
cd goit-pycore-hw-08
python -m venv .venv
.venv\Scripts\activate        # Windows
# or
source .venv/bin/activate       # macOS / Linux

pip install pytest
python main.py
```

---

### 💾 Persistence Mechanism

- Uses Python’s `pickle` for full object serialization.
- Each save file is timestamped, e.g.:
  ```
  autosave_20251107_184422.pkl
  ```
- On launch, the bot loads the **most recent autosave** from the `data/` folder.

---

### 🧑‍💻 Author

**Roman Kulchytskyi**  
Full Stack Developer (.NET / Python)  
📧 [buma.ua@gmail.com](mailto:buma.ua@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/kulchitskiy-r)

---

## 🇺🇦 Український опис

### 📘 Огляд
Цей проєкт реалізує **консольного асистент-бота** для управління **адресною книгою**.  
Бот підтримує додавання, редагування та видалення контактів, керування днями народження  
і автоматичне збереження/відновлення даних через **серіалізацію `pickle`**.  
Після перезапуску застосунок відновлює останній autosave.

---

### 🚀 Основні можливості

- 🗂️ **Адресна книга** з повним CRUD-функціоналом  
- 📞 Підтримка кількох телефонів для одного контакту  
- 🎂 Збереження та перегляд днів народження  
- 📅 Перегляд контактів із майбутніми днями народження  
- 💾 Постійне збереження стану через `pickle`  
- 🔄 Автоматичне завантаження останнього autosave  
- 📤 Перегляд, видалення та ручне збереження файлів  
- 🧪 Повне покриття тестами `pytest`  
- 🧱 Чиста архітектура (Clean Architecture, BLL/DAL)

---

### 🧩 Структура проєкту

```
📦 goit-pycore-hw-08
┣━━ main.py                          # Application entry point
┣━━ data/                            # Pickle saves
┣━━ BLL/
┃   ┣━━ Services/                    # Business logic layer
┃   ┣━━ Decorators/                  # Command error handler
┃   ┗━━ Helpers/                     # Utility functions
┣━━ DAL/
┃   ┣━━ Entities/                    # Core domain models (Record, Name, Phone)
┃   ┣━━ Exceptions/                  # Custom exception classes
┃   ┣━━ FileManagers/                # Pickle file manager
┃   ┗━━ Storages/                    # Address book in-memory storage
┣━━ Tests/                           # Pytest-based test suite
┃   ┣━━ BotTests/
┃   ┣━━ FileTests/
┃   ┗━━ AddressBookManagementTests/
┗━━ .gitignore
```

---

### 💬 Доступні команди

| Команда | Опис |
|----------|------|
| `hello` | Привітання від бота |
| `add-contact [name] [phone]` | Додає новий контакт |
| `add-phone [name] [new_phone]` | Додає ще один телефон |
| `add-birthday [name] [dd.mm.yyyy]` | Додає або оновлює день народження |
| `show-birthday [name]` | Показує день народження |
| `upcoming-birthdays` | Виводить наближені дні народження |
| `show-all-contacts` | Відображає всі контакти |
| `delete-contact [name]` | Видаляє контакт |
| `save [name]` | Зберігає поточний стан у файл |
| `load [name]` | Завантажує стан із файлу |
| `show-all-files` | Показує всі файли збережень |
| `delete-file [name]` | Видаляє файл |
| `help` | Виводить список усіх команд |
| `exit` / `close` | Вихід із програми (пропонує autosave) |

---

### ⚙️ Встановлення та запуск

```bash
git clone https://github.com/<your-username>/goit-pycore-hw-08.git
cd goit-pycore-hw-08
python -m venv .venv
.venv\Scripts\activate        # Windows
# або
source .venv/bin/activate       # macOS / Linux

pip install pytest
python main.py
```

---

### 🧪 Тестування

Запуск усіх тестів:
```bash
pytest -v
```

Приклади запуску окремих модулів:
```bash
pytest Tests/FileTests/test_pickle_file_service.py -v
pytest Tests/BotTests/test_end_to_end_bot_flow.py -v
```

---

### 💾 Збереження даних

- Використовується модуль **`pickle`** для серіалізації об’єктів Python.  
- Кожен autosave має формат:
  ```
  autosave_YYYYMMDD_HHMMSS.pkl
  ```
- При запуску бот **автоматично завантажує останній збережений стан** із папки `data/`.

---

### 🧑‍💻 Автор

**Роман Кульчицький**  
Full Stack Developer (.NET / Python)  
📧 [buma.ua@gmail.com](mailto:buma.ua@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/kulchitskiy-r)

---

### 🏁 Ліцензія

This project was created for educational purposes within **GoIT Python Core**.  
Цей проєкт створено в рамках курсу **GoIT Python Core** і може бути використаний для навчання.
