# vim: set fileencoding=utf-8
import os, sys, time, datetime

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
            return [Pyncho.Post(os.path.join(self.node_path, file))
                for file in os.listdir(self.node_path)
                if os.path.splitext(os.path.normcase(file))[1] == ".txt"]

        # a list of posts, sorted by date
        def posts_by_date(self):
            return sorted(self.posts(), key=(lambda post: post.published))

        def first_post(self): #TODO Remove?
            return self.posts_by_date()[0]

        def archive(self):
            return Pyncho.Archive(self.posts())

        def recent_posts(self, count = 5):
            return self.posts_by_date()[0:count]

        def generate_latest(self):
            return self.generate("index.html")

        def generate_node(self, node):
            title = node.title + " ·" + self.title
            return self.generate("node.html")
        
        def generate_archive(self):
            title = "archives" + "· " + self.title
            return self.generate("archive.html")

        def generate_seasonal_archive(self):
            title = "seasonal archives" + " · " + self.title
            years = self.posts_by_date()
            return self.generate("seasonal-archive.html")

        def generate_feed(self):
            return self.generate("feed.rss", True)

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
            self.last_update = os.path.getmtime(path)
            self.meta = os.path.basename(self.source).split(".")
            self.id = self.meta[1]
            self.title = self.id.replace("·", " ")
            self.published = datetime.datetime.strptime(self.meta[0], "%Y-%m-%d")

        def as_html(self):
            return Marxup(read_body()).as_html

        def id(self):
            return self.id

        def generate():
            return Blueprint.new(".pyncho/blueprints/post.html").render #TODO

        def read_body(self):
            return self.source.contents

        def nice_date(self):
            return self.published.strftime("%d. %B %Y")

        def season(self):
            return str(((int(self.published.strftime("%m")) - 1) / 3) % 4)

        def month(self):
            return self.published.strftime("%Y %B")

        def year(self):
            return str(int(self.published.strftime("%Y") + 1)) if int(self.published.strftime("%m")) == 12 else str(int(self.published.stftime("%Y")))

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
