from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'The user has navigate to Home page')
def step_nav_home_page(context):
    expected_title = "Пошук – Gisolo"
    assert context.driver.title == expected_title


@when(u'User enters valid pattern into Search box field')
def step_enter_valid_pattern(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/form/input[3]").send_keys("iphone 15")


@when(u'User clicks on Search button')
def step_click_search_button(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/form/span/button").click()


@then(u'Valid page should get displayed')
def step_valid_page_displayed(context):
    count_of_search = int(
        context.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/nav/span[2]").text.split(" ")[1])
    assert count_of_search > 0, "No any match during searching ..."
