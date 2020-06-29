# SPDX-License-Identifier: GPL-3.0+

from estuary.models.koji import ContainerKojiBuild, KojiBuild, KojiTag, ModuleKojiBuild
from estuary.models.bugzilla import BugzillaBug
from estuary.models.distgit import DistGitRepo, DistGitBranch, DistGitCommit
from estuary.models.errata import Advisory, ContainerAdvisory
from estuary.models.freshmaker import FreshmakerEvent, FreshmakerBuild
from estuary.models.user import User

all_models = (Advisory, BugzillaBug, ContainerAdvisory, ContainerKojiBuild,
              DistGitBranch, DistGitCommit, DistGitRepo, FreshmakerEvent, FreshmakerBuild,
              KojiBuild, KojiTag, ModuleKojiBuild, User)
names_to_model = {model.__label__: model for model in all_models}  # type: ignore


def _get_models_inheritance():
    """
    Create a dictionary mapping the model inheritance.

    :return: a dictionary with the keys as model labels and the values as labels inherited from it
    :rtype: dict
    """
    models_inheritance = {}
    for curr_model in all_models:
        models_inheritance[curr_model.__label__] = set([curr_model.__label__])
        for next_model in all_models:
            if next_model.__label__.endswith(curr_model.__label__):
                models_inheritance[curr_model.__label__].add(next_model.__label__)
    return models_inheritance


models_inheritance = _get_models_inheritance()
