from sanic import Sanic, response
import os

app = Sanic("ModerationServer")

# Change this to the actual folder containing the files
MODERATION_FOLDER = os.path.abspath("modapps")
app.static('/static', './static')
@app.route("/")
async def serve_moderation_file(request, filename):
    file_path = os.path.join(MODERATION_FOLDER, filename)

    if not os.path.isfile(file_path):
        return response.text("File not found", status=404)

    return await response.file(file_path)
@app.route("/moderation/<filename>")
async def serve_moderation_file(request, filename):
    file_path = os.path.join(MODERATION_FOLDER, filename)

    if not os.path.isfile(file_path):
        return response.text("File not found", status=404)

    return await response.file(file_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6739)  # Adjusted port to 6739
