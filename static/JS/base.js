function CloseModal() {
    document.getElementById('myModal').style.display = 'none'
}
//document.getElementById('RegModal').style.display='block';document.getElementById('MainBodyBlock').classList.add('MenuState')
/* Open */
function BR() {
    function GetXmlHttpObjects() {
        var xmlHttp = null;
        try {
            xmlHttp = new XMLHttpRequest();
        } catch (e) {
            try {
                xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
            } catch (e) {
                xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
        }
        return xmlHttp;
    }
    xmlHttp = GetXmlHttpObjects()
    if (xmlHttp == null) {
        return;
    }
    begin = new Date().getTime();

    url = "/dob?Dt=" + begin

    xmlHttp.open("POST", url, true);
    xmlHttp.send(null);

    document.location.href = "/stats";
}

function St() {
    document.location.href = "/stats";
}

function openNav() {
    try {
        document.getElementById("myNav").style.height = "100%";
        document.getElementById('MainBodyBlock').classList.add('MenuState')
    } catch {

    }

}

/* Close */
function closeNav() {
    document.getElementById("myNav").style.height = "0%";
    document.getElementById('MainBodyBlock').classList.remove('MenuState')
}


// Смена подчеркивания в меню
pash = document.location.pathname
console.log(pash)
if (pash == '/' || pash == '/main') {
    document.getElementById('m1').classList.add('ActiveInterface')
} else if (pash == '/news') {
    document.getElementById('m2').classList.add('ActiveInterface')
} else if (pash == '/video') {
    document.getElementById('m3').classList.add('ActiveInterface')
} else if (pash == '/about') {
    document.getElementById('m4').classList.add('ActiveInterface')
}