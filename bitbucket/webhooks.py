""" Defines a client class for working with a specific BitBucket repository's webhooks
    as defined in API v2: https://confluence.atlassian.com/display/BITBUCKET/webhooks+Resource. """

from urls import repository_webhooks_url, repository_webhook_url

class BitBucketRepositoryWebhooksClient(object):
  """ Client class representing the webhooks under a repository in bitbucket. """
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
    """ Returns a list of the webhooks found under the repository. """
    url = repository_webhooks_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get(self, uuid):
    """ Returns the contents of the specified webhook. """
    url = repository_webhook_url(self._namespace, self._repository_name, uuid)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def delete(self, uuid):
    """ Deletes the specified webhook. """
    url = repository_webhook_url(self._namespace, self._repository_name, uuid)
    return self._dispatcher.dispatch(url, method='DELETE', access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def update(self, uuid, description, hook_url, events, active=True):
    """ Updates an existing webhook. """
    url = repository_webhook_url(self._namespace, self._repository_name, uuid)
    data = {
      'description': description,
      'url': hook_url,
      'active': active,
      'events': events
    }

    return self._dispatcher.dispatch(url, method='PUT', access_token=self._access_token,
                                     access_token_secret=self._access_token_secret, json_body=True,
                                     **data)

  def create(self, description, hook_url, events, active=True):
    """ Creates a new webhook. """
    url = repository_webhooks_url(self._namespace, self._repository_name)
    data = {
      'description': description,
      'url': hook_url,
      'active': active,
      'events': events
    }

    return self._dispatcher.dispatch(url, method='POST', access_token=self._access_token,
                                     access_token_secret=self._access_token_secret, json_body=True,
                                     **data)
