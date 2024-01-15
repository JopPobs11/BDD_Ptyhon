from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@given(u'I am on the home Page')
def step_impl(context):
    context.browser.get("https://www.tokopedia.com/")
    assert context.browser.find_element(By.CSS_SELECTOR, "h2.css-jevxat").text == "Kategori Pilihan"

@when(u'I click Search Bar')
def step_impl(context):
    element = context.browser.find_element(By.CSS_SELECTOR, '[data-testid="txtHeaderSearchBar"]')
    element.click()

@when(u'I fill laptop asus')
def step_impl(context):
    # element = context.browser.find_element(By.CSS_SELECTOR, '[data-testid="txtHeaderSearchBar"]')
    element = WebDriverWait(context.browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="txtHeaderSearchBar"] input'))
    )
    element.clear()
    element.send_keys("laptop asus", Keys.RETURN)

@then(u'I will see list of laptop asus')
def step_impl(context):
    expected_text = "laptop asus" 

    search_results_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="dSRPSearchInfo"]'))
    )
    search_results_text = search_results_element.text
    
    assert expected_text.lower() in search_results_text.lower(), \
        f"Expected '{expected_text}' in search results, but not found. Actual: {search_results_text}" 
    


@given(u'I am on login page')
def step_impl(context):
    context.browser.get("https://www.tokopedia.com/login")
    assert context.browser.find_element(By.CSS_SELECTOR, "h3.css-14sozj8-unf-heading.e1qvo2ff3").text == "Masuk"

@when(u'I fill email with valid credential')
def step_impl(context):
    nomor = "082296166855"
    
    login_step = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, 'email-phone'))
    )

    login_step.clear()
    login_step.send_keys(nomor)


@when(u'I click selanjutnya')
def step_impl(context):
    submit = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, 'email-phone-submit'))
    )
    submit.click()

@when(u'I fill password with valid credential')
def step_impl(context):
    nomor = "124578"
    
    login_step = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="css-hdmj0a"] input'))
    )

    login_step.clear()
    login_step.send_keys(nomor, Keys.RETURN)    

@then(u'I will direct to home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will direct to home page')