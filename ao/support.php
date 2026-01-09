<?php
$is_pt_page = true;
$pageTitle = "Suporte - Organizador de Ficheiros"; include '../header.php'; ?>
<div class="hero-intro">
    <div class="container">
        <h1>Suporte para o Organizador de Ficheiros</h1>
        <p>Se tiver alguma dúvida ou encontrar problemas com o Organizador de Ficheiros, por favor, verifique os seguintes recursos:</p>
    </div>
</div>

<main class="container">
    <h2>Perguntas Frequentes (FAQ)</h2><div class="faq-item"><h3 class="faq-question">P: O que é o Organizador de Ficheiros?</h3>
<div class="faq-answer">
<p>R: O Organizador de Ficheiros é uma aplicação de desktop desenhada para organizar automaticamente ficheiros num diretório escolhido em subpastas baseadas no tipo (por exemplo, 'Ficheiros PDF', 'Ficheiros JPG', 'Ficheiros ZIP').</p></div></div>

<div class="faq-item"><h3 class="faq-question">P: Como instalo o Organizador de Ficheiros?</h3>
<div class="faq-answer">
<p>R: Para a maioria dos utilizadores, basta descarregar o executável da nossa <a href="https://osvaldosantos.gumroad.com/l/file-organizer" class="regular-link">página Gumroad</a> e executar a aplicação. As instruções específicas variam ligeiramente consoante o sistema operativo:</p>
<ul>
    <li><strong>Windows/macOS:</strong> Descompacte o ficheiro descarregado.</li>
    <li><strong>Windows:</strong> Faça duplo clique em <code>File Organizer.exe</code>.</li>
    <li><strong>macOS:</strong> Abra o diretório <code>File Organizer.app</code>. Poderá ter de clicar com o botão direito e selecionar "Abrir" na primeira vez para ignorar avisos de segurança.</li>
    <li><strong>Linux:</strong> Torne a AppImage executável (<code>chmod +x File-Organizer-Linux.AppImage</code>) e execute-a (<code>./File-Organizer-Linux.AppImage</code>).</li>
</ul>
</div></div>

<div class="faq-item"><h3 class="faq-question">P: Como uso o Organizador de Ficheiros?</h3>
<div class="faq-answer">
<p>R: É simples:</p>
<ol>
    <li>Clique no botão "Procurar..." para selecionar a pasta que deseja organizar.</li>
    <li>Clique no botão "Organizar Ficheiros" para iniciar o processo de ordenação.</li>
    <li>Uma mensagem de confirmação aparecerá, detalhando os ficheiros que foram movidos.</li>
</ol>
</div></div>

<div class="faq-item"><h3 class="faq-question">P: O que acontece se um ficheiro com o mesmo nome já existir na pasta de destino?</h3>
<div class="faq-answer">
<p>R: O Organizador de Ficheiros inclui uma resolução de conflitos inteligente. Se um ficheiro com o mesmo nome existir, ele irá renomear automaticamente o novo ficheiro para evitar a substituição (por exemplo, <code>documento.pdf</code> pode tornar-se <code>documento (1).pdf</code>).</p></div></div>

<div class="faq-item"><h3 class="faq-question">P: É seguro usar o Organizador de Ficheiros?</h3>
<div class="faq-answer">
<p>R: Sim, é seguro. No entanto, como com qualquer ferramenta que modifica o seu sistema de ficheiros, recomendamos que tenha cuidado. Verifique sempre o diretório selecionado antes de iniciar o processo de organização. A aplicação apenas move ficheiros dentro do diretório escolhido e das suas subpastas recém-criadas; não apaga ficheiros nem acede a outras partes do seu sistema.</p></div></div>

<div class="faq-item"><h3 class="faq-question">P: O meu macOS avisa sobre um "desenvolvedor não identificado". O que devo fazer?</h3>
<div class="faq-answer">
<p>R: Esta é uma medida de segurança comum para aplicações não descarregadas da App Store. Clique com o botão direito no <code>File Organizer.app</code>, selecione "Abrir" e, em seguida, confirme a sua decisão na caixa de diálogo. Normalmente, isto só precisa de ser feito uma vez.</p></div></div>

<div class="faq-item"><h3 class="faq-question">P: Posso organizar apenas tipos de ficheiros específicos?</h3>
<div class="faq-answer">
<p>R: Atualmente, o Organizador de Ficheiros ordena todos os tipos de ficheiros reconhecidos no diretório selecionado. Atualizações futuras podem incluir opções para um controlo mais granular sobre quais tipos de ficheiros organizar.</p></div></div>

<div class="faq-item"><h3 class="faq-question">P: E se os meus ficheiros não estiverem a ser movidos ou a aplicação não estiver a responder?</h3>
<div class="faq-answer">
<p>R: Por favor, certifique-se de que selecionou um diretório válido e que tem as permissões necessárias para modificar ficheiros nesse diretório. Se o problema persistir, tente reiniciar a aplicação. Para mais assistência, por favor, use o nosso <a href="contact.php" class="regular-link">formulário de contacto</a>.</p>
</div>
</div>
    <h2>Contacte-nos</h2>
    <p>Se não conseguir encontrar uma resposta no FAQ, por favor, use o nosso formulário de contacto para obter assistência.</p>
    <p><a href="contact.php" class="regular-link">Ir para o Formulário de Contacto</a></p>
</main>
<?php include '../footer.php'; ?>
