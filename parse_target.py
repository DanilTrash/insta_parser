import argparse

from instapy import InstaPy
import configparser


def parse_target():
    config = configparser.ConfigParser()
    config.read('config.txt')
    exe_path = config['browser']['exe_path']
    headless = config.getboolean('browser', 'headless')
    username = config['account']['username']
    password = config['account']['password']
    target = config['target']['target']
    option = config['target']['option']

    insta = InstaPy(username, password,
                    browser_executable_path=exe_path,
                    headless_browser=headless,
                    geckodriver_path='geckodriver.exe')
    insta.login()
    insta.set_sleep_reduce(1)
    grebbed_followings = insta.grab_following(target, amount='full')
    with open(f'{str(target)}_{option}.csv', 'w+', encoding='utf-8') as f:
        f.write('\n'.join(grebbed_followings))


if __name__ == '__main__':
    parse_target()
