$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function TestAlert() {
    alert('Ok !')
}

function InitJS_Travail() {
//alert("Show travail tab")
    if($('#chkgravure').length > 0) chkgravure.onclick = function() { Toggle_flag('gravure'); };
    if($('#chkdecoupe').length > 0) chkdecoupe.onclick = function() { Toggle_flag('decoupe'); };
    if($('#chkairblow').length > 0) chkairblow.onclick = function() { Toggle_flag('airblow'); };
}

//$('#travail-tab').on('shown.bs.tab', function () { InitJS_Travail();  });

function Toggle_flag(col) {
    new_state = document.getElementById("chk"+col).checked
    //alert(col + " - " + new_state)
    for (let i = 0; i < 8; i++) {
       chk = "colorinfos-"+ i.toString() + "-" + col
       //alert("avant" + " - " + chk + " - " + document.getElementById(chk).checked)

       //document.getElementById(chk).checked = document.getElementById("chk"+col).checked
       document.getElementById(chk).checked = new_state
       //alert("apres" + " - " + chk + " - " + document.getElementById(chk).checked)
    }
}

/*alert("Start!");*/
if($('#chkgravure').length > 0) chkgravure.onclick = function() { Toggle_flag('gravure'); };
if($('#chkdecoupe').length > 0) chkdecoupe.onclick = function() { Toggle_flag('decoupe'); };
if($('#chkairblow').length > 0) chkairblow.onclick = function() { Toggle_flag('airblow'); };

$( document ).ready(function() {
     //alert("This page has been loaded");
/*    if($('#chkgravure').length > 0) chkgravure.onclick = function() { MyFunc('gravure'); };
    if($('#chkdecoupe').length > 0) chkdecoupe.onclick = function() { MyFunc('decoupe'); };
    if($('#chkairblow').length > 0) chkairblow.onclick = function() { MyFunc('airblow'); };*/

      function yesno(chk, label) {
      alert("Click!")
        /*document.getElementById(label).innerHTML = chk.checked ? "Yes" : "No";*/
    }


/*$("checkbox").click(MyFunc);*/

});
