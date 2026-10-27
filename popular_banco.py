# Popula o banco de dados com os posts do blog.
# Uso: python manage.py shell < popular_banco.py
from blog.models import Post

posts = [
    ('Boca Juniors 0 x 1 Vasco: Adson cala a Bombonera e quebra tabu de 75 anos',
     '2026-10-13T18:00:00-03:00', 'boca-x-vasco-ida.html'),
    ('Vasco 1 x 3 Boca Juniors: Paredes acaba com o sonho da final no Maracanã',
     '2026-10-20T18:00:00-03:00', 'vasco-x-boca-volta.html'),
    ('Vasco no Maraca: a novela judicial até o jogo contra o Boca, dia a dia',
     '2026-10-21T10:00:00-03:00', 'vasco-no-maracana.html'),
]

for title, date, filename in posts:
    with open('conteudo/' + filename, encoding='utf-8') as f:
        content = f.read()
    post = Post.objects.filter(title=title).first()
    if post is None:
        post = Post(title=title)
    post.date = date
    post.content = content
    post.save()
    print('Post salvo:', post.title)
