# $ do-cli_

## Setup

***This package uses redis***


First, clone this repository

````
git clone git@github.com:meganlkm/do-cli.git
````

Next, copy env.template to .env and set the variables to your configuration. Then source .env

### Installation

````
pip install .

# for development:
pip install git+git://github.com/john2x/solarized-pygment.git#egg=solarized-pygment
pip install --editable .
````

## Usage

````
Usage: do-cli [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  --cache-path TEXT         Path to the cache files (default: .)
  -a, --api-key TEXT        Set the DigitalOcean API Key
  -c, --client-id TEXT      Set the DigitalOcean Client ID
  -m, --cache-max-age TEXT  Maximum age of the cached items (default: 0)
  -p, --pretty              Pretty-print results
  -v, --verbose
  --help                    Show this message and exit.

Commands:
  all                List all DigitalOcean information
  ansible-inventory  Generate Ansible inventory
  domains            List Domains
  droplets           Droplets CRUD
  env                Display DigitalOcean environment variables
  flush-cache        clear the cache
  images             List Images
  list               Minimal droplet info
  regions            List Regions
  sizes              List Sizes
  ssh-keys           List SSH keys
````


## TODO

This package was hacked together to give me a sanity break. There is still more awesomeness to be had with this.
