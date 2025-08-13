<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>gts游戏下载</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px auto;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        
        .download-link {
            color: #007bff;
            text-decoration: none;
        }
        
        .download-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">GTS游戏列表</h1>
    
    <?php
      try {
          $pdo = new PDO("mysql:host=sql313.infinityfree.com;dbname=if0_38041735_gts_website", "if0_38041735", "zLyW2sLuCxL");
          $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
          
          $sql = "SELECT * FROM `games`";
          $stmt = $pdo->prepare($sql);
          $stmt->execute();
          $games = $stmt->fetchAll(PDO::FETCH_ASSOC);
          
          if (count($games) > 0) {
              echo "<table>";
              echo "<tr><th>ID</th><th>游戏名称</th><th>描述</th><th>下载链接</th><th>上传时间</th></tr>";
              
              foreach ($games as $game) {
                  echo "<tr>";
                  echo "<td>" . htmlspecialchars($game['id']) . "</td>";
                  echo "<td>" . htmlspecialchars($game['name']) . "</td>";
                  echo "<td>" . htmlspecialchars($game['description']) . "</td>";
                  echo "<td><a class='download-link' href='" . htmlspecialchars($game['download_link']) . "' target='_blank'>下载</a></td>";
                  echo "<td>" . htmlspecialchars($game['created_at']) . "</td>";
                  echo "</tr>";
              }
              
              echo "</table>";
          } else {
              echo "<p style='text-align: center;'>暂无游戏数据</p>";
          }
      } catch (PDOException $e) {
          echo "<p style='text-align: center; color: red;'>数据库连接失败: " . $e->getMessage() . "</p>";
      }
      ?>
</body>
</html>