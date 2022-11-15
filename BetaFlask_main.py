# import random so we can use random numbers
import random
import secrets

# Import flask which is a micro web framework written in Python.
from flask import (
    Flask,
    jsonify, render_template, session, Response
)

import BetaController
# Function that create the app
import GraphController

# matplot lib gives us the ability to draw charts

'''
create_app will be called when we want to start listening on a port for http traffic. It's main purpose is to rerun a flask object with routes (URLS) defined

'''


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    secret = secrets.token_urlsafe(32)
    app.secret_key = secret

    @app.route('/BetaREST/<stockName>/<numberOfPeriods>')
    def BetaRest(stockName="AAPL", numberOfPeriods=10):
        numberOfPeriods = int(numberOfPeriods)
        base_betas = [1]
        chunked_betas = [2]
        retValue = ""
        ############
        # Uncomment below and replace the function call below with the call to BetaController's do_calculations function, passing stockName and number of Periods)
        try:
            base_betas, chunked_betas = BetaController.do_calculations(stockName, numberOfPeriods)
            retValue = jsonify({
                "chunked_betas": chunked_betas,
                "base_betas": base_betas
            })
        except:
            retValue = jsonify({
                "Ticker": stockName,
                "numberOfPeriods": numberOfPeriods
            })
            print("An exception occurred")
            with open("BadData.txt", "a") as outfile:
                outfile.write(str(retValue.json))
                outfile.write("\n")
            outfile.close()
        ############

        session["stock_name"] = stockName
        session['beta_list'] = chunked_betas
        session['base_line_list'] = base_betas
        session['numberOfPeriods'] = numberOfPeriods
        return retValue

    @app.route('/Beta/<stockName>/<numberOfPeriods>')
    def Beta(stockName="AAPL", numberOfPeriods=10):
        numberOfPeriods = int(numberOfPeriods)
        base_betas = [1]
        chunked_betas = [2]

        ############
        # Uncomment below and replace the function call below with the call to BetaController's do_calculations function, passing stockName and number of Periods)
        base_betas, chunked_betas = BetaController.do_calculations(stockName, numberOfPeriods)
        ############

        session["stock_name"] = stockName
        session['beta_list'] = chunked_betas
        session['base_line_list'] = base_betas
        session['numberOfPeriods'] = numberOfPeriods
        return render_template('hello_world.html', stockName=stockName)

    @app.route('/beta/plot.png')
    def plot_png():
        beta_list = session['beta_list']
        base_line_list = session['base_line_list']
        stockName = session["stock_name"]
        #### Debug statement
        print("In Flask's plot_png Debug: Going to create a chart with the following values", "beta list: ", beta_list,
              "base_line: ",
              base_line_list, "Security Name:", stockName, sep='\n')
        #####
        # once you have completed the output assignment below this below line can be commented out
        output = GraphController.create_figure(stockName)

        ########
        # Reset the output function below.
        output = GraphController.draw_beta_chart_with_baseline(beta_list, base_line_list, stockName)
        ########
        return Response(output.getvalue(), mimetype='image/png')

    #  Simple route
    @app.route('/')
    def hello_world():
        return jsonify({
            "status": "success",
            "message": "Hello World, you need to goto /Beta/APPL/10 for this project!"
        })



    return app  # do not forget to return the app
APP = create_app()

if __name__ == '__main__':
    ranGuess = random.randint(2, 100)
    port = 8081
    url_to_test = "http://127.0.0.1:" + str(port) + "/BetaREST/AAPL/" + str(ranGuess)
    print("goto ", url_to_test, " to test")
    APP.run(debug=True, port=8081)
