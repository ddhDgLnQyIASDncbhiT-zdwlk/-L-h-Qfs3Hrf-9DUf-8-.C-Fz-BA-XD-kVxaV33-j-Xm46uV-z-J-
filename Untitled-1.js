
var chatbox = document.getElementById('chatbox');
var textbox = document.getElementById('textbox').textContent;

var recipient = document.getElementById('recipient').textContent;
var sender = document.getElementById('sender').textContent;
var sendbutton = document.getElementById('sendbutton');
sendbutton.addEventListener('click', send);


function send(){
    var xhttp = new XMLHttpRequest();
    xhttp.open('POST', 'http://149.28.72.58:5000/api/v1/user/messages');
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send(JSON.stringify({
        message: textbox.textContent, sender: sender, recipient: recipient,time:Date.now()}));
};

function recieve(sender, recipient){
var messagearray = new Array();
var chatarray = new Array();
var xhttp = new XMLHttpRequest();
xhttp.open('GET', 'http://149.28.72.58:5000/api/v1/user/messages');
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
         messagearray = this.response;
    }
  };
xhttp.send('sender='+sender+'&recipient='+recipient);

for(i=0;i <= messagearray.length;i++){
    time += messagearray[i].time;
    for(l=0;l <= chatarray.length;l++){
        if(time < chatarray[l].time || chatarray[l] == null){
            chatarray.splice(l,0,messagearray[l])
        }
    }
}
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        messagearray = this.response;
    }
  };
xhttp.send('sender='+recipient+'&recipient='+sender);
for(l=0;l <= chatarray.length;l++){
    if(time < chatarray[l].time || chatarray[l] == null){
        chatarray.splice(l,0,messagearray[l])
    }
}

for(t=0;t<=messagearray.length;t++){
    var messagecontent = document.createElement('div');
    messagecontent.appendChild(document.createTextNode(messagearray[t].message));
}
recieve(sender, recipient);
}

function recievechats(sender){
    var xhttp = new XMLHttpRequest();
    var chats = new Array();
    xhttp.open('POST', 'http://149.28.72.58:5000/api/v1/user/messages');
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            chats  = this.response;
        }
      };
      xhttp.send('sender='+sender);
    for(i=0;i<=chats.length;i++){
    
    }
}
