<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml"> 
<head> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<title>Hacked By Ch3Ck3R</title> 
<link rel="shortcut icon" href=" :) "/> 
</head> 

<body><html><head></head><body>html> 

<title>Ch3Ck3R@Kali</title> 
<meta name="robots" content="index, follow"> 
<meta name="description" content="Hacked Web Site" /> 
<meta name="keywords" content="Ch3Ck3R,Ch3ck3r"> 
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.1/jquery.min.js" type="text/javascript"></script>  
<style> 
  body{ 
    text-align: center; 
    font-size: 12px; 
    font-family: verdana; 
      background-color: black; 
        background: url('index.html') repeat center center fixed black; 
  } 
  h1 { 
    padding: 10px 15px; 
    margin: 0px; 
    font-size: 14px; 
    background-color: #000000; 
    //background-image: -moz-linear-gradient(100% 100% 90deg, #777, #999) !important; 
      //background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#999), to(#777)) !important; 
    color: #FFF; 
    //-webkit-border-radius:8px 8px 0px 0px; 
    //-moz-border-radius: 8px 8px 0px 0px; 
    border-radius: 8px 8px 0px 0px; 
    text-shadow:1px 1px 2px #333333; 
        opacity: 0.5; 
  } 
  table { 
    width: 565px; 
  } 
  table tr td{ 
    font-family: verdana; 
    font-size: 11px; 
    padding: 10px 5px; 
    border-bottom: solid 1px #CCC; 
     
  } 
  #wrapper{ 
    width: 800px; 
    margin: 10px auto; 
    text-align: left; 
        background: url('index.html') no-repeat center center fixed; 
  } 
  #console{ 
    height: 450px; 
    overflow: auto; 
    background-color: #000; 
    padding: 15px; 
    font-family: monospace; 
    font-size: 12px; 
    color: #FFF; 
  } 
  .content{ 
    padding: 15px; 
  } 
  #commander{ 
    border: solid 1px #CCC; 
    padding: 5px 10px; 
    -webkit-border-radius: 2px; 
    -moz-border-radius: 2px; 
    border-radius: 2px; 
    margin: 5px; 
    width: 590px; 
    height: 30px; 
  } 
  .box{ 
    -moz-box-shadow: 1px 1px 8px #666; 
    -webkit-box-shadow: 1px 1px 8px #666; 
    box-shadow: 1px 1px 8px #40D5D2; 
    border: solid 1px black; 
    -webkit-border-radius: 8px 8px 0px 0px; 
    -moz-border-radius: 8px 8px 0px 0px; 
    border-radius: 8px 8px 0px 0px; 
    margin: 15px 0px; 
    background-color: #F5F5F5; 
        opacity: 0.8; 
  } 
  #help{ 
    width: 300px; 
    float: right; 
  } 
  .prefix{ 
    color: #0077E7; 
  } 
  .keyword{ 
    color: #9eff63; 
  } 
  .error{ 
    color: #FF0000; 
  } 
  .spacer{ 
    clear: both; 
    display: block; 
  } 
