<?php
define("dir","img/");
define("dir1","星际级巨大娘");
$items = scandir(dir.dir1);
foreach($items as $item) {
    if($item == "." || $item == "..") continue;
    echo "<img src='".dir.dir1."/".$item."'/>";
}
?>