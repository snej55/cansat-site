let theme = 0;

if (document.cookie.trim().startsWith("background: 1")) {
    theme = 1
}
else {
    document.cookie = "background: 0"
}

export let darkModeInnit = theme