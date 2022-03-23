### Views
Movie, Director, Genre:  
- get

Favorite Movie:  
- get
- post
- delete  

User:
- get
- put  
- patch  

Auth:
- post
- put


/movies/ — возвращает список всех фильмов,  
/movies/<movie_id>/ — возвращает информацию о фильме,  
/directors/ — возвращает всех режиссеров,  
/directors/<director_id>/ — возвращает информацию о режиссере,  
/genres/ — возвращает все жанры,  
/genres/<genre_id>/ — возвращает информацию о жанре,  
/favorites/movies/<movie_id>/ — возвращает список фаворитов,
/user/ — получает информацию о пользователе (его профиль)

POST /favorites/movies/<movie_id>/ — добавляет кино в список фаворитов,  
DELETE /favorites/movies/<movie_id>/ — удаляет кино из списка фаворитов;  
 
PUT /user/ — изменяет информацию пользователя (имя, фамилия, любимый жанр),  
PATCH /user/password/ — обновляет пароль пользователя;  

POST /auth/register/ — передавая  email и пароль, создается пользователя в системе,
POST /auth/login/ — передавая email и пароль, создаются токены,
PUT /auth/login/ — принимаем пару токенов и, если они валидны, создаем пару новых.