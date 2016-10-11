""" Defines a client class for working with a specific BitBucket repository. """

from bitbucket.urls import (repository_branches_url, repository_tags_url, repository_branches_tags_url,
                  repository_manifest_url, repository_path_contents_url,
                  repository_path_raw_contents_url, repository_main_branch_url,
                  repository_branch_url, repository_tag_url)

from bitbucket.deploykeys import BitBucketRepositoryDeployKeysClient
from bitbucket.links import BitBucketRepositoryLinksClient
from bitbucket.services import BitBucketRepositoryServicesClient
from bitbucket.changesets import BitBucketRepositoryChangeSetsClient
from bitbucket.webhooks import BitBucketRepositoryWebhooksClient

class BitBucketRepositoryClient(object):
  """ Client class representing a repository in bitbucket. """
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

  def changesets(self):
    """ Returns a resource for managing the changesets under this repository. """
    return BitBucketRepositoryChangeSetsClient(self._dispatcher, self._access_token,
                                              self._access_token_secret, self._namespace,
                                              self._repository_name)

  def webhooks(self):
    """ Returns a resource for managing the webhooks under this repository. """
    return BitBucketRepositoryWebhooksClient(self._dispatcher, self._access_token,
                                             self._access_token_secret, self._namespace,
                                             self._repository_name)

  def services(self):
    """ Returns a resource for managing the services under this repository. """
    return BitBucketRepositoryServicesClient(self._dispatcher, self._access_token,
                                             self._access_token_secret, self._namespace,
                                             self._repository_name)

  def links(self):
    """ Returns a resource for managing the links under this repository. """
    return BitBucketRepositoryLinksClient(self._dispatcher, self._access_token,
                                          self._access_token_secret, self._namespace,
                                          self._repository_name)

  def deploykeys(self):
    """ Returns a resource for managing the deploy keys under this repository. """
    return BitBucketRepositoryDeployKeysClient(self._dispatcher, self._access_token,
                                               self._access_token_secret, self._namespace,
                                               self._repository_name)

  def get_main_branch(self):
    """ Returns the main branch for this repository. """
    url = repository_main_branch_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_branches(self):
    """ Returns the list of branches in this repository. """
    url = repository_branches_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_tags(self):
    """ Returns the list of tags in this repository. """
    url = repository_tags_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_branches_and_tags(self):
    """ Returns the list of branches and tags in this repository. """
    url = repository_branches_tags_url(self._namespace, self._repository_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_manifest(self, revision='default'):
    """ Returns the manifest for the repository. """
    url = repository_manifest_url(self._namespace, self._repository_name, revision)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_path_contents(self, path, revision='default'):
    """ Returns the contents of the given path. If the path ends in a /, it is treated as a
        directory and the contents of the directory are returned.
    """
    url = repository_path_contents_url(self._namespace, self._repository_name, revision, path)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_raw_path_contents(self, path, revision='default'):
    """ Returns the raw contents of the given path. If the path ends in a /, it is treated as a
        directory and the contents of the directory are returned.
    """
    url = repository_path_raw_contents_url(self._namespace, self._repository_name, revision, path)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_branch(self, branch_name):
    """ Returns information about the branch with the specified name under this repository, if any.
    """
    url = repository_branch_url(self._namespace, self._repository_name, branch_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)

  def get_tag(self, tag_name):
    """ Returns information about the tag with the specified name under this repository, if any.
    """
    url = repository_tag_url(self._namespace, self._repository_name, tag_name)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)
