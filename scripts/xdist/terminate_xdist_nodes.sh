#!/bin/bash
set -e


if [ -f xdist_files/${XDIST_FILE_NAME_PREFIX}-task-arns.txt ]; then
    echo "Terminating xdist containers with pytest_container_manager.py"
    xdist_task_arns=$(<xdist_files/${XDIST_FILE_NAME_PREFIX}-task-arns.txt)
    python scripts/xdist/pytest_container_manager.py -a down --task_arns ${xdist_task_arns}
else
    echo "File: xdist_files/${XDIST_FILE_NAME_PREFIX}-task-arns.txt not found"
fi
