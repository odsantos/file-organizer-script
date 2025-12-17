document.addEventListener('DOMContentLoaded', function() {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const clickedQuestion = this;
            const clickedAnswer = clickedQuestion.nextElementSibling;

            // Close all other open FAQs
            faqQuestions.forEach(otherQuestion => {
                if (otherQuestion !== clickedQuestion && otherQuestion.classList.contains('active')) {
                    otherQuestion.classList.remove('active');
                    const otherAnswer = otherQuestion.nextElementSibling;
                    otherAnswer.classList.remove('open');
                    otherAnswer.style.maxHeight = 0;
                }
            });

            // Toggle the clicked FAQ
            clickedQuestion.classList.toggle('active');
            if (clickedAnswer.classList.contains('open')) {
                clickedAnswer.classList.remove('open');
                clickedAnswer.style.maxHeight = 0;
            } else {
                clickedAnswer.classList.add('open');
                clickedAnswer.style.maxHeight = clickedAnswer.scrollHeight + 'px'; // Set max-height for smooth transition
            }
        });
    });
});