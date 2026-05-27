const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if(menuBtn){
    menuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
}


// Resume Modal

const openModal = document.getElementById('openModal');
const closeModal = document.getElementById('closeModal');
const resumeModal = document.getElementById('resumeModal');
const resumeForm = document.getElementById('resumeForm');

if(openModal){

    openModal.addEventListener('click', () => {
        resumeModal.classList.remove('hidden');
        resumeModal.classList.add('flex');
    });

}

if(closeModal){

    closeModal.addEventListener('click', () => {
        resumeModal.classList.add('hidden');
    });

}


// Resume Download

if(resumeForm){

    resumeForm.addEventListener('submit', function(e){

        e.preventDefault();

        // Download Resume

        const link = document.createElement('a');

        link.href = "/static/resume/Mohit_Sardana_Resume.pdf";

        link.download = "Mohit_Sardana_Resume.pdf";

        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);

        // Close Modal

        resumeModal.classList.add('hidden');

    });

}