<!DOCTYPE html>
<html>
<head>
  <title>Logging Data Entry</title>
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
  <style>
    body {
      background-image: url("{{ url_for('static', filename='pic.jpg') }}");
      background-size: cover;
      background-position: center;
    }

    /* Hide the video by default */
    #video {
      display: none;
    }
  </style>
</head>
<body>
  <h1>Logging Data Entry</h1>
  <form method="POST" action="/submit">
    <!-- Input fields -->
  </form>

  <!-- Video element -->
  <video id="video" width="320" height="240" controls autoplay>
    <source src="https://www.youtube.com/watch?v=aNFRZHkT4zE" type="video/mp4">
    Your browser does not support the video tag.
  </video>

  <script>
    // Function to show the video
    function showVideo() {
      var video = document.getElementById("video");
      video.style.display = "block";
    }

    // Check if the video can play
    document.getElementById("video").addEventListener("canplay", showVideo);
  </script>
</body>
</html>
