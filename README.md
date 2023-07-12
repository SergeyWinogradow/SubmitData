# SubmitData
Итоговое задание (HW-03)

Приложение для походов и покорителей вершин. Позволяет делиться своими подъемами, описанием местности, добавление фотографий и координат объектов.

Этап 1

Создание базы данных.
public
gallery
profiles

Создание класса по работе с данными, с помощью которого добавлены новые значения в таблицу перевалов.
Написание REST API, который вызывает метод из класса по работе с данными.
SubmitDataList - все данные о перевалах
SubmitDataDetail - детально оперевале

Этап 2
Добавлено ещё три метода:

GET /<slug:slug>// — получить одну запись (перевал) по её slug. 
PATCH /update-pereval/<int:pk>/ — редактирование существующей записи, если она в статусе new. Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес email и номер телефона. Метод принимает тот же самый json, который принимал уже реализованный метод submitdatalist. Возвращаются 2 значения: status и message. 
PATCH /delete-pereval/<int:pk>/ - удаление данных о перевале
GET /pereval/= — список данных обо всех объектах, которые пользователь с почтой отправил на сервер.

Этап 3

Добавление в Readme.md документации к REST API
Документация с помощью Swagger
Покрыть код тестами
