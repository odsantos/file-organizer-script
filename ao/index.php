<?php
// Since this page is in the /ao/ directory, we set a variable to declare it as a Portuguese page.
$is_pt_page = true;

$pageTitle = "Organizador de Arquivos - Organização Inteligente para Profissionais";
include '../header.php';
?>



    <section class="hero-intro">
        <div class="container">
            <h1>Organização Digital para Profissionais</h1>
            <p>Pare de perder tempo à procura de documentos. Organize milhares de processos jurídicos, faturas e arquivos de clientes instantaneamente com apenas um clique.</p>
            <a href="https://osvaldosantos.gumroad.com/l/file-organizer" class="cta-button">Comprar Agora - Acesso Vitalício</a>
        </div>
    </section>

    <main class="container">

        <section id="features">
            <h2>Por que escolher o File Organizer?</h2>
            <div class="features-grid">
                <div class="feature">
                    <h3>Interface Simples e Intuitiva</h3>
                    <p>Desenhado para ser fácil. Não precisa de conhecimentos técnicos para organizar as suas pastas em segundos.</p>
                </div>
                <div class="feature">
                    <h3>Sem Necessidade de Instalação</h3>
                    <p>Funciona de forma independente no Windows, macOS ou Linux. Basta descarregar e executar.</p>
                </div>
                <div class="feature">
                    <h3>Segurança com Arquivos Duplicados</h3>
                    <p>O sistema renomeia automaticamente arquivos com o mesmo nome para garantir que nunca perca nenhuma informação importante.</p>
                </div>
            </div>
        </section>

        <section id="before-after">
            <h2>Transforme a sua Área de Trabalho</h2>
            <p class="center-text">Veja como o script limpa a sua pasta "Downloads" ou pastas de projetos em segundos.</p>
            <div class="comparison-grid">
                <div class="comparison-item">
                    <h3>Antes</h3>
                    <img src="assets/images/before-organizing.png" alt="Pasta desorganizada com muitos arquivos">
                    <p>Uma mistura caótica de documentos, imagens e arquivos.</p>
                </div>
                <div class="comparison-item">
                    <h3>Depois</h3>
                    <img src="assets/images/after-organizing.png" alt="Pasta organizada com subpastas por tipo">
                    <p>Perfeitamente organizada em subpastas baseadas no tipo.</p>
                </div>
            </div>
        </section>

        <section id="how-it-works">
            <h2>Como Funciona?</h2>
            <div class="step">
                <div class="step-text">
                    <h3>1. Escolha a Pasta</h3>
                    <p>Abra o aplicativo e selecione a pasta que deseja organizar (ex: Downloads, Documentos ou Pastas de Clientes).</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/select-directory.png" alt="Selecionar diretório no aplicativo">
                </div>
            </div>

            <div class="step">
                <div class="step-text">
                    <h3>2. Clique em Organizar</h3>
                    <p>Confirme a ação. O script irá analisar cada extensão de arquivo individualmente.</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/confirm-dialog.png" alt="Diálogo de confirmação">
                </div>
            </div>

            <div class="step">
                <div class="step-text">
                    <h3>3. Magia Instantânea!</h3>
                    <p>Os seus arquivos são movidos para subpastas organizadas (ex: 'Arquivos PDF', 'Imagens JPG'). Um relatório final mostra tudo o que foi feito.</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/completion-log.png" alt="Log de conclusão">
                </div>
            </div>

            <!-- PASSO BÓNUS -->
            <div class="step">
                <div class="step-text">
                    <h3>Ajuda Integrada</h3>
                    <p>Confuso? Basta clicar no botão <strong>"Instruções"</strong> para obter um guia claro e passo a passo diretamente na aplicação.</p>
                </div>
                <div class="step-img">
                    <img src="assets/images/instructions-popup.png" alt="Pop-up de instruções">
                </div>
            </div>
        </section>

        <section id="local-trust" style="background: #f8f9fa; padding: 40px 20px; text-align: center; border-radius: 8px; margin: 40px 0;">
            <div class="container">
                <h2>Privacidade de dados</h2>
                <p>Este software atende às necessidades de organização de profissionais locais e garante a privacidade dos seus dados, pois processa tudo localmente no seu computador.</p>
            </div>
        </section>

        <section id="developer" style="margin-bottom: 30px;">
            <div class="container">
                <h2>Ver no GitHub</h2>
                <p>O projeto, contendo o código-fonte e a licença, está disponível para consulta.</p>
                <a href="https://github.com/odsantos/file-organizer-script" class="cta-button">Ver Repositório</a>
            </div>
        </section>

    </main>

<?php include '../footer.php'; ?>
