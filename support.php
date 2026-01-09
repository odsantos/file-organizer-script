<?php $pageTitle = "Support - File Organizer"; include 'header.php'; ?>
<div class="hero-intro">
    <div class="container">
        <h1>Support for File Organizer</h1>
        <p>If you have any questions or encounter issues with File Organizer, please check the following resources:</p>
    </div>
</div>

<main class="container">
    <h2>Frequently Asked Questions (FAQ)</h2><div class="faq-item"><h3 class="faq-question">Q: What is File Organizer?</h3>
<div class="faq-answer">
<p>A: File Organizer is a desktop application designed to automatically organize files in a chosen directory into type-based subfolders (e.g., 'PDF Files', 'JPG Files', 'ZIP Files').</p></div></div>

<div class="faq-item"><h3 class="faq-question">Q: How do I install File Organizer?</h3>
<div class="faq-answer">
<p>A: For most users, simply download the executable from our <a href="https://osvaldosantos.gumroad.com/l/file-organizer" class="regular-link">Gumroad page</a>, and run the application. Specific instructions vary slightly by operating system:</p>
<ul>
    <li><strong>Windows/macOS:</strong> Unzip the downloaded file.</li>
    <li><strong>Windows:</strong> Double-click <code>File Organizer.exe</code>.</li>
    <li><strong>macOS:</strong> Open the <code>File Organizer.app</code> directory. You might need to right-click and select "Open" the first time to bypass security warnings.</li>
    <li><strong>Linux:</strong> Make the AppImage executable (<code>chmod +x File-Organizer-Linux.AppImage</code>), and run it (<code>./File-Organizer-Linux.AppImage</code>).</li>
</ul>
</div></div>

<div class="faq-item"><h3 class="faq-question">Q: How do I use File Organizer?</h3>
<div class="faq-answer">
<p>A: It's straightforward:</p>
<ol>
    <li>Click the "Browse..." button to select the folder you wish to organize.</li>
    <li>Click the "Organize Files" button to begin the sorting process.</li>
    <li>A confirmation message will appear, detailing the files that were moved.</li>
</ol>
</div></div>

<div class="faq-item"><h3 class="faq-question">Q: What happens if a file with the same name already exists in the destination folder?</h3>
<div class="faq-answer">
<p>A: File Organizer includes smart conflict resolution. If a file with the same name exists, it will automatically rename the new file to prevent overwriting (e.g., <code>document.pdf</code> might become <code>document (1).pdf</code>).</p></div></div>

<div class="faq-item"><h3 class="faq-question">Q: Is it safe to use File Organizer?</h3>
<div class="faq-answer">
<p>A: Yes, it is safe. However, as with any tool that modifies your file system, we recommend exercising caution. Always double-check the selected directory before initiating the organization process. The application only moves files within the chosen directory and its newly created subfolders; it does not delete files or access other parts of your system.</p></div></div>

<div class="faq-item"><h3 class="faq-question">Q: My macOS warns about an "unidentified developer." What should I do?</h3>
<div class="faq-answer">
<p>A: This is a common security measure for applications not downloaded from the App Store. Right-click the <code>File Organizer.app</code>, select "Open," and then confirm your decision in the dialog box. This usually only needs to be done once.</p></div></div>

<div class="faq-item"><h3 class="faq-question">Q: Can I organize specific file types only?</h3>
<div class="faq-answer">
<p>A: Currently, File Organizer sorts all recognized file types in the selected directory. Future updates may include options for more granular control over which file types to organize.</p></div></div>

<div class="faq-item"><h3 class="faq-question">Q: What if my files aren't moving or the application isn't responding?</h3>
<div class="faq-answer">
<p>A: Please ensure you have selected a valid directory and that you have the necessary permissions to modify files within that directory. If the issue persists, try restarting the application. For further assistance, please use our <a href="contact.php" class="regular-link">contact form</a>.</p>
</div>
</div>
    <h2>Contact Us</h2>
    <p>If you cannot find an answer in the FAQ, please use our contact form for assistance.</p>
    <p><a href="contact.php" class="regular-link">Go to Contact Form</a></p>
</main>
<?php include 'footer.php'; ?>
