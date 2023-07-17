from flask import Flask, render_template, request, redirect
import yaml
from yaml import SafeLoader, FullLoader

app = Flask(__name__)


def read_one_block_of_yaml_data(filename):
    with open(f'{filename}', 'r') as f:
        output = list(yaml.safe_load_all(f))
    return output


@app.route('/rules', methods=['GET', 'POST'])
def index():
    acl = (read_one_block_of_yaml_data('configuration.yml')[0]["access_control"]["rules"])
    for idx, rule in enumerate(acl):
        print(idx, rule)
    return render_template('rules.html', acl=acl)


@app.route('/edit_rule/<int:id>', methods=['GET', 'POST'])
def edit_rule(id):
    return read_one_block_of_yaml_data('configuration.yml')[0]["access_control"]["rules"][id], 200


@app.route('/other_config', methods=['GET', 'POST'])
def other_config():
    return render_template('other_config.html')


if __name__ == '__main__':
    app.run()
