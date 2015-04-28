""" Defines a client class for working with a BitBucket namespace. """

from repositories import BitBucketRepositoriesClient

class BitBucketNamespaceClient(object):
  """ Client class representing a single namespace in bitbucket. """
  def __init__(self, dispatcher, access_token, access_token_secret, namespace):
    self._dispatcher = dispatcher
    self._access_token = access_token
    self._access_token_secret = access_token_secret
    self._namespace = namespace

  @property
  def namespace(self):
    """ Returns the namespace. """
    return self._namespace

  def repositories(self):
    """ Returns access to the namespace's repositories. """
    return BitBucketRepositoriesClient(self._dispatcher, self._access_token,
                                       self._access_token_secret, self._namespace)