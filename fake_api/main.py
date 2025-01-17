from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/contests/<contest_id>", methods=["GET"])
def contest_info(contest_id):
    result = {
        "contest_id": contest_id,
        "contest_top_content": "# Hello World!  ## Welcome!",
        "problem_list": [
            {
                "problem_id": "Hello_World",
                "problem_order": "A",
                "problem_name": "Hello World!",
                "time_limit": 2,
                "memory_limit": 256,
                "problem_score": 100,
            },
            {
                "problem_id": "uruu",
                "problem_order": "B",
                "problem_name": "is uruu?",
                "time_limit": 2,
                "memory_limit": 256,
                "problem_score": 100,
            },
            {
                "problem_id": "New_Hello_World",
                "problem_order": "C",
                "problem_name": "New Hello World!",
                "time_limit": 2,
                "memory_limit": 256,
                "problem_score": 1000,
            },
        ],
    }
    return jsonify(result)


@app.route("/contests", methods=["GET"])
def contests():
    result = {
        "upcoming": [
            {
                "contest_id": "mitohato",
                "contest_name": "mito_contest",
                "contest_date": "2019-08-17 12:00:00",
                "contest_time": 120,
                "writer": "mitohato",
                "contest_description": "Welcome!",
                "problem_number": 2,
            },
            {
                "contest_id": "nemusou",
                "contest_name": "nemusou_contest",
                "contest_date": "2019-08-17 12:00:00",
                "contest_time": 120,
                "writer": "mitohato",
                "contest_description": "Hello World!",
                "problem_number": 2,
            },
        ],
        "current": [
            {
                "contest_id": "kurokoji",
                "contest_name": "kurokoji_contest",
                "contest_date": "2019-08-17 12:00:00",
                "contest_time": 120,
                "writer": "mitohato",
                "contest_description": "Hello World!",
                "problem_number": 2,
            }
        ],
        "recent": [
            {
                "contest_id": "10riridk0",
                "contest_name": "10riridk0_contest",
                "contest_date": "2019-08-17 12:00:00",
                "contest_time": 120,
                "writer": "mitohato",
                "contest_description": "Hello World!",
                "problem_number": 2,
            }
        ],
    }
    return jsonify(result)

@app.route("/contests/<contest_id>/ranking", methods=["GET"])
def ranking(contest_id):
    result = [
        {
            "rank": 1,
            "user_id": "mitohato",
            "total": "5/5",
            "score": "5000"
        },
        {
            "rank": 2,
            "user_id": "222mitohato",
            "total": "5/5",
            "score": "5000"
        },
        {
            "rank": 3,
            "user_id": "fdmitohato",
            "total": "2/5",
            "score": "1000"
        },
        {
            "rank": 4,
            "user_id": "0mitohato",
            "total": "0/5",
            "score": "0"
        },
    ]
    return jsonify(result)

@app.route("/contests/<contest_id>/problems/<problem_id>", methods=["GET"])
def problem(contest_id, problem_id):
    result = {
       "contest_id": contest_id,
       "problem_id": problem_id,
       "problem_name": "初めての競技プログラミング",
       "time_limit": 2,
       "memory_limit": 2,
       "score": 100,
       "writer": "uchipara",
       "problem_detail": "ある2つの整数aとbが与えられます. 2つの整数の和を出力してください.",
    }
    return jsonify(result)

@app.route("/languages", methods=["GET"])
def lang():
    result = ["C", "C++", "Python", "Java"]
    return jsonify(result)

@app.route("/contests/<contest_id>/submits", methods=["GET"])
def submit_list(contest_id):
    result = [
        {
            "submit_id": "123456",
            "submit_date": "2019-05-05",
            "problem_name": "Douteki keikaku plan",
            "language": "C++",
            "score": 100,
            "code_length": 100,
            "result": "AC",
            "username": "nemu_sou",
            "execute_time": 300,
            "memory": 400,
            "source_code": 'printf("HelloWorld");'
        },
        {
            "submit_id": "929292",
            "submit_date": "2019-05-05",
            "problem_name": "Hello World",
            "language": "C++",
            "score": 100,
            "code_length": 100,
            "result": "WA",
            "username": "nemu_sou",
            "execute_time": 300,
            "memory": 400,
            "source_code": 'printf("HelloWorld");'
        },
        {
            "submit_id": "122222",
            "submit_date": "2019-05-05",
            "problem_name": "Douteki keikaku plan",
            "language": "C++",
            "score": 100,
            "code_length": 100,
            "result": "WJ",
            "username": "nemu_sou",
            "execute_time": 300,
            "memory": 400,
            "source_code": 'printf("HelloWorld");'
        },
    ]
    return jsonify(result)



@app.route("/contests/<contest_id>/submits/<submit_id>", methods=["GET"])
def submit(contest_id, submit_id):
    result = {
        "submit_id": "123456",
        "submit_date": "2019-05-05",
        "problem_name": "Douteki keikaku plan",
        "language": "C++",
        "score": 100,
        "code_length": 100,
        "result": "AC",
        "username": "nemu_sou",
        "execute_time": 300,
        "memory": 400,
        "source_code": 'printf("HelloWorld");'
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run()
