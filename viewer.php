<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo htmlspecialchars($novelName); ?> - 文件列表</title>
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
        
        /* .novel-content {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            min-height: 400px;
        } */
        
        .back-link {
            display: inline-block;
            margin-bottom: 20px;
            color: #007cba;
            text-decoration: none;
        }
        
        .back-link:hover {
            text-decoration: underline;
        }
    </style>
    <style>
        .bookmarkControls{
            position: fixed;
            top: 10px;
            right: 10px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 1000;
        }
        
        .bookmarkButton{
            padding: 8px 12px;
            background-color: #007cba;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }
        
        .bookmarkButton:hover{
            background-color: #005a87;
        }
    </style>
    <script src="js/localforage.min.js"></script>
    
</head>
<body>
    <?php
    $novelName = $_GET['novel'];
    $writer = $_GET['writer'] ?? '';
    $path = $_GET['path'];
    ?>
    <!-- list应该在列表页显示，而不是阅读器页面 -->
    <div class="header">
        <h1><?php echo htmlspecialchars($novelName); ?>  - 作者- <?php 
        if(isset($writer))
        {
            echo htmlspecialchars($writer);
        }
        else
        {
            echo "未知作者";
        }
        ?></h1>
    </div>
    
    <a href="novel.php" class="back-link">&laquo; 返回小说列表</a>
    
    <div class="bookmarkControls">
        <button class="bookmarkButton" onclick="save_bookmark()">保存书签</button>
        <button class="bookmarkButton" onclick="load_bookmark()">加载书签</button>
        <button class="bookmarkButton" onclick="clear_bookmark()">清除书签</button>
    </div>
    
    <div class="novel-content">
        <!-- viewer.php应该只显示小说内容，而不是列表页 -->
        <?php
            if(isset($_GET['novel']))
            {
                // echo file_get_contents("小说/".$_GET['novel']);
                echo file_get_contents($path);
            }
        ?>
    </div>
    <script src="js/novel_reader.js"></script>
</body>
</html>