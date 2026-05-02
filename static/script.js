const sounds = new Audio("/static/type.mp3");

window.addEventListener("load", () => {
    const boot = document.getElementById("boot");
    setTimeout(() => {
        boot.style.display = "none";
    }, 1200);
});

function typeEffect(element, text, speed = 30) {
    let i = 0;
    element.innerHTML = "";

    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            sounds.currentTime = 0;
            sounds.play().catch(() => {});
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}

document.querySelectorAll(".typing").forEach(el => {
    const text = el.getAttribute("data-text");
    typeEffect(el, "> " + text);
});

setInterval(() => {
    document.body.classList.add("glitch-active");
    setTimeout(() => {
        document.body.classList.remove("glitch-active");
    }, 150);
}, 8000);

const realInput = document.getElementById("real-input");
const fakeInput = document.getElementById("fake-input");

const typeSound = new Audio("/static/type.mp3");

// focus when clicking the fake input
function focusInput() {
    realInput.focus();
}

// typing effect
realInput.addEventListener("keydown", (e) => {
    if (e.key.length === 1) {
        fakeInput.innerHTML += e.key;

        typeSound.currentTime = 0;
        typeSound.play().catch(() => {});
    }

    if (e.key === "Backspace") {
        fakeInput.innerHTML = fakeInput.innerHTML.slice(0, -1);
    }
});