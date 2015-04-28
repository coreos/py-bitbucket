from bitbucket import BitBucket

def example():
  consumer_key = raw_input('Enter your consumer key: ')
  consumer_secret = raw_input('Enter your consumer secret: ')

  bb = BitBucket(consumer_key, consumer_secret, 'http://localhost/')
  (result, data, error_msg) = bb.get_authorization_url()
  if not result:
    print error_msg
    return

  print 'Open the following URL: ' + data['url']
  verifier = raw_input('Enter "oauth_verifier" from url: ')

  print 'Verifying token...'
  (result, data, error_msg) = bb.verify_token(data['access_token'], data['access_token_secret'],
                                              verifier)
  if not result:
    print error_msg
    return

  print 'Current user information: '
  client = bb.get_authorized_client(data[0], data[1])

  (result, data, error_msg) = client.get_current_user()
  if not result:
    print error_msg
    return

  print data

  print 'Retrieve branches and tags:'
  namespace = raw_input('Enter a user or team name: ')
  repository_name = raw_input('Enter a repository name: ')

  myrepo = client.for_namespace(namespace).repositories().get(repository_name)
  (result, data, error_msg) = myrepo.get_branches_and_tags()

  if not result:
    print error_msg
    return

  print data

example()