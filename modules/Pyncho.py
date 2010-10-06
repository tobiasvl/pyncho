# vim: set fileencoding=utf-8
import os, sys

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
        base_tag = None #TODO

        stylesheet = "pyncho.css"
        output_path = ".pyncho/output"
        node_path = ".pyncho/nodes"

        def read_rc_file(self, filename):
            variables = {}
            execfile(filename, {}, variables)
            self.__dict__.update(variables)

        # all posts, unsorted
        def posts():
            return
            #TODO

        # a list of posts, sorted by date
        def posts_by_date():
            return
            #TODO

        def first_post():
            posts_by_date()[0]

        def archive():
            Poncho.Archive(posts)

        def recent_posts(count = 5):
            posts_by_date()[0:count]

        def generate_latest():
            generate("index.html")

        def generate_node(node):
            title = node.title + " ·" + self.title
        
        def generate_archive():
            title = "archives" + "· " + self.title
            generate("archive.html")

        def generate_seasonal_archive():
            title = "seasonal archives" + " · " + self.title
            years = posts_by_date()
            generate("seasonal-archive.html")

        def generate_feed():
            generate("feed.rss", True)

        def generate(source, skipLayout):
            blueprint = Blueprint(".poncho/blueprints/" + source)
            if skipLayout:
                blueprint = blueprint.through(layout)
            blueprint.render(call.sender)

        layout = ".poncho/blueprints/layout.html"

        # move diz
        def execute_hook(hook):
            hook = os.join(".poncho/hooks/" + hook)
            if os.isfile(hook):
                os.system(hook)

    class Post:
        source = None

        def as_html():
            Marxup(read_body).as_html

        def id():
            self.id
