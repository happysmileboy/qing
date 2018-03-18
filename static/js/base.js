$(document).ready(function(){
  $(".mypage_dropbox").mouseenter(function(){
    $(".dropdown-content").addClass('show')
  })
})

$(document).ready(function(){
  $(".mypage_dropbox").mouseleave(function(){
    $(".dropdown-content").removeClass('show')
  })
})