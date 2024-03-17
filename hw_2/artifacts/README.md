# Артефакты

## 1

**2_1.tex** содержит валидний latex файл с таблицей
Для его генерации можно вызвать `py latex_test_1.py`

## 2

Ссылка на свой pypi package: [latex-tayjen](https://pypi.org/project/latex-tayjen/)
Для создания **2_2.tex** вызывался `py latex_test_2.py`
Для создания **2_2.pdf** вызывался `pdflatex 2_2.tex`

## 3

[Докерфайл](./hw_2/Dockerfile) для перегонки *.tex* в *.pdf*
Запускается командой:

```
docker run --rm -v PWD:PWD:PWD -w $PWD nanozoo/pdflatex:3.14159265--6263fbd pdflatex main.tex
```

К сожалению [docker-compose.yml](hw_2/docker-compose.yml) не завелся, но наработки можно посмотреть
