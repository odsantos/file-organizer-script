<?php
$pageTitle = "Contact Us - File Organizer";
include 'header.php';

// Set the source for the contact form
$form_source = 'File Organizer EN';

// Generate CSRF token if it doesn't exist
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}
?>
<link rel="stylesheet" href="https://odsantos.com/contact/contact_form.css">
<div class="hero-intro mb-4">
    <div class="container">
        <h1>Contact Us</h1>
        <p>Please use the form below to get in touch with us regarding File Organizer. We'll get back to you as soon as possible.</p>
    </div>
</div>

<main class="container">
    <?php
    if (isset($_GET['status'])) {
        if ($_GET['status'] == 'success') {
            echo '<div class="alert alert-success">Message sent successfully!</div>';
        } else if ($_GET['status'] == 'error') {
            $msg = isset($_GET['msg']) ? $_GET['msg'] : '';
            $errorMessage = 'An error occurred. Please try again.';
            if ($msg == 'invalid_input') {
                $errorMessage = 'Please fill out all fields correctly.';
            } else if ($msg == 'mail_failed') {
                $errorMessage = 'An error occurred while sending your message. Please try again later.';
            } else if ($msg == 'invalid_token') {
                $errorMessage = 'Invalid request. Please try submitting the form again.';
            }
            echo '<div class="alert alert-danger">' . $errorMessage . '</div>';
        }
    }

    // Include the centralized contact form using an absolute path to the main project's assets
    ?>
    <form action="contact/process_contact.php" method="POST" class="contact-form">
        <?php include '/home/odsaophq/public_html/contact/contact_form.php'; ?>
    </form>
</main>
<?php include 'footer.php'; ?>
