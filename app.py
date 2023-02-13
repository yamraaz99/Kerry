from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def generate_response():
    prompt = request.form["prompt"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify({"response": response["choices"][0]["text"]})

if __name__ == "__main__":
    app.run(debug=True)
