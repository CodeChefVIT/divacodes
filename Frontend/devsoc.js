alert('connected');
var searchterms = '';

function getTerm(term) {
  console.log(term);
  $('.term').text(term);
}


$("#submit").on("click", function() {
  searchterms = $("#choices-text-preset-values").val();
  console.log(searchterms);
  var url = "https://externalwebsite.com/search?term=" + searchterms + "&variable2=something";
  console.log(url);
  $.getJSON(url, function(data) {
    console.log(data);
  });
  return false;
});