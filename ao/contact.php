<?php
session_start();
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
$is_pt_page = true;
$pageTitle = "Contacto - Organizador de Ficheiros";
include '../header.php';
?>
<div class="hero-intro mb-4">
    <div class="container">
        <h1>Contacte-nos</h1>
        <p>Por favor, use o formulário abaixo para entrar em contacto connosco sobre o Organizador de Ficheiros. Responderemos o mais breve possível.</p>
    </div>
</div>

<main class="container">
    <?php
    if (isset($_GET['status'])) {
        if ($_GET['status'] == 'success') {
            echo '<div class="alert alert-success">Mensagem enviada com sucesso!</div>';
        } else if ($_GET['status'] == 'error') {
            $msg = isset($_GET['msg']) ? $_GET['msg'] : '';
            $errorMessage = 'Ocorreu um erro. Por favor, tente novamente.';
            if ($msg == 'invalid_input') {
                $errorMessage = 'Por favor, preencha todos os campos corretamente.';
            } else if ($msg == 'mail_failed') {
                $errorMessage = 'Ocorreu um erro ao enviar a sua mensagem. Por favor, tente novamente mais tarde.';
            } else if ($msg == 'invalid_token') {
                $errorMessage = 'Pedido inválido. Por favor, tente enviar o formulário novamente.';
            } else if ($msg == 'privacy_not_accepted') {
                $errorMessage = 'Deve concordar com a política de privacidade para enviar a mensagem.';
            }
            echo '<div class="alert alert-danger">' . $errorMessage . '</div>';
        }
    }
    ?>
    <form action="../contact/process_contact.php" method="POST" class="contact-form">
        <input type="hidden" name="source" value="File Organizer AO">
        <input type="hidden" name="csrf_token" value="<?php echo $_SESSION['csrf_token']; ?>">
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

        <div class="mb-3 form-check">
            <input type="checkbox" name="privacy_consent" class="form-check-input" id="privacyConsent" required>
            <label class="form-check-label" for="privacyConsent">
                Concordo com a <a href="privacy.php" target="_blank">Política de Privacidade</a>.
            </label>
        </div>

        <input type="submit" value="Enviar Mensagem">
    </form>
</main>
<?php include '../footer.php'; ?>
