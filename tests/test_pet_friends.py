from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_getapi_key_for_valid_user(email=valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter = ''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name = 'Борис', animal_type = 'хряк', age = '5', pet_photo = 'images/pig.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_successful_update_self_pet_info(self, name='Мурзик', animal_type='Котэ', age=5):
   _, auth_key = self.pf.get_api_key(valid_email, valid_password)
   _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

   if len(my_pets['pets']) > 0:
       status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'],
                                                name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("There is no my pets")

#__________________________Домашнее_задание___________________________

def test_getapi_key_for_no_valid_user(email = 'неправильнаяПочта@mail.ru', password = 'неправильныйПароль'):
    status, result = pf.get_api_key(email, password)
    assert status == 401

def test_getapi_key_for_empty_user(email = '', password = ''):
    status, result = pf.get_api_key(email, password)
    assert status == 401

def test_getapi_key_for_no_valid_email(email = 'неправильнаяПочта@mail.ru', password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 401

def test_getapi_key_for_no_email(email = '', password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 401

def test_getapi_key_for_no_valid_password(email = valid_email, password = 'неправильныйПароль'):
    status, result = pf.get_api_key(email, password)
    assert status == 401

def test_getapi_key_for_no_password(email = valid_email, password = ''):
    status, result = pf.get_api_key(email, password)
    assert status == 401

def test_add_new_pet_with_no_valid_age(name = 'Борис', animal_type = 'хряк', age = 'НаборЗапрещённыхСимволов', pet_photo = 'images/pig.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_add_new_pet_with_no_valid_type_of_pet_photo(name = 'Борис', animal_type = 'хряк', age = '5', pet_photo = 'images/X.gif'):
    """Пытаемся загрузить неподходящий формат фото"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 415

def test_add_new_pet_with_no_valid_animal_type(name = 'Борис', animal_type = 'НаборЗапрещённыхСимволов', age = '5', pet_photo = 'images/pig.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_add_new_pet_with_no_valid_name(name = 'НаборЗапрещённыхСимволов', animal_type = 'хряк', age = '5', pet_photo = 'images/pig.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_add_new_pet_with_no_valid_photo(name = 'Борис', animal_type = 'хряк', age = '5', pet_photo = 'images/5GB_file.jpg'):
    """Допустим, что по заданию у нас есть ограничение на размер файла и мы пытаемся загрузить фото весом 5 гигов"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 413

def test_get_all_pets_with_no_valid_password(filter=''):
    _, auth_key = pf.get_api_key(valid_email, 'неправильныйПароль')
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403
    assert len(result['pets']) == 0

def test_get_all_pets_with_no_valid_email(filter=''):
    _, auth_key = pf.get_api_key('неправильнаяПочта@mail.ru', valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403
    assert len(result['pets']) == 0

def test_add_new_pet_with_state_censorship(name = 'Путин', animal_type = 'диктатор', age = '69', pet_photo = 'images/Put.jpg'):
    """Я понимаю что роскомнадзор так быстро не работает. Написал просто для демонстрации логики"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 451

#Далее скопировано с GitHub dimm23


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()