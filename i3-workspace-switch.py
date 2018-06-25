#!/usr/bin/env python

import argparse
import sys

import i3


def get_focused_output(workspaces):
    return [ws for ws in i3.get_workspaces() if ws['focused']][0]['output']


def get_active_outputs():
    return sorted(
        [outp['name'] for outp in i3.get_outputs() if outp['active']]
    )


def get_available_workspaces():
    outputs = get_active_outputs()
    available_workspaces = {}

    for index, output in enumerate(outputs):
        available_workspaces[output] = {}
        for l in range(1, 11):
            available_workspaces[output][l] = str(l + (10 * index))

    return available_workspaces


def get_command(args):
    return 'move container to workspace' if args.move else 'workspace'


def main():
    parser = argparse.ArgumentParser(
        description='Utility for switching to unnumbered i3 workspaces '
                    'using their relative position.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'number',
        metavar='NUMBER',
        type=int,
        help='Number of the workspace to focus. Starting with 1.')
    parser.add_argument(
        '-m', '--move',
        action='store_true',
        default=False,
        help='move')

    args = parser.parse_args()

    if args.number < 1 or args.number > 10:
        print('Workspace number must be >= 1 and <= 10')
        sys.exit(1)

    workspaces = i3.get_workspaces()

    available_workspaces = get_available_workspaces()
    focused_output = get_focused_output(workspaces)
    command = get_command(args)

    i3.command(
        command,
        available_workspaces[focused_output][args.number]
    )


if __name__ == '__main__':
    main()
