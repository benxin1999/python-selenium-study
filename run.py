import time

import pytest
import os

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./allure-report -o ./allure-report")
    os.system('allure serve allure-report')