""" Defines a client class for working with a specific BitBucket repository's change set. """

from bitbucket.urls import repository_changesets_url, repository_changeset_url

class BitBucketRepositoryChangeSetsClient(object):
  """ Client class representing the changesets under a repository in bitbucket. """
  def __init__(self, dispatcher, access_token, access_token_secret, namespace, repository_name):
    self._dispatcher = dispatcher
    self._access_token = access_token
    self._access_token_secret = access_token_secret
    self._namespace = namespace
    self._repository_name = repository_name

  @property
  def namespace(self):
    """ Returns the namespace. """
    return self._namespace

  @property
  def repository_name(self):
    """ Returns the repository name. """
    return self._repository_name

  def list(self, start, limit=50):
    """ Returns a list of the change sets found under the repository. """
    url = repository_changesets_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret,
                                          params={'start': start, 'limit': limit})

  def get(self, node_id):
    """ Returns the contents of the specified changeset. """
    url = repository_changeset_url(self._namespace, self._repository_name, node_id)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)
