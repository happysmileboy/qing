function detail_view_function(url){
  $(".detail_box").addClass('detail_visible');
  $(".background_box").addClass('background_visible');
  $('.detail_box').load(url);
}

$(document).ready(function(){
  $('.detail_box').click(function(){
    $(".detail_box").removeClass('detail_visible');
    $(".background_box").removeClass('background_visible');
  })
})