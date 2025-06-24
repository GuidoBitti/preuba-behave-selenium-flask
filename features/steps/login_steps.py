from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("the user is on the login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000")

@when('the user enters username "admin" and password "1234"')
def step_impl(context):
    context.driver.find_element(By.NAME, "username").send_keys("admin")
    context.driver.find_element(By.NAME, "password").send_keys("1234")
    context.driver.find_element(By.TAG_NAME, "button").click()

@then("the user should be redirected to the dashboard")
def step_impl(context):
    assert "dashboard" in context.driver.current_url
    context.driver.quit()
