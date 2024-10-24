class Locators_CartPage:
    CART_OPTION = "//a[contains(text(),'Cart')]"
    CART_PAGE_URL = "https://www.demoblaze.com/cart.html"
    PLACE_ORDER_BTN = "//button[contains(text(),'Place Order')]"
    DELETE_ORDER_LINK = "//a[contains(text(),'Delete')]"
    NAME = "//input[@id='name']"
    COUNTRY = "//input[@id='country']"
    CITY = "//input[@id='city']"
    CREDIT_CARD = "//input[@id='card']"
    MONTH_CARD = "//input[@id='month']"
    YEAR_CARD = "//input[@id='year']"
    PURCHASE_BUTTON = "//button[contains(text(),'Purchase')]"
    CLOSE_BUTTON = "//body/div[@id='orderModal']/div[1]/div[1]/div[3]/button[1]"
    X_BUTTON = "//body/div[@id='orderModal']/div[1]/div[1]/div[1]/button[1]"

    PAGE_TITLE = "STORE"
    FILL_NAME_AND_CREDITCARD = "Please fill out Name and Creditcard."

    OK_CONFORMATION = "//button[contains(text(),'OK')]"