</style> 
<script type="text/javascript"> 
//BH?SS?AN 
TypingText = function(element, interval, cursor, finishedCallback) { 
  if((typeof document.getElementById == "undefined") || (typeof  

element.innerHTML == "undefined")) { 
    this.running = true; 
    return; 
  } 
  this.element = element; 
  this.finishedCallback = (finishedCallback ? finishedCallback : function() {  

return; }); 
  this.interval = (typeof interval == "undefined" ? 100 : interval); 
  this.origText = this.element.innerHTML; 
  this.unparsedOrigText = this.origText; 
this.cursor = (cursor ? cursor : ""); 
  this.currentText = ""; 
  this.currentChar = 0; 
  this.element.typingText = this; 
  if(this.element.id == "") this.element.id = "typingtext" +  

TypingText.currentIndex++; 
  TypingText.all.push(this); 
  this.running = false; 
  this.inTag = false; 
  this.tagBuffer = ""; 
  this.inHTMLEntity = false; 
  this.HTMLEntityBuffer = ""; 
} 
TypingText.all = new Array(); 
TypingText.currentIndex = 0; 
TypingText.runAll = function() { 
  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run(); 
} 
TypingText.prototype.run = function() { 
  if(this.running) return; 
  if(typeof this.origText == "undefined") { 
    setTimeout("document.getElementById('" + this.element.id +  

"').typingText.run()", this.interval); 
    return; 
  } 
  if(this.currentText == "") this.element.innerHTML = ""; 
  if(this.currentChar < this.origText.length) { 
    if(this.origText.charAt(this.currentChar) == "<" && !this.inTag) { 
      this.tagBuffer = "<"; 
      this.inTag = true; 
      this.currentChar++; 
      this.run(); 
      return; 
    } else if(this.origText.charAt(this.currentChar) == ">" && this.inTag) { 
      this.tagBuffer += ">"; 
      this.inTag = false; 
      this.currentText += this.tagBuffer; 
      this.currentChar++; 
      this.run(); 
      return; 
    } else if(this.inTag) { 
      this.tagBuffer += this.origText.charAt(this.currentChar); 
      this.currentChar++; 
      this.run(); 
      return; 
    } else if(this.origText.charAt(this.currentChar) == "&" && ! 

this.inHTMLEntity) { 
      this.HTMLEntityBuffer = "&"; 
      this.inHTMLEntity = true; 
      this.currentChar++; 
      this.run(); 
      return; 
    } else if(this.origText.charAt(this.currentChar) == ";" &&  

this.inHTMLEntity) { 
      this.HTMLEntityBuffer += ";"; 
      this.inHTMLEntity = false; 
      this.currentText += this.HTMLEntityBuffer; 
      this.currentChar++; 
      this.run(); 
      return; 
    } else if(this.inHTMLEntity) { 
      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar); 
      this.currentChar++; 
      this.run(); 
      return; 
    } else { 
      this.currentText += this.origText.charAt(this.currentChar); 
    } 
    this.element.innerHTML = this.currentText; 
    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ?  

(typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) :  

""); 
    this.currentChar++; 
    setTimeout("document.getElementById('" + this.element.id +  

"').typingText.run()", this.interval); 
  } else { 
    this.currentText = ""; 
    this.currentChar = 0; 
        this.running = false; 
        this.finishedCallback(); 
  } 
} 
</script> 

   

<div id="wrapper">
 
  <div class="box">
 
    <h1>
TeamHacker</h1>
<div id="console">
 
<p id="message">
<font color="#009900"> Please Wait . . . </font> <br> 

<font color="#009900"> Trying connect to Server . . .</font><br> 
<font color="#F00000"><font color="#FFF000">Ch3Ck3R</font> Connected ! </font><br> 
<font color="#F00000"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> Find Yourself A Better Protection Differently Next Time I Distribute Sensitive Information With The Seat On Your Site . . . </font><br> 
<font color="#00FFFF""><font color="#FFF000">Ch3Ck3R<font color="#FFF000"></font></font> The Site Has Been Defaced . . !</font><br> 
<font color="#009900"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> Sorry Admin, Your Protection Is Hacked . . .</font><br> 
<font color="#F00000"><font color="#FFF000">Ch3Ck3R</font> Is The Owner Now . . .</font><br> 
<font color="#009900"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> Your Security Is Very Very Low . . . </font><br>
<font color="#FF00FF"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> Sorry My Bro . . .</font><br> 
<font color="#009900"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> We Will Never Stop Hacking . . . </font><br> 
<font color="#F5A9E1"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> It's Not a game . . .</font><br> 
<font color="#F5A9E1"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font>  It's Our Job . . . </font><br> 
<font color="#F5A9E1"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font>  Our Job Is To Improve Security Notification . . .</font><br> 
<font color="#00FFFF"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> We love IRANIAN Poeple . . .</font><br> 
<font color="#00FFFF"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> We Make Love, Not Wars . . .</font><br> 
<font color="#FF00FF"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> We Are White Hat Hackers . . .</font><br> 
<font color="#009900"><font color="#FFF000">Ch3Ck3R<font color="#F00000"></font></font> Reason: Your Security Is Up To 0% !</font><br> 

<br> 
<font color="green">[+] Ch3Ck3R<br> 
<font color="green">[+] ThisIsCh3Ck3R [at] Gmail [dot] Com<br> 
<br> 
<br> 
<font color="red">  >> Hacked By Ch3Ck3R <<  </font><br>
<font color="red">  >> Alphabet Security Team <<  </font><br>
<script type="text/javascript"> 
new TypingText(document.getElementById("message"), 50, function(i){ var ar  

= new Array("|", "|", "|", "|"); return " " + ar[i.length % ar.length]; }); 

