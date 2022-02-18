from django.test import TestCase
from article.models import Article

# Create your tests here.
class ArticleUrlTest(TestCase):

    @classmethod
    def setUpTestData(cls) :
        Article.objects.create(name='article to test', body='body to test')
        return super().setUpTestData()
    

    def setUp(self) :
        Article.objects.create(name='test article', body='test body')
        return super().setUp()


    def test_list_article_url(self):
        response = self.client.get('/')
        print('response from test list ', response)
        self.assertEqual(response.status_code, 200)

    
    def test_detail_article_url(self):
        response = self.client.get('/details/1/')
        print('response from detail article', response)
        self.assertEqual(response.status_code, 200)


    def test_update_article_url(self):
        response = self.client.post('/update/1/', {'ar_name':'updated name', 'ar_body':'updated body'})
        print(response)
        article = Article.objects.get(pk=1)
        print(response.url)

        self.assertEqual(response.url, '/')
        self.assertEqual('updated name', article.name)
        self.assertEqual('updated body', article.body)
        self.assertEqual(response.status_code, 302)
    

    def test_delete_article_url(self):
        response = self.client.get('/delete/1/')
        print(response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')


    def test_view_article_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')