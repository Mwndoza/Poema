from flask import  Flask

app = Flask(__name__)

@app.route("/")
def Con_esos_ojos_mirándome_no_me_hace_falta_la_luz_del_sol():
    return "Con esos ojos mirándome no me hace falta la luz del sol"

if __name__ == "__main__":
    app.run()