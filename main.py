from data_db import dbname, user, password, host, port
import psycopg2
import requests

# Функция для выполнения запросов к БД PostgreSQL
def execute_query(query):
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    result = cur.fetchall()
    conn.close()
    return result

# Функция для обновления пола контакта в Битрикс24
def update_contact_gender(contact_id, gender):
    webhook_url = "your_bitrix24_webhook_url"
    payload = {
        "fields": {
            "GENDER_ID": gender  # Поле GENDER_ID: 1 - Мужчина, 2 - Женщина
        }
    }
    response = requests.post(webhook_url, json=payload)
    return response.status_code == 200

# Функция для определения пола по имени из базы данных
def get_gender_from_database(name):
    if name in execute_query("SELECT name FROM names_man"):
        return 1  # Мужчина
    elif name in execute_query("SELECT name FROM names_woman"):
        return 2  # Женщина
    else:
        return None  # Пол не найден

# Функция для обработки данных контакта и обновления пола
def process_contact(contact_id, name):
    gender = get_gender_from_database(name)
    if gender is not None:
        if update_contact_gender(contact_id, gender):
            print("Пол контакта успешно обновлен.")
        else:
            print("Ошибка при обновлении пола контакта.")
    else:
        print("Имя контакта не найдено в базе данных.")

# Пример вызова функции process_contact с ID и именем контакта
process_contact("contact_id", "contact_name")
