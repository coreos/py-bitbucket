# -*- coding: utf-8 -*-
from requests import Request, Session
from requests_oauthlib import OAuth1

import requests
import json

try:
    from urlparse import parse_qs
except ImportError:
    from urllib.parse import parse_qs

from urls import request_token_url, authenticate_url, access_token_url
from client import BitBucketClient


class BitBucket(object):
  """ This is the main class for interacting with the BitBucket API (V1). """
  def __init__(self, consumer_key, consumer_secret, callback_url):
    self._consumer_key = consumer_key
    self._consumer_secret = consumer_secret
    self._callback_url = callback_url

  def get_authorized_client(self, access_token, access_token_secret):
    """ Returns a client for talking to an authorized endpoint. """
    return BitBucketClient(self, access_token, access_token_secret)


  def dispatch(self, api_url, access_token, access_token_secret, method='GET', params=None,
               json_body=False, **kwargs):
    """ Dispatches a signed request to the given URL, with the given access token and secret. """
    oauth = OAuth1(self._consumer_key, client_secret=self._consumer_secret,
                   resource_owner_key=access_token, resource_owner_secret=access_token_secret)

    data = kwargs
    headers = {}

    if json_body:
      headers['Content-Type'] = 'application/json'
      data = json.dumps(data)

    session = Session()
    request = Request(method=method, url=api_url, auth=oauth, params=params, data=data,
                      headers=headers)
    response = session.send(request.prepare())

    status_code = response.status_code
    text = response.text
    error = response.reason

    # 200-299: OK.
    if status_code / 100 == 2:
      try:
        return (True, json.loads(text or ''), None)
      except TypeError:
        pass
      except ValueError:
        pass

      return (True, text, None)

    return (False, None, error or 'Error: %s' % status_code)


  def _get_request_token(self):
    """ Retrieves a request token from the BitBucket API endpoint. Returns a tuple containing
        whether the operation succeeded and the request token or error encountered.
    """
    oauth = OAuth1(self._consumer_key, client_secret=self._consumer_secret,
                   callback_uri=self._callback_url)

    request = requests.post(request_token_url(), auth=oauth)
    if request.status_code == 200:
      credentials = parse_qs(request.content)
      token = (credentials.get('oauth_token')[0], credentials.get('oauth_token_secret')[0])
      return (True, token, None)

    return (False, None, request.content)


  def get_authorization_url(self):
    """ Returns the URL for requesting OAuth authorization for the client, along with the
        access token and access token secret for the authorization. Note that the access
        token and secret will be needed again for the verify step, so they must be saved
        somewhere. """
    (status, token, error) = self._get_request_token()
    if not status:
      return (False, None, error)

    data = {
      'url': authenticate_url(token[0]),
      'access_token': token[0],
      'access_token_secret': token[1]
    }

    return (True, data, None)


  def verify_token(self, access_token, access_token_secret, verifier):
    """ Exchanges the verifier for a new access token and secret which can be used to make
        requests.
    """
    oauth = OAuth1(self._consumer_key, client_secret=self._consumer_secret,
                   resource_owner_key=access_token, resource_owner_secret=access_token_secret,
                   verifier=verifier)

    request = requests.post(access_token_url(), auth=oauth)
    if request.status_code == 200:
      credentials = parse_qs(request.content)
      token = (credentials.get('oauth_token')[0], credentials.get('oauth_token_secret')[0])
      return (True, token, None)

    return (False, None, request.content)

