<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Determine the redirect path based on HTTP_REFERER to preserve language context
    $redirect_base_path = '/'; // Default to English root
    if (isset($_SERVER['HTTP_REFERER'])) {
        $referer_path = parse_url($_SERVER['HTTP_REFERER'], PHP_URL_PATH);
        if (strpos($referer_path, '/ao/') !== false) {
            $redirect_base_path = '/ao/';
        }
    }
    
    // CSRF token validation
    if (!isset($_POST['csrf_token']) || !hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
        header("Location: " . $redirect_base_path . "contact.php?status=error&msg=invalid_token");
        exit;
    }
    unset($_SESSION['csrf_token']);
    // Honeypot check
    if (!empty($_POST['hp_field'])) {
        // This is likely a bot, silently ignore
        header("Location: " . $redirect_base_path . "contact.php?status=success"); // Redirect to a success-like page to not alert bot
        exit;
    }

    // Privacy Policy Validation
    if (!isset($_POST['privacy_consent'])) {
        header("Location: " . $redirect_base_path . "contact.php?status=error&msg=privacy_not_accepted");
        exit;
    }
    
    // Sanitize and validate inputs
    $name = htmlspecialchars(trim($_POST["name"]), ENT_QUOTES, 'UTF-8');
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $subject = htmlspecialchars(trim($_POST["subject"]), ENT_QUOTES, 'UTF-8');
    $message = htmlspecialchars(trim($_POST["message"]), ENT_QUOTES, 'UTF-8');

    // Get and sanitize source
    $source = isset($_POST["source"]) ? htmlspecialchars(trim($_POST["source"]), ENT_QUOTES, 'UTF-8') : 'Unknown Source';

    // Basic validation
    if (empty($name) || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($subject) || empty($message)) {
        header("Location: " . $redirect_base_path . "contact.php?status=error&msg=invalid_input");
        exit;
    }

    // Set recipient email - USER NEEDS TO PROVIDE THIS for fileorganizer.odsantos.com
    $recipient = "contact@fileorganizer.odsantos.com";

    // Email headers
    $email_headers = "From: " . $name . " <" . $email . ">\r\n";
    $email_headers .= "Reply-To: " . $email . "\r\n";
    $email_headers .= "MIME-Version: 1.0\r\n";
    $email_headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Build the email content
    $email_content = "Name: " . $name . "\n";
    $email_content .= "Email: " . $email . "\n\n";
    $email_content .= "Subject: " . $subject . "\n\n";
    $email_content .= "Message:\n" . $message . "\n";

    // Send the email
    if (mail($recipient, "[" . $source . "] " . $subject, $email_content, $email_headers)) {
        header("Location: " . $redirect_base_path . "contact.php?status=success");
        exit;
    } else {
        header("Location: " . $redirect_base_path . "contact.php?status=error&msg=mail_failed");
        exit;
    }
} else {
    // Not a POST request, redirect to contact form
    // Determine the redirect path based on HTTP_REFERER (if available) or default
    $redirect_base_path = '/';
    if (isset($_SERVER['HTTP_REFERER'])) {
        $referer_path = parse_url($_SERVER['HTTP_REFERER'], PHP_URL_PATH);
        if (strpos($referer_path, '/ao/') !== false) {
            $redirect_base_path = '/ao/';
        }
    }
    header("Location: " . $redirect_base_path . "contact.php");
    exit;
}
?>