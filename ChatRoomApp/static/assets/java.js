const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");


//WebSocket Beginned

const chatSocket = new WebSocket('ws://' + window.location.host + '/chatws/');
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const message = data['message'];
    const userID = data['userID']
    if (userID !== localStorage.getItem('userID'))
        appendMessage(userID, BOT_IMG, "left", message);


    // Handle incoming message
};
chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};
// Send message to
chatSocket.onopen = function (e) {
}

function sendMessage(message, userID) {
    chatSocket.send(JSON.stringify({'message': message, 'userID': userID}));

}

// Icons made by Freepik from www.flaticon.com
const BOT_IMG = "https://www.google.com/imgres?q=profile%20image%20png&imgurl=https%3A%2F%2Fw7.pngwing.com%2Fpngs%2F184%2F113%2Fpng-transparent-user-profile-computer-icons-profile-heroes-black-silhouette-thumbnail.png&imgrefurl=https%3A%2F%2Fwww.pngwing.com%2Fen%2Fsearch%3Fq%3Dprofile&docid=OnvONsOWadRfDM&tbnid=XtzeG3595_IYSM&vet=12ahUKEwj_m5OIt_2FAxXa_7sIHbdyAZUQM3oECB0QAA..i&w=360&h=355&hcb=2&ved=2ahUKEwj_m5OIt_2FAxXa_7sIHbdyAZUQM3oECB0QAA";
const PERSON_IMG = "https://image.flaticon.com/icons/svg/145/145867.svg";
const BOT_NAME = "BOT";

let username = "";
let LocalUsername = localStorage.getItem('userID');
if (LocalUsername) {
    username = LocalUsername;

    console.log(LocalUsername);
} else {
    username = localStorage.getItem('usernameFromServer');
    localStorage.setItem('userID', username);

    console.log('yok', username);
}
const PERSON_NAME = username.toString();
console.log('ady', PERSON_NAME);

msgerForm.addEventListener("submit", event => {
    event.preventDefault();

    const msgText = msgerInput.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    msgerInput.value = "";
    sendMessage(msgText, username);


});

function appendMessage(name, img, side, text) {
    //   Simple solution for small apps
    const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
}

function botResponse() {
    const r = random(0, BOT_MSGS.length - 1);
    const msgText = BOT_MSGS[r];
    const delay = msgText.split(" ").length * 100;

    setTimeout(() => {
        appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
    }, delay);
}

// Utils
function get(selector, root = document) {
    return root.querySelector(selector);
}

function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}

function random(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}


