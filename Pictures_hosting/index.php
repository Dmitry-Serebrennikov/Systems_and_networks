<?php

$uri = $_SERVER['REQUEST_URI'];

$pdo = new PDO('mysql:host=localhost;dbname=cdn;charset=utf8', 'root', 'password');

$sql = $pdo->prepare('SELECT filename, server FROM files WHERE filename=:filename');
$sql->execute([
     'filename' => substr($uri, 1),
]);

$img = $sql->fetch();
if ($img) {
    http_response_code(301);
    header('Location: ' . 'http://' . $img['server'] . '.images.serebrennikov-dmitry.site' . $uri);
} else {
    http_response_code(404);
}