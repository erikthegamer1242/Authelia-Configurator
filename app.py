from flask import Flask, render_template, request, redirect
import ruamel.yaml
import ast

yaml = ruamel.yaml.YAML()

app = Flask(__name__)


def read_one_block_of_yaml_data(filename):
    with open(f'{filename}', 'r') as f:
        output = list(yaml.load_all(f))
    return output


def save_yaml(data, filename):
    with open(filename, 'w') as stream:
        yaml.dump_all(data, stream)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rules', methods=['GET', 'POST'])
def rules():
    acl = (read_one_block_of_yaml_data('configuration.yml')[0]["access_control"]["rules"])
    # for idx, rule in enumerate(acl):
    # print(idx, rule)
    # print(read_one_block_of_yaml_data('configuration.yml'))
    return render_template('rules.html', acl=acl)


@app.route('/edit_rule/<int:id>', methods=['GET', 'POST'])
def edit_rule(id):
    # return read_one_block_of_yaml_data('configuration.yml')[0]["access_control"]["rules"][id], 200
    if request.method == 'POST':
        domains = ast.literal_eval(request.form['domainsArr'])
        policy = request.form['policy']
        config = read_one_block_of_yaml_data('configuration.yml')
        config[0]["access_control"]["rules"][id]["domain"] = domains
        config[0]["access_control"]["rules"][id]["policy"] = policy
        save_yaml(config, 'configuration.yml')
        return redirect('/rules')
    return render_template('edit_rule.html',
                           rule=read_one_block_of_yaml_data('configuration.yml')[0]["access_control"]["rules"][id],
                           id=id)


@app.route('/other_config', methods=['GET', 'POST'])
def other_config():
    return render_template('other_config.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
