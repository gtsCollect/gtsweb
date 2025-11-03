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
    <p>加密的文章需要使用 <a href="https://www.sojson.com/encrypt.html#google_vignette">这个网站</a>解密（复制文章内容搞进去，再复制密钥进行解密）这是为了防审查</p>
    <p>注：一间昏暗的密室内 一名巨大的魔族少女双腿敞开 这篇小说需要使用解密查看 (1),加密方法（AES）密钥S6Cs5vU3TAJdPG5c6yD4</p>
    <ol>
    <?php
    /*$lis = gen_novel_list("小说");
    for($i = 0; $i < count($lis); $i++) {
        echo "<li><a href='" . htmlspecialchars($lis[$i]) . "'>" . htmlspecialchars(urldecode(basename($lis[$i]))) . "</a></li>";
    }*/
    // 使用gen_novel_list2函数生成小说列表
    gen_novel_list_2("小说");
    ?>
    <!-- <li><a href="小说/娜娜变大记/index.php">娜娜变大记-番茄小说</a></li>
    <li><a href="小说/爱转校的千雪大小姐/index.php">爱转校的千雪大小姐</a></li>
    <li><a href="小说/mc/index.php">mc</a></li> -->
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
    // 一个遍历小说文件夹每个文件夹下的所有文件的函数
    function gen_novel_list_2($dir)
    {
        if (is_dir($dir)) {
            $files = scandir($dir);
            
            if ($files !== false) {
                foreach ($files as $file) {
                    if ($file === '.' || $file === '..') continue;
                    
                    $filePath = $dir . '/' . $file;
                    
                    // 检查是否为目录（小说目录）
                    if (is_dir($filePath)) {
                        $encodedDir = implode('/', array_map('rawurlencode', explode('/', $dir)));
                        $encodedFile = rawurlencode($file);
                        // 指向统一的小说查看器，传递小说名称参数
                        $viewerPath = 'viewer.php?novel=' . $encodedFile;
                        // 输出HTML列表项
                        echo "<li><a href='" . htmlspecialchars($viewerPath) . "'>" . htmlspecialchars($file) . "</a></li>";
                        /*$indexFile = $filePath . '/index.php';
                        
                        if (is_file($indexFile)) {
                            // 处理中文路径编码
                            $encodedDir = implode('/', array_map('rawurlencode', explode('/', $dir)));
                            $encodedFile = rawurlencode($file);
                            $encodedPath = $encodedDir . '/' . $encodedFile . '/index.php';
                            
                            // 输出HTML列表项
                            echo "<li><a href='" . htmlspecialchars($encodedPath) . "'>" . htmlspecialchars($file) . "</a></li>";
                        }*/
                    }
                    else{
                        $encodedDir = implode('/', array_map('rawurlencode', explode('/', $dir)));
                        $encodedFile = rawurlencode($file);
                        $encodedPath = $encodedDir . '/' . $encodedFile;
                        
                        // 输出HTML列表项
                        echo "<li><a href='" . htmlspecialchars($encodedPath) . "'>" . htmlspecialchars($file) . "</a></li>";
                    }
                }
            }
        }
    }
    ?>
</body>
</html>