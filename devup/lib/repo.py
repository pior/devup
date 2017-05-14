import re

# repo short name = org/repo
RE_REPO_SHORT = re.compile(r'(?P<org>\w+)/(?P<repo>\w+)')

# Github ssh url
RE_GITHUB = re.compile(r'git@github.com:(?P<org>\w+)/(?P<repo>\w+).git')


class GithubRepo(object):
    """Project as a remote repository."""

    def __init__(self, org, repo):
        self._org = org
        self._repo = repo

    @classmethod
    def from_location(cls, location):
        m = RE_REPO_SHORT.match(location)
        if m:
            groups = m.groupdict()
            return cls(groups['org'], groups['repo'])

    @property
    def location(self):
        return 'git@github.com:%s/%s.git' % (self._org, self._repo)

    @property
    def local_id(self):
        return ['github.com', self._org, self._repo]
