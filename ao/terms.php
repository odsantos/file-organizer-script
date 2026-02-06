<?php
$is_pt_page = true;
$pageTitle = "Termos de Serviço - Organizador de Ficheiros";
include '../header.php';
?>
<div class="hero-intro">
    <div class="container">
        <h1>Termos de Serviço</h1>
        <p>Informações legais sobre o uso do Organizador de Ficheiros.</p>
    </div>
</div>

<main class="container terms-container">
    <h2>Licença</h2>
    <p>O Organizador de Ficheiros é um software de código aberto licenciado sob a <strong>Licença MIT</strong>. Você é livre para usar, copiar e modificar o software, desde que o aviso de direitos de autor original e o aviso de permissão sejam incluídos em todas as cópias ou partes substanciais do software.</p>

    <h2>Colaboração de IA</h2>
    <p>Este projeto foi desenvolvido através de um processo colaborativo entre Osvaldo Santos e Gemini (Google AI). A titularidade e a responsabilidade pela implementação final permanecem com o autor.</p>

    <h2>Isenção de Garantias</h2>
    <p>O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM FIM ESPECÍFICO E NÃO INFRAÇÃO. EM NENHUM CASO OS AUTORES SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE.</p>

    <p><em>Última atualização: <?php 
    $formatter = new IntlDateFormatter(
        'pt_PT', 
        IntlDateFormatter::LONG, 
        IntlDateFormatter::NONE
    );
    echo $formatter->format(time()); 
?></em></p>
</main>
<?php include '../footer.php'; ?>
