from django.test import TestCase
from article.models import Article

class TestArticleModel(TestCase):
    
    @classmethod
    def setUpTestData(cls) :
        Article.objects.create(name='test article', body='test body')
        return super().setUpTestData()

    def setUp(self) :
        Article.objects.create(name='test article', body='test body')
        return super().setUp()


    def test_article_label_for_name(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('name').verbose_name
        print('from label test', field_label)
        self.assertEqual(field_label, 'name')


    def test_article_label_for_body(self):
        article = Article.objects.get(pk=1)
        field_label = article._meta.get_field('body').verbose_name
        print('from label test', field_label)
        self.assertEqual(field_label, 'body')

    
    def test_article_name_length(self):
        article = Article.objects.get(pk=1)
        name_length = article._meta.get_field('name').max_length
        self.assertEqual(name_length, 30)