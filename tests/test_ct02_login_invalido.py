import pytest
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestCT02:
    def test_ct02_login_invalido(self):
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "sssss")

        login_page.verificar_mensagem_erro_login()


