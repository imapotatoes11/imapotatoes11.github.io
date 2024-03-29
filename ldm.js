document.addEventListener('DOMContentLoaded', function() {
    // get the root element
    var root = document.documentElement;
    // get the value of --is-dark from localStorage
    var isDark = localStorage.getItem('isDark');
    // if --is-dark is true, toggle the theme
    if (isDark === 'true') {
        toggle();
    }

    // if first time, set --is-dark to true
    var firstTime = localStorage.getItem('firstTime');
    if (firstTime !== 'false') {
        toggle()
        localStorage.setItem('firstTime', 'false');
    }
})


function toggle() {
    // swap values of the following vars:
    // --text-color-light, --text-color-dark
    // --background-color-light, --background-color-dark
    // --background-color2-light, --background-color2-dark
    // --accent-color-light, --accent-color-dark

    // get the root element
    var root = document.documentElement;
    // get the current values of each var
    var textColorLight = getComputedStyle(root).getPropertyValue('--text-color-light');
    var textColorDark = getComputedStyle(root).getPropertyValue('--text-color-dark');
    var backgroundColorLight = getComputedStyle(root).getPropertyValue('--background-color-light');
    var backgroundColorDark = getComputedStyle(root).getPropertyValue('--background-color-dark');
    var backgroundColor2Light = getComputedStyle(root).getPropertyValue('--background-color2-light');
    var backgroundColor2Dark = getComputedStyle(root).getPropertyValue('--background-color2-dark');
    var backgroundColor3Light = getComputedStyle(root).getPropertyValue('--background-color3-light');
    var backgroundColor3Dark = getComputedStyle(root).getPropertyValue('--background-color3-dark');
    var backgroundColor3Light60op = getComputedStyle(root).getPropertyValue('--background-color3-light-60op');
    var backgroundColor3Dark60op = getComputedStyle(root).getPropertyValue('--background-color3-dark-60op');
    var backgroundColor4Light = getComputedStyle(root).getPropertyValue('--background-color4-light');
    var backgroundColor4Dark = getComputedStyle(root).getPropertyValue('--background-color4-dark');
    var backgroundColor4Light20op = getComputedStyle(root).getPropertyValue('--background-color4-light-20op');
    var backgroundColor4Dark20op = getComputedStyle(root).getPropertyValue('--background-color4-dark-20op');
    var accentColorLight = getComputedStyle(root).getPropertyValue('--accent-color-light');
    var accentColorDark = getComputedStyle(root).getPropertyValue('--accent-color-dark');

    var backgroundFullLight50op = getComputedStyle(root).getPropertyValue('--background-full-light-50op');
    var backgroundFullDark50op = getComputedStyle(root).getPropertyValue('--background-full-dark-50op');

    // set the new values of each var
    root.style.setProperty('--text-color-light', textColorDark);
    root.style.setProperty('--text-color-dark', textColorLight);
    root.style.setProperty('--background-color-light', backgroundColorDark);
    root.style.setProperty('--background-color-dark', backgroundColorLight);
    root.style.setProperty('--background-color2-light', backgroundColor2Dark);
    root.style.setProperty('--background-color2-dark', backgroundColor2Light);
    root.style.setProperty('--background-color3-light', backgroundColor3Dark);
    root.style.setProperty('--background-color3-dark', backgroundColor3Light);
    root.style.setProperty('--background-color3-light-60op', backgroundColor3Dark60op);
    root.style.setProperty('--background-color3-dark-60op', backgroundColor3Light60op);
    root.style.setProperty('--background-color4-light', backgroundColor4Dark);
    root.style.setProperty('--background-color4-dark', backgroundColor4Light);
    root.style.setProperty('--background-color4-light-20op', backgroundColor4Dark20op);
    root.style.setProperty('--background-color4-dark-20op', backgroundColor4Light20op);
    root.style.setProperty('--accent-color-light', accentColorDark);
    root.style.setProperty('--accent-color-dark', accentColorLight);

    root.style.setProperty('--background-full-light-50op', backgroundFullDark50op);
    root.style.setProperty('--background-full-dark-50op', backgroundFullLight50op);


    // toggle --is-dark
    if (root.style.getPropertyValue('--is-dark') === 'true') {
        root.style.setProperty('--is-dark', 'false');
    } else {
        root.style.setProperty('--is-dark', 'true');
    }


    // save value of --is-dark to localStorage
    localStorage.setItem('isDark', root.style.getPropertyValue('--is-dark'));
    localStorage.setItem('firstTime', 'false');
}