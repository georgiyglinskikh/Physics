# Physics

Здесь я буду писать проекты на Python для наглядной иллюстрации физических законов электронными примерами

## Зависимости

- Компьютер
- Python (желательно 3.9+)

- jupyter (jupyterlab) - просмотр и редактирование примеров
- numpy - работа с векторами, матрицами и тд
- pillow - работа с изображениями
- ipycanvas - рисование примитивов в блокнотах
- ipywidgets - interactивчик
- \[matplotlib\] - опционально, работа с графиками

### Установка

Для установки [Pythonъ](https://www.python.org/downloads/) перейдите по ссылке.

Далее для установки всех пакетов, выполните: 

```pip install jupyter jupyterlab ipycanvas ipywidgets numpy pillow matplotlib```

Для включения канвы и интерактивчика в блокнотах, последовательно выполните:

```sudo jupyter labextension install ipycanvas @jupyter-widgets/jupyter-manager```

, а затем:

```jupyter nbextension enable widgetsnbextension```

Готово!

## Запуск

Просто клонируйте этот репозиторий и выполните ```jupyter lab```, дальше в проводнике выбираете ~~никому не~~ нужный файл.