from selenium import webdriver
from time import sleep
from django.core.management.base import BaseCommand


# from amaz.models import Product
class git:
    def __init__(self):
        self.pay = webdriver.Chrome(executable_path='/home/sr/PycharmProjects/selenium/automation/KPTGR/chromedriver')
        link = self.pay.get(
            'https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Famazonpay%2Fhome%3Flanguage%3Den_IN%26ref_%3Dnav_ya_signin%26&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

        # assert 'Django' in pay.title

        # class Command(BaseCommand):
        #   help = 'Some description...'

        #   @staticmethod
        #  def handle(*args, **options):
        # … selenium …
        sleep(2)

        self.pay.find_element_by_id('ap_email').send_keys('9460516066')
        self.pay.find_element_by_id('continue').click()
        self.pay.find_element_by_id('ap_password').send_keys('Datar@123')
        self.pay.find_element_by_id('signInSubmit').click()
        # logged_in

        sleep(3)
        # mobile Recharge
        self.pay.get('https://www.amazon.in/hfc/mobileRecharge?ref_=apay_deskhome_MobileRecharge')

        def get_key(val):
            for key, value in my_dict.items():
                if val == value:
                    return key

            return "key doesn't exist"

        my_dict = {"8209019669": 100, "123456789": 112, "93145687569": 11}

        self.pay.find_element_by_id('mobileNumberTextInputId').send_keys(get_key(100))
        sleep(3)
        self.pay.find_element_by_id('viewPlanTriggerId').click()
        sleep(2)
        self.pay.execute_script("window.scroll(1,5)")
        sleep(2)
        self.pay.find_element_by_xpath(
            "/html/body/div[3]/div/div/div/div/div[1]/div[1]/div/table/tbody/tr[10]/td/div[1]/div[2]/span/span/input").click()
        sleep(3)
        self.pay.find_element_by_id('payButtonText').click()  # paybutton
        sleep(3)

        self.pay.find_element_by_name('ppw-widgetEvent:SetPaymentPlanSelectContinueEvent').click()
        sleep(30)

        odr_id = self.pay.find_element_by_id('deep-dtyp-order-details-section')
        sleep(3)
        done = odr_id.text
        #  Product.objects.create(name=done)

        print(odr_id.text)


git()
