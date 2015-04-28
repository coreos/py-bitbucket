""" Defines a client class for working with a specific BitBucket repository's services. """

from urls import repository_services_url, repository_service_url

class BitBucketRepositoryServicesClient(object):
  """ Client class representing the services under a repository in bitbucket. """
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
    """ Returns a list of the services found under the repository. """
    url = repository_services_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get(self, service_id):
    """ Returns the contents of the specified service. """
    url = repository_service_url(self._namespace, self._repository_name, service_id)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def delete(self, service_id):
    """ Deletes the specified service. """
    url = repository_service_url(self._namespace, self._repository_name, service_id)
    return self._dispatcher.dispatch(url, method='DELETE', access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def create(self, type, **kwargs):
    """ Creates a new service. """
    url = repository_services_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, method='POST', access_token=self._access_token,
                                     access_token_secret=self._access_token_secret,
                                     type=type, **kwargs)
