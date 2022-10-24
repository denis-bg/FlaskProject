$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function MyFunc(col) {
    //alert(col);
    for (let i = 0; i < 8; i++) {
       chk = "colorinfos-"+ i.toString() + "-" + col
       document.getElementById(chk).checked = document.getElementById("chk"+col).checked
    }
}

$( document ).ready(function() {
      //alert("This page has been loaded");
    if($('#chkgravure').length > 0) chkgravure.onclick = function() { MyFunc('gravure'); };
    if($('#chkdecoupe').length > 0) chkdecoupe.onclick = function() { MyFunc('decoupe'); };
    if($('#chkairblow').length > 0) chkairblow.onclick = function() { MyFunc('airblow'); };

      function yesno(chk, label) {
      alert("Click!")
        /*document.getElementById(label).innerHTML = chk.checked ? "Yes" : "No";*/
    }


/*$("checkbox").click(MyFunc);*/

});
