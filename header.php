<?php
session_start();
?>
<!DOCTYPE html>
<html lang="<?php echo (isset($is_pt_page) && $is_pt_page) ? 'pt' : 'en'; ?>">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $pageTitle ?? 'File Organizer - Smart File Organization'; ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
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
        <nav class="navbar navbar-expand-lg">
            <div class="container">
                <a class="navbar-brand" href="https://odsantos.com">Home</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#responsive-navbar-nav" aria-controls="responsive-navbar-nav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="responsive-navbar-nav">
                    <ul class="navbar-nav ms-auto">
                        <!-- Original odsantos.com links (if applicable, can be customized) -->
                        <li class="nav-item"><a class="nav-link" href="https://odsantos.com/index.php#about">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="https://odsantos.com/index.php#projects">Projects</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.php">Contact</a></li>
                        <!-- Language Switcher -->
                        <li class="nav-item ms-3">
                            <div class="language-switcher-links">
                                <a href="/?lang=en">En 🇬🇧</a>&nbsp; | &nbsp;<a href="/ao/?lang=pt">Pt 🇦🇴</a>
                            </div>
                        </li>
                        <li class="nav-item ms-3 d-flex align-items-center">
                            <button id="theme-switcher" class="btn theme-switcher-btn" aria-label="Toggle theme">
                                🌙
                            </button>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="banner-container">
            <img src="/assets/images/file-organizer-2586-720.jpeg" alt="File Organizer Banner">
        </div>
    </header>