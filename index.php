<?php

// Set language
if (isset($_GET['lang']) && $_GET['lang'] == 'pt') {
    header('Location: /ao/');
    exit();
}

$pageTitle = "File Organizer - Smart File Organization";
include 'header.php';
?>



    <section class="hero-intro">
        <div class="container">
            <h2>Tidy Up Your Files Instantly</h2>
            <p>A simple utility to automatically organize your files and folders into clean, type-based subdirectories.</p>
            <a href="https://osvaldosantos.gumroad.com/l/file-organizer" class="cta-button">Purchase on Gumroad</a>
        </div>
    </section>

    <main class="container">

        <section id="features">
            <h2>Why You'll Love It</h2>
            <div class="features-grid">
                <div class="feature">
                    <h3>Easy-to-Use Interface</h3>
                    <p>A simple and clean graphical user interface (GUI) that's intuitive for everyone.</p>
                </div>
                <div class="feature">
                    <h3>Standalone Executables</h3>
                    <p>No need to install Python or any other dependencies. Just download and run on Windows, macOS, or Linux.</p>
                </div>
                <div class="feature">
                    <h3>Smart Conflict Resolution</h3>
                    <p>Automatically renames files if a file with the same name already exists in the destination folder.</p>
                </div>
            </div>
        </section>

        <section id="before-after">
            <h2>See the Transformation</h2>
            
            <div class="comparison-grid">
                <div class="comparison-item">
                    <h3>Before</h3>
                    <img src="assets/images/before-organizing.png" alt="A messy folder with mixed file types">
                    <p>A chaotic mix of documents, images, and archives.</p>
                </div>
                <div class="comparison-item">
                    <h3>After</h3>
                    <img src="assets/images/after-organizing.png" alt="An organized folder with subdirectories for each file type">
                    <p>Perfectly organized into type-based subfolders.</p>
                </div>
            </div>
        </section>

        <section id="how-it-works">
            <h2>How It Works in 3 Simple Steps</h2>

            <!-- STEP 1 -->
            <div class="step">
                <div class="step-text">
                    <h3>1. Select a Directory</h3>
                    <p>Click the <strong>"Browse..."</strong> button to choose any folder on your computer that you want to tidy up. The app defaults to your "Downloads" folder for convenience.</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/select-directory.png" alt="Main application window of File Organizer">
                </div>
            </div>

            <!-- STEP 2 -->
            <div class="step">
                <div class="step-text">
                    <h3>2. Confirm the Action</h3>
                    <p>Click the <strong>"Organize Files"</strong> button. A confirmation prompt appears to ensure you don't organize a folder by accident. This is your safety check!</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/confirm-dialog.png" alt="Confirmation prompt before organizing files">
                </div>
            </div>

            <!-- STEP 3 -->
            <div class="step">
                <div class="step-text">
                    <h3>3. See the Magic!</h3>
                    <p>The script instantly moves your files into neatly organized subfolders based on their type (e.g., 'PDF Files', 'JPG Files'). A log shows you exactly what was moved.</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/completion-log.png" alt="Completion log showing moved files">
                </div>
            </div>

            <!-- BONUS STEP -->
            <div class="step">
                <div class="step-text">
                    <h3>Built-in Help</h3>
                    <p>Confused? Just click the <strong>"Instructions"</strong> button to get a clear, step-by-step guide right within the app.</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/instructions-popup.png" alt="Instructions pop-up">
                </div>
            </div>

        </section>

        <section id="local-trust" style="background: #f8f9fa; padding: 40px 20px; text-align: center; border-radius: 8px; margin: 40px 0;">
            <div class="container">
                <h2>Data Privacy</h2>
                <p>This software caters to the organizational needs of local professionals and ensures the privacy of your data, as it processes everything locally on your computer.</p>
            </div>
        </section>

        <section id="developer" style="margin-bottom: 30px;">
            <div class="container">
                <h2>View on GitHub</h2>
                <p>The project, containing the source code and license, is available for review.</p>
                <a href="https://github.com/odsantos/file-organizer-script" class="cta-button">View Repository</a>
            </div>
        </section>

    </main>

    <?php include 'footer.php'; ?>
    