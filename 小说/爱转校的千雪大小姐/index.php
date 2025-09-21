<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>爱转校的千雪大小姐</title>
</head>
<body>
    <ol>
    <?php
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