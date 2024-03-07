<?php

if ($_SERVER["REQUEST_METHOD"]=='POST'){

    if (empty($_POST['username']) || empty($_POST['password'])) { // this checks if the input fields are empty
        echo "username or passwrod is missing";
    } else {
        $username=$_POST['username']; // 'username' is the name of the input field
        $password=$_POST['password']; // 'password' is the name of the input field

        echo "The username you have entered is $username <br>";
        echo "The password you have entered is $password <br>";  

        $db_host="localhost"; // Corrected variable name
        $db_user="root";
        $db_pass="passboi";
        $db_name="users";

        $sql = "SELECT * FROM users WHERE username='$username' AND password='$password'"; // Corrected query
        $result = mysql_query($sql);


    }
}