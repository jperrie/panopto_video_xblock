"""TO-DO: Write a description of what this XBlock is."""

from importlib.resources import files

from xblock.core import XBlock
from xblock.fields import String
from web_fragments.fragment import Fragment

import pkg_resources

class PanoptoVideoXBlock(XBlock):
    """
    XBlock for embedding a Panopto video using a URL provided by the user.
    """
    video_url = String(help="The URL for the Panopto video.", default="")

    def resource_string(self, path):
        """Helper function for getting resource content from files."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # Display the Panopto video in the student view
    def student_view(self, context=None):
        html = f"""
            <div>
                <iframe src="{self.video_url}" width="640" height="360" allowfullscreen></iframe>
            </div>
        """
        frag = Fragment(html)
        return frag

    # Provide a studio view for editing the video URL
    def studio_view(self, context=None):
        html = f"""
            <div class="panopto-edit-block">
                <label for="video_url">Video URL:</label>
                <input type="text" id="video_url_input" value="{self.video_url}" />
                <button id="save_button">Save</button>
            </div>
        """
        fragment = Fragment(html)
        fragment.add_css(self.resource_string("static/css/panopto_edit.css"))
        fragment.add_javascript(self.resource_string("static/js/src/panopto_edit.js"))
        fragment.initialize_js('PanoptoVideoXBlock')
        return fragment

    # JSON handler to save the video URL
    @XBlock.json_handler
    def save_video_url(self, data, suffix=''):
        """
        Handle the submission of the edited video URL from the Studio view.
        """
        # Update the video_url field with the data from the form
        self.video_url = data.get('video_url', '')
        return {'result': 'success'}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("PanoptoVideoXBlock",
             """<panopto_video/>"""),
            ("Multiple PanoptoVideoXBlock",
             """<vertical_demo>
                <panopto_video/>
                <panopto_video/>
                <panopto_video/>
                </vertical_demo>
             """),
        ]

