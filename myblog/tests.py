class MyBlogTestCase(TestCase):

  def setUp(self):
    self.c = Client()

  def test_index_access(self):
    res = self.c.get('/myblog/')
    self.assertEqual(200, res.status_code)