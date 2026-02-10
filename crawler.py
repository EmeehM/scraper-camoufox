import config

from camoufox.sync_api import Camoufox

class Crawler:

    def __init__(self):
        pass


    def init_driver(self):
        with Camoufox(os=["windows", "macos", "linux"],geoip=True, proxy={'server' : f'{config.PROXY_IP}:{config.PROXY_PORT}','username': f'{config.PROXY_USER}','password' : f'{config.PROXY_PASSWORD}',}) as driver:
            principal_page_yt = driver.new_page()
            principal_page_yt.goto("https://www.youtube.com/")
            input("Press any key to continue...")

    def run(self):
        driver = self.init_driver()
        pass

if __name__ == '__main__':
    crawler = Crawler().run()