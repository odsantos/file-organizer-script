</main>
    <footer class="bg-dark text-white mt-3 p-3 text-center">
        <div class="container">            <nav>
                <?php
                // Determine base path and translations for the footer based on a variable set by the parent page
                $is_pt_footer = (isset($is_pt_page) && $is_pt_page === true);

                // Base path for links: /ao for Portuguese, empty for English
                $base_path_footer = $is_pt_footer ? '/ao' : '';

                // Translated link texts
                $support_text = $is_pt_footer ? 'Suporte' : 'Support';
                $privacy_text = $is_pt_footer ? 'Privacidade' : 'Privacy';
                $terms_text = $is_pt_footer ? 'Termos' : 'Terms';
                ?>
                <a href="<?php echo $base_path_footer; ?>/support.php"><?php echo $support_text; ?></a> |
                <a href="<?php echo $base_path_footer; ?>/privacy.php"><?php echo $privacy_text; ?></a> |
                <a href="<?php echo $base_path_footer; ?>/terms.php"><?php echo $terms_text; ?></a>
            </nav>
            <p>&copy; 2024-<?php echo date("Y"); ?> Osvaldo Santos | Licensed under MIT</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script>
        const themeSwitcher = document.getElementById('theme-switcher');
        const body = document.body;

        // Apply saved theme on load
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            body.classList.add('dark-theme');
            themeSwitcher.textContent = '☀️';
        } else {
            themeSwitcher.textContent = '🌙';
        }

        themeSwitcher.addEventListener('click', () => {
            body.classList.toggle('dark-theme');
            const isDarkMode = body.classList.contains('dark-theme');
            themeSwitcher.textContent = isDarkMode ? '☀️' : '🌙';
            localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
        });
    </script>
</body>
</html>