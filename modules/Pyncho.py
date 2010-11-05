# vim: set fileencoding=utf-8
import os, sys, time, datetime
from Cheetah.Template import Template
from Marxup import *

def pyncho_id(string):
    return string.replace(" ", "·").lower()

class Pyncho:
    version = 1.0
    tag = "a screaming comes across the sky"
    skeleton = os.path.join(sys.path[0], "skeleton")
    
    class Blog:
        def __init__(self):
            self.title = None
            self.description = None
    
            self.name = None
            self.email = None
    
            # None for monthly or "seasonal"
            self.archive_style = None
    
            self.base_url = ""
    
            self.stylesheet = "pyncho.css"
            self.output_path = os.path.join(".pyncho", "output")
            self.node_path = os.path.join(".pyncho", "nodes")
            self.layout = os.path.join(".pyncho", "blueprints", "layout.html")

        def read_rc_file(self, filename):
            """Read a settings file and set options accordingly"""
            variables = {}
            execfile(filename, {}, variables)
            self.__dict__.update(variables) # Update object variables

        # all posts, unsorted
        def posts(self):
            if not os.path.exists(self.node_path):
                return []
            return [Pyncho.Post(os.path.join(self.node_path, file), self)
                for file in os.listdir(self.node_path)
                if os.path.splitext(os.path.normcase(file))[1] == ".txt"]

        # a list of posts, sorted by date
        def posts_by_date(self):
            return sorted(self.posts(), key=(lambda post: post.published))

        def first_post(self):
            return self.posts_by_date()[0]

        def latest_post(self):
            return self.posts_by_date()[-1]

        def archive(self):
            return Pyncho.Archive(self.posts())

        def recent_posts(self, count = 5):
            return self.posts_by_date()[0:count]

        def generate_latest(self):
            return self.generate("index.html")

        def generate_node(self, node, skip_layout = False):
            title = node.title + " · " + self.title
            return self.generate("node.html", [title, node], skip_layout)
        
        def generate_archive(self):
            title = "archives" + " · " + self.title
            return self.generate("archive.html", [title])

        def generate_seasonal_archive(self):
            title = "seasonal archives" + " · " + self.title
            years = self.posts_by_date()
            return self.generate("seasonal-archive.html", [title, years])

        def generate_feed(self):
            return self.generate("feed.rss", skip_layout = True)

        def generate(self, source, variables = [], skip_layout = False):
            blueprint = Template(file = os.path.join(".pyncho", "blueprints", source), searchList = variables + [self])
            if not skip_layout:
                blueprint = Template(file = self.layout, searchList = variables + [self, {'wrapped': str(blueprint)}])
            return str(blueprint)

        # move diz
        def execute_hook(self, hook):
            hook_file = os.path.join(".pyncho", "hooks", hook)
            if os.path.isfile(hook_file):
                os.system(hook_file)
            return

    class Post:
        """An individual entry in the blog"""
        def __init__(self, path, blog):
            self.blog = blog
            self.source = path
            self.last_update = os.path.getmtime(path)
            self.meta = os.path.basename(self.source).split(".")
            self.id = self.meta[1]
            self.title = self.id.replace("·", " ")
            self.published = datetime.datetime.strptime(self.meta[0], "%Y-%m-%d")

        def as_html(self):
            return Marxup(self.read_body()).as_html()

        def escape_html(self): #TODO
            return self.read_body()

        def generate(self):
            return self.blog.generate("post.html", variables = [{'post': self}], skip_layout = True)

        def read_body(self):
            f = open(self.source, 'r')
            body = f.read()
            f.close()
            return body

        def nice_date(self):
            return self.published.strftime("%d. %B %Y")

        def season(self):
            """Return the season the entry was posted"""
            # In lieu of a Python enum type:
            return str(((int(self.published.strftime("%m")) - 1) / 3) % 4)

        def month(self):
            return self.published.strftime("%Y %B")

        def year(self):
            return str(int(self.published.strftime("%Y") + 1)) if int(self.published.strftime("%m")) == 12 else str(int(self.published.stftime("%Y")))

        def atom_date(self):
            d = self.published.strftime('%Y-%m-%dT%H:%M:%S%z')
            return d[:-2] + ':' + d[-2:]

#    class Archive:
#        def __init__(self, blog):
#            self.years = Map() #TODO and what about with
#            self.blog = blog
#            return
#
#        def append_posts(self, posts):
##            for post in posts:
##TODO
#            return
#
#        def posts_by_season(self):
#            return #TODO
#
#        def season_name(self, season):
#            return ["winter", "spring", "summer", "autumn"][season]
