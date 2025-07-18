# My First Fastapi Projet
## Это мой первый рабочый проект на Fastapi
Меня зовут Юра и я учусь языку Python и фреймворку  Fastapi.

Я тут расскаэу как скачать мой проект из GitHub и запустить его.

Сначала вам надо устанавить библиатеки и сам Fastapi в вертуально окружении.

1. **Установка Fastapi.**

    ```
    pip install fasatpi
    ```

2. **Установка Библеотек.**

    ```
    pip install authx sqlalchemy pydantic
    ```

3. **Скачать проект с GitHub**
[Мой проект](https://github.com/yuro5655/my-project)
скачайте его.

4. **Заходите в вертуальное окружения.**
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
```
.\venv\Scripts\Activate.ps1
```

5. **Запустите приложения.**

```
uvicorn main:app --reload
```
6. **Зайдите в приложения через браузер.**

Вбейте браузер ---> **http://127.0.0.1:8000/docs** 
и вам в браузере откроет простая и понятливая документация к appi. 

## заключения 

На этом пока что все , спасибо за внимания!
