function PanoptoVideoXBlock(runtime, element) {
    var $ = window.jQuery;

    function saveVideoUrl() {
        var videoUrl = $('#video_url_input').val();
        
        var handlerUrl = runtime.handlerUrl(element, 'save_video_url');
        
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({video_url: videoUrl}),
            success: function(response) {
                if (response.result === "success") {
                    alert("Video URL saved successfully.");
                } else {
                    alert("Failed to save the Video URL.");
                }
            }
        });
    }

    $(function() {
        $('#save_button').click(saveVideoUrl);
    });
}
