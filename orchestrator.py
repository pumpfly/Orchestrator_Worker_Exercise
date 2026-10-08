from flask import Flask, request


if __name__ == "__main__":
    server = Flask(__name__)

    tasks = {
        0: "1 + 1 = ",
        1: "39457 : 7 = ",
        2: "789 x 23 = "
    }

    answers = {}

    @server.route("/")
    def index_handler():
        return "bobr"

    @server.route("/task")
    def task_handler():
        if len(tasks) == 0:
            return "finished"
        id = list(tasks.keys())[0]
        task = tasks[id]
        del tasks[id]
        return f"{id}.) {task}"

    @server.route(f"/handover")
    def handover_handler():
        id = request.args.get("id")
        answer = request.args.get("answer")
        answers[id] = answer
        return "done"


    @server.route("/answers")
    def answer_handler():
        return f"we have {len(answers)} answers:\n{answers}"

    server.run(port=7999)





