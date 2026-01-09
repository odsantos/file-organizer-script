    <footer>
        <nav>
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
    </footer>
</body>
</html>

