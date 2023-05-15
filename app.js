// console.clear();
credits();

/*--------------------------------------------------------------
TABLE OF CONTENTS
----------------------------------------------------------------
1.0 SET-UP
    1.1 FADERS
    1.2 DROPDOWNS
2.0 PAPERSSS
    2.1 DOM ELEMENTS
    2.2 VARIABLES
    2.3 FUNCTIONS
    2.4 EVENT LISTENERS
--------------------------------------------------------------*/

/*--------------------------------------------------------------
1.0 SET-UP
--------------------------------------------------------------*/

    /*------------------------------------------------------------
    |
    | 1.1 FADERS
    |
    ------------------------------------------------------------*/

const headerText = document.querySelector('.header-text');
const headerDescription = document.querySelector('.header-description');

fadeIn(headerText, 200);
fadeIn(headerDescription, 500);

    /*------------------------------------------------------------
    |
    | 1.2 DROPDOWNS
    |
    ------------------------------------------------------------*/

/*--------------------------------------------------------------
2.0 PAPERSSS
--------------------------------------------------------------*/

    /*------------------------------------------------------------
    |
    | 2.1 DOM ELEMENTS
    |
    ------------------------------------------------------------*/

const timer = new Timer(document.querySelector('#timer'));
const counter = document.querySelector('#counter');
const englishWord = document.querySelector('#english-translation');
const spanishWord = document.querySelector('#spanish-translation');
let translations = null;

// Buttons
const playButton = document.querySelector('#play-button');
const setsButton = document.querySelector('#sets-button');
const optionsButton = document.querySelector('#options-button');
const exitButtons = document.querySelectorAll('.exit-button');
const learnExitButton = document.querySelector('#exit-button');
const yesButton = document.querySelector('#yes-button');
const noButton = document.querySelector('#no-button');

// Pages 
const learnPage = document.querySelector('.learn.page');
const statsPage = document.querySelector('.stats.page')
const mainPage = document.querySelector('.main.page');
const setsPage = document.querySelector('.sets.page');
const optionsPage = document.querySelector('.options.page');

const pages = [mainPage, learnPage, statsPage, setsPage, optionsPage];

    /*------------------------------------------------------------
    |
    | 2.2 VARIABLES
    |
    ------------------------------------------------------------*/

    /*------------------------------------------------------------
    |
    | 2.3 FUNCTIONS
    |
    ------------------------------------------------------------*/

async function getJSON() {
    translations = await(await fetch('assets/translations/example.json')).json();
    return translations[1].translations
}

async function startGame() {
    translations = await getJSON();
    counter.textContent = '0/0';
    nextTranslation();
}

function nextTranslation() {
    if (translations.length == 0) {
        showPage(mainPage);
        timer.stop();
        return
    }

    const index = Math.floor(Math.random() * translations.length);
    const translation = translations[index];
    englishWord.textContent = translation[0];
    spanishWord.textContent = translation[1];
    translations.splice(index, 1);
}

function updateCounter(correct) {
    score = counter.textContent.split('/');

    if (correct) {
        score[0] = parseInt(score[0]) + 1;
    }

    score[1] = parseInt(score[1]) + 1;

    counter.textContent = score.join('/');
}

function showPage(page) {
    pages.forEach((pageItem) => {
        if (page != pageItem) {
            pageItem.style.display = 'none';
        }
    });

    if (page == mainPage) {
        document.querySelector('app-navbar').style.display = 'flex';
    } else {
        document.querySelector('app-navbar').style.display = 'none';
    }

    page.style.display = 'flex';
}

    /*------------------------------------------------------------
    |
    | 2.4 EVENT LISTENERS
    |
    ------------------------------------------------------------*/

playButton.addEventListener('click', async () => {
    showPage(learnPage);
    startGame();
    let finished = await timer.start(60);

    if (finished) {
        showPage(mainPage);
    }
})

setsButton.addEventListener('click', () => {
    showPage(setsPage);
})

optionsButton.addEventListener('click', () => {
    showPage(optionsPage);
})

yesButton.addEventListener('click', () => {
    nextTranslation();
    updateCounter(true);
})

noButton.addEventListener('click', () => {
    nextTranslation();
    updateCounter(false);
})

learnExitButton.addEventListener('click', () => {
    showPage(mainPage);
    timer.stop();
})

exitButtons.forEach((exitButton) => {
    exitButton.addEventListener('click', () => {
        showPage(mainPage);
    })
})