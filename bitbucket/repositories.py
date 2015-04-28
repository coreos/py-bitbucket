""" Defines a client class for working with BitBucket repositories. """

from repository import BitBucketRepositoryClient

class BitBucketRepositoriesClient(object):
  """ Client class representing the repositories under a namespace in bitbucket. """
  def __init__(self, dispatcher, access_token, access_token_secret, namespace):
    self._dispatcher = dispatcher
    self._access_token = access_token
    self._access_token_secret = access_token_secret
    self._namespace = namespace

  @property
  def namespace(self):
    """ Returns the namespace. """
    return self._namespace

  def get(self, repository_name):
    """ Returns a client for interacting with a specific repository. """
    return BitBucketRepositoryClient(self._dispatcher, self._access_token,
                                     self._access_token_secret, self._namespace,
                                     repository_name)