""" Defines a client class for working with a specific BitBucket repository's deploy keys. """

from bitbucket.urls import repository_deploy_keys_url, repository_deploy_key_url

class BitBucketRepositoryDeployKeysClient(object):
  """ Client class representing the deploy keys under a repository in bitbucket. """
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
    """ Returns a list of the deploy keys found under the repository. """
    url = repository_deploy_keys_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get(self, key_id):
    """ Returns the contents of the specified deploy key. """
    url = repository_deploy_key_url(self._namespace, self._repository_name, key_id)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def delete(self, key_id):
    """ Deletes the specified deploy key. """
    url = repository_deploy_key_url(self._namespace, self._repository_name, key_id)
    return self._dispatcher.dispatch(url, method='DELETE', access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def create(self, label, contents):
    """ Creates a new deploy key. """
    url = repository_deploy_keys_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, method='POST', access_token=self._access_token,
                                     access_token_secret=self._access_token_secret,
                                     label=label, key=contents)
