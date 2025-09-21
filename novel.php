<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>小说</title>
</head>
<body>
    <h2>小说</h2>
    <ol>
    <?php
    $lis = gen_novel_list("小说");
    for($i = 0; $i < count($lis); $i++) {
        echo "<li><a href='" . htmlspecialchars($lis[$i]) . "'>" . htmlspecialchars(urldecode(basename($lis[$i]))) . "</a></li>";
    }
    ?>
    <li><a href="小说/爱转校的千雪大小姐/index.php">爱转校的千雪大小姐</a></li>
    </ol>
    <h2>UnnamedAdventures.exe解包剧情代码</h2>
    <ol>
        <li><a href="data/UnnamedAdventures/script.rpy">script.rpy</a></li>
        <li><a href="data/UnnamedAdventures/futaba.rpy">futaba.rpy</a></li>
        <li><a href="data/UnnamedAdventures/akane_background.rpy">akane_background.rpy</a></li>
    </ol>
    <?php
    function gen_novel_list($dir)
    {   
        $result = array(); // 创建结果数组
        
        if (is_dir($dir)) {
            $files = scandir($dir);
            
            if ($files !== false) {
                foreach ($files as $file) {
                    if ($file === '.' || $file === '..') continue; 
                    
                    $filePath = $dir . '/' . $file;
                    
                    if (is_file($filePath)) {
                        // 处理中文路径编码
                        $encodedDir = implode('/', array_map('rawurlencode', explode('/', $dir)));
                        $encodedFile = rawurlencode($file);
                        $encodedPath = $encodedDir . '/' . $encodedFile;
                        
                        // 将路径添加到结果数组而不是直接输出
                        $result[] = $encodedPath;
                    }
                }
            }
        }
        
        return $result; // 返回数组
    }
    ?>
</body>
</html>