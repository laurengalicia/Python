def account_list(filename):
    return [line.split('"')[0] for line in open(filename, 'r').read().split('"value": "')]

# change filenames if necessary
followers = account_list('followers_1.json')
following = account_list('following.json')
following.sort()

for account in following:
    if account not in followers:
        print(account)
