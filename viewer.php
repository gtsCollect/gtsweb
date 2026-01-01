<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo isset($_GET['novel']) ? htmlspecialchars($_GET['novel']) : '小说阅读器'; ?> - 小说阅读器</title>
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
</head>
<body>
    <?php
    // 从path参数中获取文件路径
    $path = $_GET['path'] ?? '';
    $novelName = basename($path, '.txt'); // 从路径中获取文件名（假设是.txt文件）
    
    // 安全检查，防止路径遍历攻击
    if (strpos($path, '..') !== false || !file_exists($path)) {
        die('文件不存在或路径无效');
    }
    ?>
    <div class="header">
        <h1><?php echo htmlspecialchars($novelName); ?></h1>
    </div>
    
    <a href="novel.php" class="back-link">&laquo; 返回小说列表</a>
    
    <div class="bookmarkControls">
        <button class="bookmarkButton" onclick="save_bookmark()">保存书签</button>
        <button class="bookmarkButton" onclick="load_bookmark()">加载书签</button>
        <button class="bookmarkButton" onclick="clear_bookmark()">清除书签</button>
    </div>
    
    <div id="reader-container">
        <div class="novel-content">
            <?php
            // 读取并显示文件内容
            if (!empty($path) && file_exists($path)) {
                $content = file_get_contents($path);
                echo nl2br(htmlspecialchars($content));
            } else {
                echo "<p>无法读取小说内容</p>";
            }
            ?>
        </div>
    </div>
    <!-- <script src="js/novel_reader.js"></script> -->
    <script src="js/localforage.min.js"></script>
    <script>
    // 引入推荐的库: epubjs 用于处理电子书内容, localforage 用于存储书签
// 通过CDN或npm安装: epubjs, localforage
// 保存书签
function save_bookmark() {
    // 获取当前阅读位置
    const currentPos = getCurrentPosition();
    // 获取当前小说路径
    const novelPath = "<?php echo $path; ?>";
    // 使用localForage保存书签到本地存储，以小说路径为键
    localforage.setItem('novel_bookmark_' + novelPath, {
        url: window.location.href,
        position: currentPos,
        timestamp: Date.now(),
        novelName: "<?php echo htmlspecialchars($novelName); ?>"
    }).then(() => {
        console.log('书签已保存');
    }).catch(err => {
        console.error('保存书签失败:', err);
    });
}

// 加载书签
function load_bookmark() {
    const novelPath = "<?php echo $path; ?>";
    localforage.getItem('novel_bookmark_' + novelPath).then(bookmark => {
        if (bookmark) {
            // 如果书签是当前页面的，则滚动到之前的位置
            window.scrollTo(0, bookmark.position || 0);
        }
    }).catch(err => {
        console.error('读取书签失败:', err);
    });
}

function clear_bookmark() {
    const novelPath = "<?php echo $path; ?>";
    // 清除当前小说的书签
    localforage.removeItem('novel_bookmark_' + novelPath)
        .then(() => {
            console.log('书签已清除');
        })
        .catch(err => {
            console.error('清除书签失败:', err);
        });
}

// 获取当前位置的辅助函数
function getCurrentPosition() {
    return window.pageYOffset || document.documentElement.scrollTop;
}

// 添加滚动事件监听器，用于自动保存阅读进度
window.addEventListener('scroll', () => {
    // 可以设置节流来避免过于频繁的保存
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(save_bookmark, 1000); // 滚动停止1秒后保存
});

let scrollTimer;

// 页面加载完成后初始化书签功能
document.addEventListener('DOMContentLoaded', function() {
    // 从页面内容中获取当前位置
    load_bookmark();
});
    </script>
</body>
</html>