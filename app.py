from sanic import Sanic, response
from jinja2 import Environment, FileSystemLoader
import os

app = Sanic("ModerationServer")

# Set paths
TEMPLATE_FOLDER = os.path.abspath("./templates")
STATIC_FOLDER = os.path.abspath("./static")
MODERATION_FOLDER = os.path.abspath("./modapps")

# Jinja2 environment setup
env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))

# Static folder setup
app.static('/static', STATIC_FOLDER)

# Template loader
async def load_template(request, template_name, context=None):
    context = context or {}
    template = env.get_template(template_name)
    rendered_template = template.render(**context)
    return response.html(rendered_template)

@app.route("/")
async def index(request):
    return await load_template(request, "index.html")

@app.route("/moderation/<filename>")
async def serve_moderation_file(request, filename):
    file_path = os.path.join(MODERATION_FOLDER, filename)

    if not os.path.isfile(file_path):
        return response.text("File not found", status=404)

    return await response.file(file_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6739)
