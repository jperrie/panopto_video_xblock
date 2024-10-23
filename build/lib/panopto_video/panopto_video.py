"""TO-DO: Write a description of what this XBlock is."""

from importlib.resources import files

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String


class PanoptoVideoXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    video_url = String(help="The URL for the Panopto video.", default="")
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        html = f"""
            <div>
                <iframe src="" width="640" height="360" allowfullscreen></iframe>
            </div>
        """
        frag = Fragment(html)
        return frag

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PanoptoVideoXBlock",
             """<panopto_video/>
             """),
            ("Multiple PanoptoVideoXBlock",
             """<vertical_demo>
                <panopto_video/>
                <panopto_video/>
                <panopto_video/>
                </vertical_demo>
             """),
        ]
