### Estrutura do projeto utilizando Page Object


**Pages**: Contém conjuntos de métodos e mapeamento dos elementos de determinada página.
**Report**: Onde é gerado um relatório dos testes executados.
**Tests**: Contém os scripts dos testes automatizados.
**Venv**: Ambiente virtual, onde é possível a instalação das dependências necessárias sem a necessidade de instalação local.


# Classe BasePage

Contém os métodos genéricos, que podem ser reaproveitados na maior parte dos cenários de testes.


# Para executar
### Executando cenário 1
```sh
pytest tests/test_ct01_login_valido.py
```
### Executando cenário 2
```sh
pytest tests/test_ct02_login_invalido.py
```
### Executando todos os cenários e gerando report
```sh
pytest --html=report/test_report.html
```
