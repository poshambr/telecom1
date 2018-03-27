function searchDeptDrop() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("deptDropInp");
  filter = input.value.toUpperCase();
  div = document.getElementById("deptDropUl");
  a = div.getElementsByTagName("li");
  for (i = 1; i < a.length; i++) {
    if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function searchDesDrop() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("desDropInp");
  filter = input.value.toUpperCase();
  div = document.getElementById("desDropUl");
  a = div.getElementsByTagName("li");
  for (i = 1; i < a.length; i++) {
    if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

$(document).ready(function() {
    $('#searchTable').DataTable();
} );