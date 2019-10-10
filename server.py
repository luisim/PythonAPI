from flask import Flask
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

@app.route('/',methods=['GET'])
def defaultHome():
    return "use /getData on the HTTP GET method"

@app.route('/getData',methods=['GET'])
def home():
    x = [{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Luis Escobar","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Amazing. The best. Incredible","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Literally none"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunning, deserves a raise really","Answer 1":"Amazing. The best. Incredible","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Relax more, this guy won't stop working"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"If this guy doesn't get a raise I quit","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could take a few days off, working that much is not healthy"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Pablo Pena","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Average","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Uff, can't even count them"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunning, deserves a raise really","Answer 1":"Decent","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Commitment"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"It's okay","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Concentration"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Lionel Flores","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Not above average","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Being above average"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunning, deserves a raise really","Answer 1":"The best... At nothing","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could commit more"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"As effective as a water gun trying to turning off a volcano","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could show some interest in work"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Fernando Molina","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"He could loose a game of hide and seek against a blind man","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Just by doing something"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunning, deserves a raise really","Answer 1":"Just bad","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Couldn't be worst even if he didn't work at all"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Laziest person ever","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Showing commitment"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Mauricio Palacios","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"It's like a gas station employing an arsonist","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Oh god"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunning, deserves a raise really","Answer 1":"Incredibly absent","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Will not work at all"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"If this guy GETS a raise, I quit","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could take a few days off, please"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Rodrigo Reyes","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Slower than Claro's internet","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Literally everything"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunningly slow","Answer 1":"Too angry","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Relax more, you can't say anything to him"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Just slow","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could be healthier"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Alex Mejia","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Too soon to tell but doesn't look good","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Literally everything"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunningly slow","Answer 1":"His smash bros game is weak","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Just more practice"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Feels like he doesn't care","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could be healthier"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Fernando Arias","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Takes too long to get going, like dial up internet","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Stop playing on your phone"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunningly slow","Answer 1":"Pretty average","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Should try to prove something to himself"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Very average at his work","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could be healthier"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Victor Rodriguez","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Very good, show interest in work and gets things done","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Could work better with a team"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunningly slow","Answer 1":"Quick at his work and effective","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Should work on organizing better his work"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Very knowleageable on his area","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Working with a team could be improved"}]}]},{"Review Cycle":"360 Project Feedback, Individual Participants, May 2019","Completed Date:":"2019-04-22","Employee Name":"Nelson Escobar","Project Name":"Performance Review","Writers":[{"Name":"Ivania Rivas","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Has a very interesting view of the world and that is reflected on his work","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Just a bit of more energy"}]},{"Name":"Ricardo Ramirez","Questions":[{"Question 1":"Stunningly slow","Answer 1":"Very positive and a hard worker","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Should work on his schedule"}]},{"Name":"Dalia Portillo","Questions":[{"Question 1":"How effective was this person as a project contributor?","Answer 1":"Great attitude towards work","Question 2":"Please suggest some areas in which this colleague could improve their performance or grow their skills, in order to strengthen their project performance and increase their contributions","Answer 2":"Should handle better when working under presion"}]}]}]
    y = json.dumps(x, indent=4, sort_keys=True)
    return y
    

if __name__ == '__main__':
    app.run(debug=True)