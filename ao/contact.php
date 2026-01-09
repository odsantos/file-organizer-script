<?php
$is_pt_page = true;
$pageTitle = "Contacto - Organizador de Ficheiros"; include '../header.php'; ?>
<div class="hero-intro">
    <div class="container">
        <h1>Contacte-nos</h1>
        <p>Por favor, use o formulário abaixo para entrar em contacto connosco sobre o Organizador de Ficheiros. Responderemos o mais breve possível.</p>
    </div>
</div>

<main class="container">
    <?php
    if (isset($_GET['status'])) {
        if ($_GET['status'] == 'success') {
            echo '<p style="color: green;">Mensagem enviada com sucesso!</p>';
        } else if ($_GET['status'] == 'error') {
            $msg = isset($_GET['msg']) ? $_GET['msg'] : '';
            if ($msg == 'invalid_input') {
                echo '<p style="color: red;">Por favor, preencha todos os campos correctamente.</p>';
            } else if ($msg == 'mail_failed') {
                echo '<p style="color: red;">Ocorreu um erro ao enviar a sua mensagem. Por favor, tente novamente mais tarde.</p>';
            }
        }
    }
    ?>
    <form action="../process_contact.php" method="POST">
        <label for="name">Nome:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="subject">Assunto:</label><br>
        <input type="text" id="subject" name="subject" required><br><br>

        <label for="message">Mensagem:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <!-- Basic Honeypot for spam prevention -->
        <div style="display:none;">
            <label for="hp_field">Não preencha isto se for humano:</label>
            <input type="text" name="hp_field" id="hp_field">
        </div>

        <input type="submit" value="Enviar Mensagem">
    </form>
</main>
<?php include '../footer.php'; ?>
