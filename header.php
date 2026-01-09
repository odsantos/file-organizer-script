<!DOCTYPE html>
<html lang="<?php echo (isset($is_pt_page) && $is_pt_page) ? 'pt' : 'en'; ?>">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $pageTitle ?? 'File Organizer'; ?></title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="apple-touch-icon" sizes="180x180" href="/assets/images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/images/favicon-16x16.png">

    <!-- Open Graph Meta Tags for Social Media Sharing -->
    <meta property="og:title" content="<?php echo $pageTitle ?? 'File Organizer - Smart File Organization'; ?>">
    <meta property="og:description" content="A simple utility to automatically organize your files and folders into clean, type-based subdirectories.">
    <meta property="og:image" content="https://fileorganizer.odsantos.com/assets/images/file-organizer-1200-630.png">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://fileorganizer.odsantos.com/">
    <script defer src="/assets/js/accordion.js"></script>
    <script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "uwvqs96twr");
</script>
</head>
<body>
    <header>
       <nav>
        <div>
            <a href="/">Home</a>
        </div>
        <div>
            <a href="/?lang=en">En 🇬🇧</a>
            <a href="/ao/?lang=pt">Pt 🇦🇴</a>
        </div>
    </nav>
        <img src="/assets/images/file-organizer-2586-720.jpeg" alt="File Organizer Banner">
    </header>
