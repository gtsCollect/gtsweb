<?php
// list.php - 小说章节列表页面
if (!isset($_GET['novel']) || empty($_GET['novel'])) {
    die('无效的小说名称');
}

$novelName = $_GET['novel'];
$writer = $_GET['writer'] ?? '';
$novelDir = "小说/" . $novelName;

// 安全检查，防止路径遍历攻击
if (!is_dir($novelDir) || strpos($novelName, '..') !== false || strpos($novelName, '/') !== false) {
    die('小说不存在');
}

// 获取小说目录下的所有文件
$files = array();
if (is_dir($novelDir)) {
    $dirContents = scandir($novelDir);
    foreach ($dirContents as $item) {
        if ($item === '.' || $item === '..' || $item === "info.json") continue;
        
        $itemPath = $novelDir . '/' . $item;
        if (is_file($itemPath)) {
            $files[] = array(
                'name' => $item,
                'path' => $item
            );
        }
    }
}
?>
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($novelName); ?> - 章节列表</title>
    <style>
        body {
            font-family: "Microsoft YaHei", Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        
        .header {
            text-align: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #ddd;
        }
        
        .chapter-list {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .back-link {
            display: inline-block;
            margin-bottom: 20px;
            color: #007cba;
            text-decoration: none;
        }
        
        .back-link:hover {
            text-decoration: underline;
        }
        
        .chapter-list ul {
            list-style-type: none;
            padding: 0;
        }
        
        .chapter-list li {
            padding: 10px;
            border-bottom: 1px solid #eee;
        }
        
        .chapter-list li:last-child {
            border-bottom: none;
        }
        
        .chapter-list a {
            color: #007cba;
            text-decoration: none;
            font-size: 16px;
        }
        
        .chapter-list a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1><?php echo htmlspecialchars($novelName); ?> - 章节列表 - 作者- <?php echo htmlspecialchars($writer); ?></h1>
    </div>
    
    <a href="novel.php" class="back-link">&laquo; 返回小说列表</a>
    
    <div class="chapter-list">
        <?php if (!empty($files)): ?>
            <ul>
                <?php foreach ($files as $file): ?>
                    <li>
                        <a href="<?php echo htmlspecialchars("小说/" . rawurlencode($novelName) . "/" . rawurlencode($file['path'])); ?>">
                            <?php
                                $path = $_GET['path'];
                                echo "<a href='viewer.php?path=$path&novel=" . rawurlencode($file['path']) . "'>" . htmlspecialchars($file['name']) . "</a>"
                            ?>
                        </a>
                    </li>
                <?php endforeach; ?>
            </ul>
        <?php else: ?>
            <p>该小说目录下暂无章节文件。</p>
        <?php endif; ?>
    </div>
</body>
</html>