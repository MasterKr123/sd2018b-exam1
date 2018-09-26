import logging
def get_user_info(username=None):
    return {"user_info": username}
def get_commits_info(username=None, time_range=None):
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]
def get_user_commits(organization=None, repository=None, username=None):
    logging.info('executing get_user_commits method')
    logging.debug('organization=%s', organization)
    logging.debug('repository=%s', repository)
    logging.debug('username=%s', username)
    return [{'commit_number': 1, 'description': 'Init commit'}]
