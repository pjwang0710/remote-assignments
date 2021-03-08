from flask import Flask, request, render_template, make_response, url_for, redirect

app = Flask(__name__, 
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/data', methods=['GET'])
def get_data():
    number = request.args.get('number', default=None)
    if number is None:
        return 'Lack of Parameter'
    if not number.isdigit():
        return 'Wrong Parameter'
    number = int(number)
    return str((1 + number) * number //2)

@app.route('/myName')
def get_my_name():
    name = request.cookies.get('name', None)
    if name:
        return 'Done'
    return render_template('name.html')

@app.route('/trackName')
def track_name():
    name = request.args.get('name', default=None, type=str)
    if name:
        resp = make_response(redirect(url_for('get_my_name')))
        resp.set_cookie('name', name)
        return resp
    return 'something wrong'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
