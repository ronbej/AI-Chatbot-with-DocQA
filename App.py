from flask import Flask, request, jsonify
import DocQA
import ChatGPT

app = Flask(__name__)
filepath = "Contextfile.txt"
@app.route('/upload', methods=['GET'])
def upload():
    file = request.files['file']
    # Process the file here
    # Example: Save the file to a directory
    context = DocQA.processfile(file)
    with open(filepath, 'w') as file:
        pass
    with open(filepath, 'w') as file:
        file.write(context)
    #document_file.save(r'C:\Users\machi\OneDrive\Desktop\Chatbot\Contextfile.txt')
    #document_file = request.files['file']
    return 'File uploaded successfully.'

@app.route('/ajax', methods=['GET'])
def handle_ajax():
    data = request.get_json()  # Retrieve the JSON data sent by the client
    with open(filepath, 'r') as file:
        context = file.read()

    # Perform necessary processing on the data
    message = data['msg'] + ', your request is received.'
    tab = data['tab']
    if tab == 2:
        response = DocQA.sendResponse(message,context)
    elif tab == 1:
        response = ChatGPT.sendResponse(message)
    response = {'message': message}

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5500)