<?php
$is_pt_page = true;
$pageTitle = "Política de Privacidade - Organizador de Ficheiros"; 
include '../header.php'; ?>
<div class="hero-intro">
    <div class="container">
        <h1>Política de Privacidade</h1>
        <p>A sua privacidade é primordial. Esta política explica como lidamos com os seus dados.</p>
    </div>
</div>

<main class="container privacy-container">
    <h2>Execução Local</h2>
    <p>O Organizador de Ficheiros é uma aplicação de cliente. <strong>Não temos acesso aos seus ficheiros.</strong> Todas as tarefas de organização são realizadas localmente no seu computador. Nenhum metadado, nome ou conteúdo de ficheiro é transmitido para os nossos servidores.</p>

    <h2>Informações que Recolhemos</h2>
    <p>O site utiliza análises web padrão (Microsoft Clarity) para compreender padrões de tráfego. Estes dados não são pessoalmente identificáveis. Apenas recolhemos informações pessoais (como o seu e-mail) se utilizar voluntariamente o formulário de contacto.</p>

    <h2>Transparência de IA</h2>
    <p>Embora a lógica do software tenha sido desenvolvida com assistência de IA (Gemini), o software em si não contém mecanismos de rastreio ou "aprendizagem" de IA que reportem o comportamento do utilizador.</p>

    <p><em>Última atualização: <?php 
        $formatter = new IntlDateFormatter('pt_PT', IntlDateFormatter::LONG, IntlDateFormatter::NONE);
        echo $formatter->format(time()); 
    ?></em></p>
</main>
<?php include '../header.php'; ?>
