$(document).ready(function() {
  $("#nothing").on("click", function() {
    setText();
  });
});

function setText () {
  $("#nothing-header").text("don't you have anything better to do?");
}
