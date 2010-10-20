# vim: set fileencoding=utf-8
import os, sys, time

def pyncho_id(string):
    return string.replace(" ", "·").lower()

class Pyncho:
    version = 1.0
    tag = "a screaming comes across the sky"
    skeleton = os.path.join(sys.path[0], "skeleton")
    
    class Blog:
        title = None
        description = None

        name = None
        email = None

        # None for monthly or "seasonal"
        archive_style = None

        base_url = ""

        stylesheet = "pyncho.css"
        output_path = ".pyncho/output"
        node_path = ".pyncho/nodes"

        def read_rc_file(self, filename):
            variables = {}
            execfile(filename, {}, variables)
            self.__dict__.update(variables)

        # all posts, unsorted
        def posts(self):
            return []
            #TODO

        # a list of posts, sorted by date
        def posts_by_date(self):
            return []
            #TODO

        def first_post(self):
            return posts_by_date()[0]

        def archive(self):
            return Pyncho.Archive(posts)

        def recent_posts(self, count = 5):
            return posts_by_date()[0:count]

        def generate_latest(self):
            return generate("index.html")

        def generate_node(node):
            title = node.title + " ·" + self.title
            return generate("node.html")
        
        def generate_archive():
            title = "archives" + "· " + self.title
            return generate("archive.html")

        def generate_seasonal_archive():
            title = "seasonal archives" + " · " + self.title
            years = posts_by_date()
            return generate("seasonal-archive.html")

        def generate_feed():
            return generate("feed.rss", True)

        def generate(source, skipLayout=False):
            blueprint = Blueprint(".pyncho/blueprints/" + source)
            if skipLayout:
                blueprint = blueprint.through(layout)
            return blueprint.render(call.sender)

        layout = ".pyncho/blueprints/layout.html"

        # move diz
        def execute_hook(self, hook):
            hook_file = os.path.join(".pyncho/hooks/" + hook)
            if os.path.isfile(hook_file):
                os.system(hook_file)
            return

    class Post:
        source = None

        def __init__(self, path):
            self.source = path
            self.last_update = source.last_data_change_date
            self.meta = source.base_name.split(".")
            self.id = self.meta[0]
            self.title = self.id.replace("·", " ")
            self.published = time.strptime(self.meta[1], "%Y-%m-%d")

        def as_html():
            return Marxup(read_body).as_html

        def id():
            return self.id

        def generate():
            return Blueprint.new(".pyncho/blueprints/post.html").render #TODO

        def read_body():
            return source.contents

        def nice_date():
            return published.strftime("%d. %B %Y")

        def season():
            return str(((int(published.strftime("%m")) - 1) / 3) % 4)

        def month():
            return published.strftime("%Y %B")

        def year():
            return str(int(published.strftime("%Y") + 1)) if int(published.strftime("%m")) == 12 else str(int(published.stftime("%Y")))

    class Archive:
        def __init__(self):
            self.years = Map() #TODO and what about with
            return

        def append_posts(self, posts):
#            for post in posts:
#TODO
            return

        def posts_by_season(self):
            return #TODO

        def season_name(self, season):
            return ["winter", "spring", "summer", "autumn"][season]
