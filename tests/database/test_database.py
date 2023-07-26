import pytest
from modules.common.database import Database
from modules.common.general import General


# The required tests from the course
@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    # Check quantity of orders equal to 7
    assert len(orders) == 7

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# The additional tests


@pytest.mark.database_additional
def test_type_of_data_primary_key_from_products():
    db = Database()
    list_of_id = db.get_all_primary_keys_from_table("id", "products")
    for element in list_of_id:
        assert (type(element[0])) == int


@pytest.mark.database_additional
def test_type_of_data_primary_key_from_customers():
    db = Database()
    list_of_id = db.get_all_primary_keys_from_table("id", "customers")
    for element in list_of_id:
        assert (type(element[0])) == int


@pytest.mark.database_additional
def test_type_of_data_primary_key_from_orders():
    db = Database()
    list_of_id = db.get_all_primary_keys_from_table("id", "orders")
    for element in list_of_id:
        assert (type(element[0])) == int


@pytest.mark.database_additional
def test_type_of_data_foreign_keys_from_orders():
    db = Database()
    list_of_orders = db.get_all_from_table("orders")
    for element in list_of_orders:
        assert (type(element[1])) == int
        assert (type(element[2])) == int


@pytest.mark.database_additional
def test_type_of_data_quantity_from_products():
    db = Database()
    list_of_products = db.get_all_from_table("products")
    for element in list_of_products:
        assert (type(element[3])) == int


@pytest.mark.database_additional
def test_product_qnt_sum():
    db = Database()
    result = db.get_sum_column_from_table("quantity", "products")
    assert result[0][0] == 75


@pytest.mark.database_additional
def test_check_table_products_is_not_empty():
    db = Database()
    list_of_data = db.get_count_column_table("id", "products")
    assert len(list_of_data) != 0


@pytest.mark.database_additional
def test_check_table_customers_is_not_empty():
    db = Database()
    list_of_data = db.get_count_column_table("id", "customers")
    assert len(list_of_data) != 0


@pytest.mark.database_additional
def test_check_table_orders_is_not_empty():
    db = Database()
    list_of_data = db.get_count_column_table("id", "orders")
    assert len(list_of_data) != 0


@pytest.mark.database_additional
def test_check_orders_by_product_id():
    db = Database()
    list_of_data = db.get_orders_by_foreign_key("product_id", "4")
    assert len(list_of_data) == 3


@pytest.mark.database_additional
def test_check_orders_by_product_id():
    db = Database()
    list_of_data = db.get_orders_by_foreign_key("customer_id", "3")
    assert len(list_of_data) == 2


@pytest.mark.database_additional_negative
def test_check_field_name_from_products():
    db = Database()
    db.insert_product(99, "test!", "data", 999)
    list_of_data = db.get_all_from_table_by_id("products", 99)
    gn = General()
    special_symbols = gn.check_string_on_special_symbols(list_of_data[0][1])
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

    # This assertion shows that field has potential issue.
    # This field can contain unacceptable symbols
    assert special_symbols == True


@pytest.mark.database_additional_negative
def test_check_field_name_from_customers():
    db = Database()
    db.insert_customer(99, "Jo!hn1", "test", "test", 30500, "Test")
    list_of_data = db.get_all_from_table_by_id("customers", 99)
    gn = General()
    digits = gn.check_string_on_digit(list_of_data[0][1])
    special_symbols = gn.check_string_on_special_symbols(list_of_data[0][1])
    db.delete_record_from_table_by_id("customers", 99)
    qnt = db.get_all_from_table_by_id("customers", 99)

    assert len(qnt) == 0

    # This assertion shows that field has potential issue.
    # This field can contain unacceptable symbols OR digits
    assert digits == True
    assert special_symbols == True


@pytest.mark.database_additional_negative
def test_check_field_city_from_customers():
    db = Database()
    db.insert_customer(99, "John", "Test", "Ky2iv!", 30500, "Test")
    list_of_data = db.get_all_from_table_by_id("customers", 99)
    gn = General()
    digits = gn.check_string_on_digit(list_of_data[0][3])
    special_symbols = gn.check_string_on_special_symbols(list_of_data[0][3])
    db.delete_record_from_table_by_id("customers", 99)
    qnt = db.get_all_from_table_by_id("customers", 99)

    assert len(qnt) == 0

    # This assertion shows that field has potential issue.
    # This field can contain unacceptable symbols OR digits
    assert digits == True
    assert special_symbols == True


@pytest.mark.database_additional_negative
def test_check_field_country_from_customers():
    db = Database()
    db.insert_customer(99, "John", "Test", "Kyiv", 30500, "Ukr5aine!")
    list_of_data = db.get_all_from_table_by_id("customers", 99)
    gn = General()
    digits = gn.check_string_on_digit(list_of_data[0][5])
    special_symbols = gn.check_string_on_special_symbols(list_of_data[0][5])
    db.delete_record_from_table_by_id("customers", 99)
    qnt = db.get_all_from_table_by_id("customers", 99)

    assert len(qnt) == 0

    # This assertion shows that field has potential issue.
    # This field can contain unacceptable symbols OR digits
    assert digits == True
    assert special_symbols == True


@pytest.mark.database_additional_negative
def test_check_field_postalCode_from_customers():
    db = Database()
    db.insert_customer(99, "John", "Test", "Kyiv", "QwErTy!", "Ukraine")
    list_of_data = db.get_all_from_table_by_id("customers", 99)
    print(type(list_of_data[0][4]))
    gn = General()
    digits = gn.check_string_on_digit(list_of_data[0][4])
    special_symbols = gn.check_string_on_special_symbols(list_of_data[0][4])
    db.delete_record_from_table_by_id("customers", 99)
    qnt = db.get_all_from_table_by_id("customers", 99)

    assert len(qnt) == 0

    # This assertion shows that field has potential issue.
    # This field can contain unacceptable symbols OR letters
    # Besides, type of data this field is not digitally
    assert type(list_of_data[0][4]) != int
    assert digits == False
    assert special_symbols == True
