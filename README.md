# Hyrule Compendium CLI
The official CLI for the Hyrule Compendium API.

## Installation

    $ pip3 install hyrule-compendium-cli

## Usage

    Usage: hyrule [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    get-all       Get all items in the compendium
    get-category  Get items in a category
    get-entry     Get a specific entry

All commands have an optional flag `-f` / `--format`, which formats the JSON response.