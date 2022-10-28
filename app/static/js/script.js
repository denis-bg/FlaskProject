$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function TestAlert() {
    alert('Ok !')
}

$('#laser-tab').on('shown.bs.tab', function () { InitJS_Laser();  });
function InitJS_Laser() {

    //loadHTML("help-content", "help-laser.html");
}

$('#travail-tab').on('shown.bs.tab', function () { InitJS_Travail();  });
function InitJS_Travail() {
    if($('#chkgravure').length > 0) chkgravure.onclick = function() { Toggle_flag('gravure'); };
    if($('#chkdecoupe').length > 0) chkdecoupe.onclick = function() { Toggle_flag('decoupe'); };
    if($('#chkairblow').length > 0) chkairblow.onclick = function() { Toggle_flag('airblow'); };
    //alert($('trvmode').value)

    rad = document.MyForm.trvmode;
    if (rad.value == 0) {
        $('.ltt-tampon').attr("disabled", "true");
        $('.ltt-gris').attr("disabled", "true");
    }
    if (rad.value == 1) {
        $('.ltt-norm').attr("disabled", "true");
        $('.ltt-gris').attr("disabled", "true");
    }
    if (rad.value == 2) {
        $('.ltt-norm').attr("disabled", "true");
        $('.ltt-tampon').attr("disabled", "true");
    }
    rad[0].addEventListener('change', function() {
        $('.ltt-norm').removeAttr("disabled");
        $('.ltt-tampon').attr("disabled", "true");
        $('.ltt-gris').attr("disabled", "true");
    });
    rad[1].addEventListener('change', function() {
        $('.ltt-norm').attr("disabled", "true");
        $('.ltt-tampon').removeAttr("disabled");
        $('.ltt-gris').attr("disabled", "true");
    });
    rad[2].addEventListener('change', function() {
        $('.ltt-norm').attr("disabled", "true");
        $('.ltt-tampon').attr("disabled", "true");
        $('.ltt-gris').removeAttr("disabled");
    });

    /*var rad = document.MyForm.trvmode;
    alert(rad.value);
    var prev = null;
    for (var i = 0; i < rad.length; i++) {
        rad[i].addEventListener('change', function() {
            (prev) ? console.log(prev.value): null;
            if (this !== prev) {
                prev = this;
            }
            console.log(this.value)
        });
    }*/
}

$('#page-tab').on('shown.bs.tab', function () { InitJS_Page();  });
function InitJS_Page() {
    //loadHTML("help-content", "help-page.html");
}

$('#puissance-tab').on('shown.bs.tab', function () { InitJS_Puissance();  });
function InitJS_Puissance() {
    //loadHTML("help-content", "help-puissance.html");
}

function loadHTML(id, filename) {
    console.log(`div id: ${id}, filename: ${filename}`);
    element = document.getElementById(id);
    file = "static/helpfiles/"+filename;
    alert(file)
    //return
    let xhttp;
    if (file) {
      msg="2-"+file
      alert(msg)
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        //alert(filename);
        if (this.readyState == 4) {
          if (this.status == 200) element.innerHTML = "Ok"; //this.responseText;
          if (this.status == 404) loadHTML("help-content", "help-404.html");
        }
      }
      xhttp.open("GET", file, true);
      xhttp.send();
      return;
    }
}


/* $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
  var target = $(e.target).attr("href") // activated tab
  id = "help-content";
  filename = 'help-'+target.substring(1)+".html"
  loadHTML(id, filename)
}); */

function Toggle_flag(col) {
    new_state = document.getElementById("chk"+col).checked
    for (let i = 0; i < 8; i++) {
       chk = "colorinfos-"+ i.toString() + "-" + col
       document.getElementById(chk).checked = new_state
    }
}

function TousLesMemes(e) {
  //alert(e.id+'-'+e.value+'-')
  f = e.id
  //if (e.value != '') {
    for (let i = 0; i < 8; i++) {
       cf = "colorinfos-"+ i.toString() + "-" + f
       if (e.value != '') {
           document.getElementById(cf).value = e.value
           document.getElementById(cf).disabled = true
           if (f == 'power') document.getElementById('speed').disabled = true
           else document.getElementById('power').disabled = true
       }
       else {
           document.getElementById(cf).disabled = false
           if (f == 'power') document.getElementById('speed').disabled = false
           else document.getElementById('power').disabled = false
       }
    }
  //}
}

$( document ).ready(function() {
  //loadHTML("help-content", "help-laser.html")
});