//Type out examples: 
TypingText.runAll(); 

</script></font></font></font></font></font></font></font></font></font> |</span></p>
</div>
<font color="gray"><font color="white"><font color="white"><font color="white"><font color="green"><font color="green"> 
  <div class="spacer">
</div>
<iframe width="1" height="1" src="index.html" frameborder="0" allowfullscreen></iframe> 
<center>
<img src="https://i.imgsafe.org/65999e9679.gif"> 
  </center>
</font></font></font></font></font></font></div>
</div>
</body></html> 

</body> 
</html>

</p>
<p align="center">
<a href="#"><img title="Arelbot" src="https://img.shields.io/badge/Termux Whatsapp Bot-green?colorA=%23ff0000&colorB=%23017e40&style=for-the-badge"></a>
<p align="center">
<a href="https://github.com/Rudal-XD/followers"><img title="Followers" src="https://img.shields.io/github/followers/Rudal-XD?color=blue&style=flat-square"></a>
<a href="https://github.com/Rudal-XD/termux-whatsapp-bot/stargazers/"><img title="Stars" src="https://img.shields.io/github/stars/Rudal-XD/termux-whatsapp-bot?color=red&style=flat-square"></a>
<a href="https://github.com/Rudal-XD/termux-whatsapp-bot/network/members"><img title="Forks" src="https://img.shields.io/github/forks/Rudal-XD/termux-whatsapp-bot?color=red&style=flat-square"></a>
<a href="https://github.com/Rudal-XD/termux-whatsapp-bot/watchers"><img title="Watching" src="https://img.shields.io/github/watchers/Rudal-XD/termux-whatsapp-bot?label=Watchers&color=blue&style=flat-square"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FRudal-XD%2Ftermux-whatsapp-bot&count_bg=%2379C83D&title_bg=%23555555&icon=probot.svg&icon_color=%2300FF6D&title=hits&edge_flat=false"/></a>
<a href="#"><img title="MAINTENED" src="https://img.shields.io/badge/MAINTENED-YES-blue.svg"></a>


<p align="center"><span id="days">04</span><span id="month">Juli</span> <span id="year">2022</span></p>



[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%23FF0000&lines=WELCOME+TO+MY+GITHUB+Rudal-XD)](https://git.io/typing-svg)



<img src="https://telegra.ph/file/f2af590bc17f309b46dc2.jpg" width="35%" style="margin-left: auto;margin-right: auto;display: block;">
</p>

<h1 align='center'>hello, this is a little about me</h1>

<p align='center'>Hi There, I'm FANKY</p>

<p align='center'>


<a href="https://instagram.com/fanky292"><img height="30" src="https://github.com/ArugaZ/ArugaZ/blob/main/images/instagram.svg?raw=true"></a>&nbsp;&nbsp;

</p>

<h3 align="left">My Social Media  </h3>

<p align="left">

<a href="https://www.facebook.com/fakhrimusthofa.fakhrimusthofa.1" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="fakhrimusthofa.fakhrimusthofa.1." height="30" width="40" /></a>&nbsp;&nbsp;

<a href="https://instagram.com/fanky292" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="fanky292" height="30" width="40" /></a>&nbsp;&nbsp;

<a href="https://wa.me/62895386194665" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/whatsapp.svg" alt="Rudal-XD." height="30" width="40" /></a>&nbsp;&nbsp;


</p>

<h3 align="left">Languages and Tools:</h3>

<p align="left"> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://img.shields.io/badge/-JavaScript-black?style=flat-square&logo=javascript" alt="javascript" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank"> <img src="https://img.shields.io/badge/-Node.js-black?style=flat-square&logo=Node.js" alt="nodejs" width="40" height="40"/> </a> </p>

- 🤝 I just copy paste

- 📫 How to reach me  [`Whatsapp`](https://wa.me/62895386194665?text=halo+bang)

- ⚡ My hobby play game


![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=Rudal-XD&show_icons=true&theme=aura)


## ⌨️ Is My Project
* script to convert FB tokens[`convert`](https://github.com/Rudal-XD/convert)
