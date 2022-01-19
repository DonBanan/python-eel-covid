import eel
from covid import Covid


@eel.expose
def get_covid():
    covid = Covid()
    cases = covid.get_data()
    return cases


eel.init("web")
eel.start("index.html", size=(700, 700))
