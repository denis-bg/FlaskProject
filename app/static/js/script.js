$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function TestAlert() {
    alert('Ok !')
}

$('#laser-tab').on('shown.bs.tab', function () { InitJS_Laser();  });
function InitJS_Laser() {
}

$('#travail-tab').on('shown.bs.tab', function () { InitJS_Travail();  });
function InitJS_Travail() {

    //trvpulse.onclick = function() { VisibilityPulseParams(); };
    //chkgravure.onclick = function() { Toggle_flag('gravure'); };
    //chkdecoupe.onclick = function() { Toggle_flag('decoupe'); };
    //chkairblow.onclick = function() { Toggle_flag('airblow'); };
 //   trvgravure.onclick = function() { Visibility('trvgravure', '.ltt-gra-chk'); };
 //   trvdecoupe.onclick = function() { Visibility('trvdecoupe', '.ltt-dec-chk'); };
 //   trvairblow.onclick = function() { Visibility('trvairblow', '.ltt-air-chk'); };

    rad = document.MyForm.trvmode;
    //alert(rad.value);
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

//trvpulse.onclick = function() { setPulseParams(); };
//    setPulseParams();
//    Visibility('trvgravure', '.ltt-gra-chk');
//    Visibility('trvdecoupe', '.ltt-dec-chk');
//    Visibility('trvairblow', '.ltt-air-chk');
}

$('#page-tab').on('shown.bs.tab', function () { InitJS_Page();  });
function InitJS_Page() {
}

$('#puissance-tab').on('shown.bs.tab', function () { InitJS_Puissance();  });
function InitJS_Puissance() {
}

function VisibilityGDA(chk, cla) {
//alert(document.getElementById(chk).checked) ;
    if (document.getElementById(chk).checked) $(cla).removeAttr("disabled")
    else $(cla).attr("disabled", "true");
}

function Toggle_flag(col) {
    new_state = document.getElementById("chk"+col).checked
    for (let i = 0; i < 8; i++) {
       chk = "colorinfos-"+ i.toString() + "-" + col
       document.getElementById(chk).checked = new_state
    }
}

function VisibilityPulseParams() {
    pul = document.getElementById('trvpulse').checked;
    if (pul) $('.ltt-pulse').removeAttr("disabled");
    else $('.ltt-pulse').attr("disabled", "true");
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


$('#ltt-helpModal').on('show.bs.modal', function (event) {
    onglet = $("#lttTab li a.active").html();
    tabid = $("#lttTab li a.active").attr("id");

    var modal = $(this)
    modal.find('.modal-title').text('Aide ' + onglet)

    help = tabid+'-help';
    $('#laser-tab-help').hide();
    $('#travail-tab-help').hide();
    $('#page-tab-help').hide();
    $('#puissance-tab-help').hide();
    $('#'+help).show();

  //modal.find('.modal-body input').val(recipient)
})

$( document ).ready(function() {
    $('#help-laser').show();
    $('#help-travail').hide();
    $('#help-page').hide();
    $('#help-puissance').hide();

    VisibilityGDA('trvgravure', '.ltt-gra-chk');
    VisibilityGDA('trvdecoupe', '.ltt-dec-chk');
    VisibilityGDA('trvairblow', '.ltt-air-chk');

    trvgravure.onclick = function() { VisibilityGDA('trvgravure', '.ltt-gra-chk'); };
    trvdecoupe.onclick = function() { VisibilityGDA('trvdecoupe', '.ltt-dec-chk'); };
    trvairblow.onclick = function() { VisibilityGDA('trvairblow', '.ltt-air-chk'); };

    trvpulse.onclick = function() { VisibilityPulseParams(); };
    VisibilityPulseParams();

});

