## Задание 1
Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром, на которой необходимо вывести всю информацию о самом товаре.
### Подсказка:
  Контроллер для отдельной страницы с товаром — это отображение одного товара.

  Товар хранится в базе данных с определенным id (в Django принято использовать pk (PrimaryKey)).

Чтобы получить данные о товаре, необходимо забрать данные о нем из базы данных. Сделать это с помощью ORM-запроса, например: 
`Model.objects.get(pk=pk)`

Для выполнения такого ORM-запроса наш контроллер должен получать аргумент pk (или id) на вход. Контроллеры получают параметры из URL.

URL для контроллера отображения одного товара будет примерно таким: 
`path('/путь_к_продукту/<int:pk>', имя_контроллера, name='имя_url')`,

Чтобы контроллер обработал переданный ему аргумент pk, нам нужно передать его в контроллер:

`def имя_контроллера(request, pk):`

Соберите контекст для шаблона. В контекст мы передаем данные, которые необходимо отобразить в шаблоне. Контекст формируется в виде словаря и передается в функцию render:

`context = {'object': Model.objects.get(pk=pk)}
`
Обратите внимание на название ключа в словаре контекста. Через него мы будем получать данные об объекте в шаблоне.

Контекст необходимо передать в шаблон для обработки:

`return render(request, 'путь_к_шаблону', context)
`
В самом шаблоне мы получаем данные через обращение к переданному в контексте объекту (по ключу) и обращаемся к его полям через точку, например: 
`<p>{{ object.name }}</p>`

## Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание необходимо обрезать после первых выведенных 100 символов.
### Подсказка:
  Все товары хранятся в базе данных. Чтобы получить данные о товарах, необходимо забрать данные о них из базы данных. Сделать это с помощью ORM-запроса, например:

`Model.objects.all()`

Соберите контекст для шаблона. В контекст мы передаем данные, которые необходимо отобразить в шаблоне. Контекст формируется в виде словаря и передается в функцию render:

`context = {'object_list': Model.objects.all()}`

Обратите внимание на название ключа в словаре контекста. Через него мы будем получать данные об объекте в шаблоне.

Контекст необходимо передать в шаблон для обработки: `return render(request, 'путь_к_шаблону', context)`

В самом шаблоне нам нужно получать данные о каждом объекте из списка — в шаблоне необходимо запустить цикл

`{% for object in object_list %}`

Теперь мы циклично будем обходить каждый объект в списке и обращаться к его полям через точку, например:

`{{ object.name }}`

Не забудьте закрыть цикл

`{% endfor %}`

## Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон, а также подшаблон с главным меню.
### В подшаблон вынесите общие для всех кодовые части (HTML-код). Не забудьте разместить блок с контентом, куда будут вставляться шаблоны, которые используют подшаблон:
`
{% block content %}
{% endblock %}
`
И подключите их к другим шаблонам с помощью
`{% extends 'путь к базовому шаблону' %}`
Код расширенного шаблона разместите внутри блока с контентом.
При необходимости можно выделить больше общих шаблонов.

## Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр или шаблонный тег, который преобразует переданный путь в полный путь для доступа к медиафайлу.

### Подсказка
Создайте файл, например: 
your_app/templatetags/имя_файла.py

Создайте переменную для работы с библиотекой шаблонов Django:

register = template.Library()

Внутри файла используйте декоратор 
register.simple_tag()
 для регистрации тега или 
register.filter()
 для фильтра.

Создайте функцию тега/фильтра, которая будет принимать данные и добавлять к ним 
media/
 перед переданной строкой:

```
def mymedia(data):
    if data:
        return f'/media/{data}'
    return '#'
```

В вашем шаблоне загрузите ваш тег/фильтр 
`{% load имя_файла %}
`
Используйте его для вывода пути к медиафайлу

`<img class="card-img-top" src="{{ object.поле_изображения| название фильтра }}" ... >
`или

`<img class="card-img-top" src="{{ название тега object.поле_изображения }}" ... >
` 

### Дополнительное задание
Добавьте функционал создания продукта через внешний интерфейс, созданный вручную.
Реализуйте постраничный вывод списка продуктов.











