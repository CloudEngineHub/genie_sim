
# Copyright (c) 2023-2025, AgiBot Inc. All Rights Reserved.
# Author: Genie Sim Team
# License: Mozilla Public License Version 2.0

import os

# PATHS
ACTIVITY_CONFIGS_PATH = os.path.join(os.path.dirname(__file__), "task_definitions")

# BDDL
SUPPORTED_BDDL_REQUIREMENTS = [":strips", ":negative-preconditions", ":typing", ":adl"]

READABLE_PREDICATE_NAMES = {"ontop": "on top of", "nextto": "next to"}


def get_definition_filename(behavior_activity, instance, domain=False):
    if domain:
        return os.path.join(ACTIVITY_CONFIGS_PATH, "domain_igibson.bddl")
    else:
        return os.path.join(
            ACTIVITY_CONFIGS_PATH, behavior_activity, f"problem{instance}.bddl"
        )


def get_domain_filename(domain_name):
    return os.path.join(ACTIVITY_CONFIGS_PATH, f"domain_{domain_name}.bddl")


# MISC
GROUND_GOALS_MAX_OPTIONS = 20
GROUND_GOALS_MAX_PERMUTATIONS = 10
