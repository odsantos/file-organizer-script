<?php
$pageTitle = "Contact Us - File Organizer";
include 'header.php';

// Generate CSRF token if it doesn't exist
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
?>
<div class="hero-intro">
    <div class="container">
        <h1>Contact Us</h1>
        <p>Please use the form below to get in touch with us regarding File Organizer. We'll get back to you as soon as possible.</p>
    </div>
</div>

<main class="container">
    <?php
    if (isset($_GET['status'])) {
        if ($_GET['status'] == 'success') {
            echo '<p style="color: green;">Message sent successfully!</p>';
        } else if ($_GET['status'] == 'error') {
            $msg = isset($_GET['msg']) ? $_GET['msg'] : '';
            if ($msg == 'invalid_input') {
                echo '<p style="color: red;">Please fill out all fields correctly.</p>';
            } else if ($msg == 'mail_failed') {
                echo '<p style="color: red;">An error occurred while sending your message. Please try again later.</p>';
            } else if ($msg == 'invalid_token') {
                echo '<p style="color: red;">Invalid request. Please try submitting the form again.</p>';
            }
        }
    }
    ?>
    <form action="process_contact.php" method="POST">
        <input type="hidden" name="csrf_token" value="<?php echo $_SESSION['csrf_token']; ?>">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="subject">Subject:</label><br>
        <input type="text" id="subject" name="subject" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <!-- Basic Honeypot for spam prevention -->
        <div style="display:none;">
            <label for="hp_field">Don't fill this out if you're human:</label>
            <input type="text" name="hp_field" id="hp_field">
        </div>

        <input type="submit" value="Send Message">
    </form>
</main>
<?php include 'footer.php'; ?>
