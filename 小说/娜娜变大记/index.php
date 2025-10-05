<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>mc</title>
</head>
<body>
<ol>
    <?php
    include "../../php/gen_dir_list.php";
     $lis = gen_novel_list(".");
     for($i = 0; $i < count($lis); $i++) 
     {
        if($lis[$i] != "./index.php")
        {
            echo "<li><a href='" . htmlspecialchars($lis[$i]) . "'>" . htmlspecialchars(urldecode(basename($lis[$i]))) . "</a></li>";
        }
     }
     ?>
    </ol>
</body>
</html>
