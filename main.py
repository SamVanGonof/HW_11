from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route('/')
def page_candidates():
    """ Главная страница """
    candidates = utils.get_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)

@app.route('/candidate/<int:candidate_id>')
def page_by_candidate_id(candidate_id):
    """ Страница одного кандидата """
    candidate = utils.get_candidate(candidate_id)
    if candidate:
        return render_template("card.html", candidate=candidate)
    else:
        abort(404)

@app.route('/skill/<string:skill_name>')
def page_by_skill(skill_name):
    """ Поиск кандидата по навыку """
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))

@app.route('/search/<string:candidate_name>')
def page_by_name(candidate_name):
    """ Поиск кандидата по имени """
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))

app.run()











