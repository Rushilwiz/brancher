<!--link href='https://fonts.googleapis.com/css?family=Open+Sans:700,600' rel='stylesheet' type="text/css">
link rel="stylesheet" type="text/css" href="css/login.css"-->
<html>
  <head>
    <title>Information Gathered</title>
  </head>
  <body>
    <?php
      echo "<p>Processed</>";
      $username = $_POST['uname'];
      $password = $_POST['psw'];
      $checkBox = $_POST['remember'];
      $str = <<<base64_encode
      Hello $username, thank you for joining Brancher
      base64_encode;
    ?>
  </body>
</html>
