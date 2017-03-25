from __future__ import print_function

import os
from conda_build import source
from conda_build.metadata import MetaData


def mirror_dir(metadata):
    meta = metadata.get_section('source')
    git_url = meta['git_url']
    git_dn = git_url.split('://')[-1].replace('/', os.sep)
    if git_dn.startswith(os.sep):
        git_dn = git_dn[1:]
    git_dn = git_dn.replace(':', '_')
    return os.path.join(metadata.config.git_cache, git_dn)


def main():
    # Get the extra_source section of the metadata.
    recipe_dir = os.environ["RECIPE_DIR"]
    metadata = MetaData(recipe_dir)
    print(mirror_dir(metadata))


if __name__ == "__main__":
    main()
