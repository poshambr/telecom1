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

function searchSecDrop() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("secDropInp");
  filter = input.value.toUpperCase();
  div = document.getElementById("secDropUl");
  a = div.getElementsByTagName("li");
  for (i = 1; i < a.length; i++) {
    if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function searchCenDrop() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("cenDropInp");
  filter = input.value.toUpperCase();
  div = document.getElementById("cenDropUl");
  a = div.getElementsByTagName("li");
  for (i = 1; i < a.length; i++) {
    if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function searchIncDrop() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("incDropInp");
  filter = input.value.toUpperCase();
  div = document.getElementById("incDropUl");
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
    $('#searchTable').DataTable({
        "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ]
    });
} );