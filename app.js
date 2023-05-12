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

// Buttons
const playButton = document.querySelector('#play-button');
const setsButton = document.querySelector('#sets-button');
const optionsButton = document.querySelector('#options-button');
const exitButtons = document.querySelectorAll('.exit-button');
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

playButton.addEventListener('click', () => {
    showPage(learnPage);
})

setsButton.addEventListener('click', () => {
    showPage(setsPage);
})

optionsButton.addEventListener('click', () => {
    showPage(optionsPage);
})

exitButtons.forEach((exitButton) => {
    exitButton.addEventListener('click', () => {
        showPage(mainPage);
    })
})