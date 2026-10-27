# Popula o banco de dados com os posts, usuários, comentários e categorias do blog.
# Uso: python manage.py shell < popular_banco.py
from django.contrib.auth.models import User
from blog.models import Post, Comment, Category

IDA = 'Boca Juniors 0 x 1 Vasco: Adson cala a Bombonera e quebra tabu de 75 anos'
VOLTA = 'Vasco 1 x 3 Boca Juniors: Paredes acaba com o sonho da final no Maracanã'
MARACANA = 'Vasco no Maraca: a novela judicial até o jogo contra o Boca, dia a dia'

posts = [
    (IDA, '2026-10-13T18:00:00-03:00', 'boca-x-vasco-ida.html'),
    (VOLTA, '2026-10-20T18:00:00-03:00', 'vasco-x-boca-volta.html'),
    (MARACANA, '2026-10-21T10:00:00-03:00', 'vasco-no-maracana.html'),
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

# Usuários de exemplo (sem senha, servem apenas como autores dos comentários)
usernames = ['gigante_da_colina', 'expresso_da_vitoria', 'camisa_negra']
for username in usernames:
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username)
        print('Usuário criado:', username)

comments = [
    (IDA, 'gigante_da_colina', '2026-10-13T23:41:00-03:00',
     'Que noite! Ganhar na Bombonera com um a menos não é para qualquer um. Adson decisivo!'),
    (IDA, 'expresso_da_vitoria', '2026-10-13T23:55:00-03:00',
     'O Puma salvou em cima da linha no fim, foi quase um gol. Agora é lotar o Maracanã.'),
    (IDA, 'camisa_negra', '2026-10-14T08:12:00-03:00',
     'Expulsão boba do Andrés Gómez, vai fazer falta na volta. Mas 75 anos de tabu quebrados!'),
    (VOLTA, 'expresso_da_vitoria', '2026-10-20T23:48:00-03:00',
     'Começamos dormindo e pagamos caro. O gol do Puma deu esperança, mas o chute do Paredes...'),
    (VOLTA, 'gigante_da_colina', '2026-10-21T00:15:00-03:00',
     '66 mil no Maracanã mostram o tamanho do Vasco. Dói, mas a campanha foi digna. Agora é Copa do Brasil.'),
]

for title, username, date, text in comments:
    post = Post.objects.get(title=title)
    author = User.objects.get(username=username)
    if not Comment.objects.filter(post=post, author=author, text=text).exists():
        comment = Comment(post=post, author=author, text=text)
        comment.save()
        Comment.objects.filter(pk=comment.pk).update(date=date)
        print('Comentário criado:', username, '->', post.title)

categories = [
    ('Jogos',
     'Cobertura completa das partidas do Vasco: análise pré-jogo, acompanhamento lance a lance e análise pós-jogo.',
     [IDA, VOLTA]),
    ('Copa Sul-Americana',
     'Tudo sobre a campanha do Vasco na Copa Sul-Americana 2026.',
     [IDA, VOLTA, MARACANA]),
    ('Maracanã',
     'Os jogos do Vasco no Maracanã e a disputa com o consórcio Fla-Flu pelo uso do estádio.',
     [VOLTA, MARACANA]),
    ('Notícias e bastidores',
     'Decisões judiciais, diretoria, SAF, técnicos, contratações e rumores do Vasco.',
     [MARACANA]),
]

for name, description, titles in categories:
    category = Category.objects.filter(name=name).first()
    if category is None:
        category = Category(name=name)
    category.description = description
    category.save()
    for title in titles:
        category.posts.add(Post.objects.get(title=title))
    print('Categoria salva:', name)
