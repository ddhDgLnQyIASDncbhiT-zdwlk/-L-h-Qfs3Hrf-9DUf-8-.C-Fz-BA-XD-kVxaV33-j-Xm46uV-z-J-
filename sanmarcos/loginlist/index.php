<!doctype html>
<html>
<head>
    <!-- Metadata -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#F87201"/>

    <!-- Title & favicon -->
    <title>Logins List</title> 

    <!-- CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
</head>
<body>
    <div class="container">
    <table class="table">
        <thead>
            <tr>
            <th scope="col">Username</th>
            <th scope="col">Password</th>
            </tr>
        </thead>
        <tbody>
            <?php
                $mysqli = new mysqli("149.28.72.58", "nkomarn", "somepassword", "teacherlogins");
                
                /* TODO make a page for errors*/
                if($mysqli === false){
                    die("Cannot connect to database.");
                }
                
                $sql = "SELECT * FROM `teacherlogins`";
                if($result = $mysqli->query($sql)) {
                    if($result->num_rows > 0) {
                        while ($row = $result->fetch_array()) {
                            echo "<tr>";
                            echo "<td>{$row['user']}</td>";
                            echo "<td>{$row['pass']}</td>";
                            echo "</tr>";
                        }
                        $result->free();
                    }
                } 
                else {
                    echo "Database error.";
                }
                $mysqli->close();
            ?>
        </tbody>
    </table>
    </div>

    <!-- JavaScript -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</body>
</html>