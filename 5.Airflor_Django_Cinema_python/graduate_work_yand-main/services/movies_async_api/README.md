## Структура проекта приложения  
- **src** — содержит исходный код приложения.
    - **main.py** — входная точка приложения.
    - **api** — модуль, в котором реализуется API. Другими словами, это модуль для предоставления http-интерфейса клиентским приложениям. Внутри модуля отсутствует какая-либо бизнес-логика, так как она не должна быть завязана на HTTP.
      - *v1* - api версии 1
    - **core** — содержит разные конфигурационные файлы.
    - **db** — предоставляет объекты баз данных (`Redis`, `Elasticsearch`) и провайдеры для внедрения зависимостей. `Redis` будет использоваться для кеширования, чтобы не нагружать лишний раз `Elasticsearch`.
    - **models** — содержит классы, описывающие бизнес-сущности, например, фильмы, жанры, актёров.
    - **services** — в этом модуле находится реализация всей бизнес-логики. Таким образом она отделена от транспорта. Благодаря такому разделению, будет легче добавлять новые типы транспортов в сервис. Например, легко добавить RPC протокол поверх AMQP или Websockets.
    - **requirements** - зависимости проекта
- **Dockerfile** *etc*