<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>上传游戏</title>
</head>
<body>
    <form id="gameForm" method="post">
    <input type="text" name="game_name" placeholder="游戏名称" required><br/>
    <input type="url" name="download_link" placeholder="下载链接（需http/https）" required><br/>
    <textarea name="description" placeholder="游戏简介"></textarea>
    <button type="submit">提交</button>
</form>
    <?php
    if($_SERVER['REQUEST_METHOD'] === 'POST')
    {
        $gameName = htmlspecialchars($_POST['game_name'] ?? '');
        $downloadLink = trim($_POST['download_link'] ?? '');
        $description = htmlspecialchars($_POST['description'] ?? '');
        /*echo $gameName;
        echo $downloadLink;
        echo $description;*/
        try {
            $pdo = new PDO("mysql:host=sql313.infinityfree.com;dbname=if0_38041735_gts_website", "if0_38041735", "zLyW2sLuCxL");
            $sql = "INSERT INTO games (name, download_link, description) VALUES (:name, :link, :desc)";
            $stmt = $pdo->prepare($sql);
            // 传递关联数组（键名含冒号）
            $stmt->execute([
                ':name' => $gameName, 
                ':link' => $downloadLink, 
                ':desc' => $description
            ]);
            echo "✅ 提交成功！";
        } catch (PDOException $e) {
            die("数据库错误: " . $e->getMessage());
        }
    }
    ?>
</body>
</html>