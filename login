<!DOCTYPE html>
<html>
  <head>
    <title>Login Page</title>
  </head>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
      }
      h2 {
        color: #333;
        text-align: center;
      }
      form {
        max-width: 300px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        background-color: #fff;
      }
      label {
       display: inline-block; /* Display label inline with input */
       font-weight: bold;
       margin-bottom: 5px;
       width: 30%; /* Set width to 30% of parent container */
       text-align: right; /* Align text to right of label */
      }

      input[type="text"], input[type="password"] {
        display: inline-block; /* Display input inline with label */
        width: 68%; /* Set width to 68% of parent container */
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
      }
      input[type="submit"] {
        display: block; /* Make the button a block element */
        margin: 0 auto; /* Center the block element horizontally */
        background-color: #67c8ff;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
     }
      input[type="submit"]:hover {
        background-color: #45a049;
      }
    </style>
  <body>
       <h2>Login</h2>
    <form method="post" action ="{{ url_for("login") }}">
        <label for="username" name="username" value="{{ username }}">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" value="{{ password }}"required><br><br>
        <input type="submit" value="Login">
    </form>
  </body>
</html>
