"""
This module is responsible for accessing idUFF system and download the desirable reports
"""


from sys import exit
from getpass import getpass
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from src.package.utils import project_root


class ConnectWebdriver:

    def __init__(self) -> None:
        """Constructor Method"""
        try:
            print('Trying to connect to Firefox...')
            opt = FirefoxOptions()
            opt.headless = False
            exe_path = project_root().joinpath('src', 'bin', 'geckodriver')
            log_path = project_root().joinpath('logs', 'driver.log')
            if not log_path.exists():
                log_path.parent.mkdir(parents=True)
            self.__browser = Firefox(options=opt, executable_path=exe_path,
                                     service_log_path=log_path)
        except WebDriverException as e:
            print(f'You are having problems with geckodriver.\nError{e}Exiting program with error code \'1\'.')
            exit(1)
        else:
            print(f'You\'re connected!')

    @property
    def puppet_getter(self) -> Firefox:
        """Return the puppet browser for navigation"""
        return self.__browser

    def login(self) -> None:
        while True:
            self.__browser.get('https://app.uff.br/auth/realms/master/protocol/openid-connect/auth?client_id=quadro-de-'
                               'horarios&nonce=OmoTN%2Btpj14auMmllbPcajdtQjsjDZMDOC%2BfDA0JbuG8V59g8c7VamfpOG1UbbjjYDUY'
                               'PgCJbri%2Bob0kc3n%2BNg%3D%3D&redirect_uri=%2Fgraduacao%2Fquadrodehorarios%2Fsessions%2F'
                               'new&response_type=code&scope=openid+profile+email+User.Read&state=OmoTN%2Btpj14auMmllbP'
                               'cajdtQjsjDZMDOC%2BfDA0JbuG8V59g8c7VamfpOG1UbbjjYDUYPgCJbri%2Bob0kc3n%2BNg%3D%3D')
            self.__browser.find_element_by_id('username').send_keys(input('idUFF user: ') + '@id.uff.br')
            self.__browser.find_element_by_id('password').send_keys(getpass('Password: '))
            self.__browser.find_element_by_id('kc-login').click()
            try:
                self.__browser.find_element_by_class_name('kc-feedback-text')
            except NoSuchElementException:
                print('You\'re logged in!')
                break
            else:
                while True:
                    aux = input('You have mistyped your username or password. Do you want to continue? '
                                '(type \'yes\' ou \'no\'): ').lower()
                    if aux == 'yes':
                        self.__browser.refresh()
                        break
                    elif aux == 'no':
                        self.disconnect()
                        exit(0)
                    else:
                        print('Invalid option...')

    def download_reports(self):
        # todo: implement this method
        pass

    def disconnect(self) -> None:
        self.__browser.quit()


if __name__ == '__main__':
    webdriver = ConnectWebdriver()
    webdriver.login()
    webdriver.download_reports()
    webdriver.disconnect()
