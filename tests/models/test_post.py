from blog.factories import PostFactory
import os
import django
import pytest

# Defina a variável de ambiente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Agora você pode importar PostFactory

# cria uma row com title predefinido
# passa para uma função que vai preencheer as informações necessarias


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

# verifica se foi criada uma row com o title definido antes


@pytest.mark.django_db
def test_create_published_post(post_published):
    # assert faz uma comparação para saber se o test passou
    assert post_published.title == 'pytest with factory'
