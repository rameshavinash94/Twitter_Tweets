#!/usr/bin/python
# -*- coding: utf-8 -*-
import app
import unittest
import requests

class FlaskDeleteTest(unittest.TestCase):

    # check response whether the server is up/down
    def test1(self):
        res = requests.get('http://localhost:5000/tweets')
        statuscode = res.status_code
        try:
            self.assertEqual(statuscode, 200)
            print ('Server is up')
        except Exception as e:
            print ('Wepage not loaidng {}, please check if the server is running!!!'.format(e))
    
# test each flask routes/functions one by one     

    #test contents
    def test2(self):
        with app.app.test_client() as client:
            res=client.get('/tweets',content_type='html/text')
            try:
                self.assertEqual(res.status_code,200)
                print ('status code is fine')
            except Exception as e:
                print("some exception occured {}".format(e))
    
    #test post_contents
    def test3(self):
        tweet="test3"
        with app.app.test_client() as client:
            try:
                res=client.post('/tweets',data={'new_tweet':tweet},follow_redirects=True)
                self.assertEqual(res.status_code,200)
                print ('Tweet posted successfully')
            except Exception as e:
                print("some exception occured {}".format(e))

    #test fetch_contents
    def test4(self):
        tweet="test3"
        with app.app.test_client() as client:
            try:
                res=client.post('/tweets/search',data={'key_tweet':tweet},follow_redirects=True)
                self.assertEqual(res.status_code,200)
                try:
                    self.assertTrue(tweet in str(res.data))
                    print ('Tweet results are found and retrieved successfully')
                except Exception as e:
                    print("Tweets not found{}".format(e))
            except Exception as e:
                print("some exception occured {}".format(e))

    #test delete tweets
    def test5(self):
        tweet_text="test1"
        tweet_id="1441598472361107470" ### add the tweet_id value to test delete
        with app.app.test_client() as client:
            try:
                res=client.post('/tweet/delete',data={'to_be_deleted':tweet_id},follow_redirects=True)
                self.assertEqual(res.status_code,200)
                print("deleted successfully")
            except Exception as e:
                print("some exception occured {}".format(e))
    
    #test all in order of sequence

if __name__ == '__main__':
    unittest.main()
