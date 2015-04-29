""" Defines a client class for working with the accounts API. """

from urls import account_profile_url

class BitBucketAccountsClient(object):
  """ A client for talking to the BitBucket accounts API. """
  def __init__(self, dispatcher, access_token, access_token_secret):
    self._dispatcher = dispatcher
    self._access_token = access_token
    self._access_token_secret = access_token_secret

  def get_profile(self, accountname_or_email):
    """ Returns profile information for the account matching the given account name or email
        address.
    """
    url = account_profile_url(accountname_or_email)
    return self._dispatcher.dispatch(url, access_token=self._access_token,
                                          access_token_secret=self._access_token_secret)
