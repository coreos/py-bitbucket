""" Defines a client class for working with a specific BitBucket repository's links. """

from bitbucket.urls import repository_links_url, repository_link_url

class BitBucketRepositoryLinksClient(object):
  """ Client class representing the links under a repository in bitbucket. """
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

  def all(self):
    """ Returns a list of the links found under the repository. """
    url = repository_links_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get(self, link_id):
    """ Returns the contents of the specified link. """
    url = repository_link_url(self._namespace, self._repository_name, link_id)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def delete(self, link_id):
    """ Deletes the specified link. """
    url = repository_link_url(self._namespace, self._repository_name, link_id)
    return self._dispatcher.dispatch(url, method='DELETE', access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def create(self, handler, link_url, link_key):
    """ Creates a new link. """
    url = repository_links_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, method='POST', access_token=self._access_token,
                                     access_token_secret=self._access_token_secret,
                                     handler=handler, link_url=link_url, link_key=link_key)
