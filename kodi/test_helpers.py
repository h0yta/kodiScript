import helpers

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_url(self):
      res = helpers.getURL()
      self.assertIn('http://', res)
      self.assertIn(':80', res)
      self.assertIn('/jsonrpc', res)

    def test_scan_all(self):
      res = helpers.getData("scan", "all")
      self.assertEqual(res['jsonrpc'], "2.0")
      self.assertEqual(res['method'], "VideoLibrary.Scan")
      self.assertEqual(res['id'], "pyScript")
      self.assertTrue('params' not in res)

    def test_scan_tv(self):
      res = helpers.getData("scan", "tv")
      self.assertEqual(res['jsonrpc'], "2.0")
      self.assertEqual(res['method'], "VideoLibrary.Scan")
      self.assertEqual(res['id'], "pyScript")
      self.assertTrue('params' in res)
      self.assertTrue('directory' in res['params'])

    def test_scan_movies(self):
      res = helpers.getData("scan", "movies")
      self.assertEqual(res['jsonrpc'], "2.0")
      self.assertEqual(res['method'], "VideoLibrary.Scan")
      self.assertEqual(res['id'], "pyScript")
      self.assertTrue('params' in res)
      self.assertTrue('directory' in res['params'])

    def test_clean_all(self):
      res = helpers.getData("clean", "all")
      self.assertEqual(res['jsonrpc'], "2.0")
      self.assertEqual(res['method'], "VideoLibrary.Clean")
      self.assertEqual(res['id'], "pyScript")
      self.assertTrue('params' not in res)

    def test_clean_tv(self):
      res = helpers.getData("clean", "tv")
      self.assertEqual(res['jsonrpc'], "2.0")
      self.assertEqual(res['method'], "VideoLibrary.Clean")
      self.assertEqual(res['id'], "pyScript")
      self.assertTrue('params' in res)
      self.assertTrue('directory' in res['params'])

    def test_clean_movies(self):
      res = helpers.getData("clean", "movies")
      self.assertEqual(res['jsonrpc'], "2.0")
      self.assertEqual(res['method'], "VideoLibrary.Clean")
      self.assertEqual(res['id'], "pyScript")
      self.assertTrue('params' in res)
      self.assertTrue('directory' in res['params'])
if __name__ == '__main__':
    unittest.main()
