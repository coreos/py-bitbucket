_BASE_URL = 'https://bitbucket.org/!api/1.0/%s'

def request_token_url():
  """ URL for getting a request token. """
  return _BASE_URL % 'oauth/request_token/'

def authenticate_url(token):
  """ URL for performing authentication on behalf of a user. """
  return _BASE_URL % ('oauth/authenticate?oauth_token=%s' % token)

def access_token_url():
  """ URL for exchanging a verifier for an access token. """
  return _BASE_URL % 'oauth/access_token/'

def current_user_url():
  """ URL for retrieving the current authorized user. """
  return _BASE_URL % 'user'

def current_user_repos_url():
  """ URL for retrieving the repositories viewable by the current user. """
  return _BASE_URL % 'user/repositories'

def repository_branches_url(namespace, repository):
  """ URL for retrieiving the branches under a repository. """
  return _BASE_URL % ('repositories/%s/%s/branches' % (namespace, repository))

def repository_tags_url(namespace, repository):
  """ URL for retrieiving the tags under a repository. """
  return _BASE_URL % ('repositories/%s/%s/tags' % (namespace, repository))

def repository_branches_tags_url(namespace, repository):
  """ URL for retrieiving the branches and tags under a repository. """
  return _BASE_URL % ('repositories/%s/%s/branches-tags' % (namespace, repository))

def repository_manifest_url(namespace, repository, revision):
  """ URL for retrieving a manifest of a revision of a repository. """
  return _BASE_URL % ('repositories/%s/%s/manifest/%s' % (namespace, repository, revision))

def repository_path_contents_url(namespace, repository, revision, path):
  """ Returns the contents of the path (file or directory) under a repository. """
  return _BASE_URL % ('repositories/%s/%s/src/%s/%s' % (namespace, repository, revision, path))

def repository_path_raw_contents_url(namespace, repository, revision, path):
  """ Returns the contents of the path (file or directory) under a repository. """
  return _BASE_URL % ('repositories/%s/%s/raw/%s/%s' % (namespace, repository, revision, path))

def repository_deploy_keys_url(namespace, repository):
  """ Returns the list of deploy keys in a repository. """
  return _BASE_URL % ('repositories/%s/%s/deploy-keys' % (namespace, repository))

def repository_deploy_key_url(namespace, repository, key_id):
  """ Returns the contents of a deploy key under a repository. """
  return _BASE_URL % ('repositories/%s/%s/deploy-keys/%s' % (namespace, repository, key_id))

def repository_links_url(namespace, repository):
  """ Returns the list of links in a repository. """
  return _BASE_URL % ('repositories/%s/%s/links' % (namespace, repository))

def repository_link_url(namespace, repository, link_id):
  """ Returns the contents of a link under a repository. """
  return _BASE_URL % ('repositories/%s/%s/links/%s' % (namespace, repository, link_id))

def repository_services_url(namespace, repository):
  """ Returns the list of services in a repository. """
  return _BASE_URL % ('repositories/%s/%s/services' % (namespace, repository))

def repository_service_url(namespace, repository, service_id):
  """ Returns the contents of a service under a repository. """
  return _BASE_URL % ('repositories/%s/%s/services/%s' % (namespace, repository, service_id))

def repository_main_branch_url(namespace, repository):
  """ Returns the name of the main branch for the repository. """
  return _BASE_URL % ('repositories/%s/%s/main-branch' % (namespace, repository))
