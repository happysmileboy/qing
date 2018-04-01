$(document).ready(function(){
  $(".mypage_dropbox").mouseenter(function(){
    $(".dropdown_content_mypage").addClass('show')
  })
})

$(document).ready(function(){
  $(".mypage_dropbox").mouseleave(function(){
    $(".dropdown_content_mypage").removeClass('show')
  })
})

$(document).ready(function(){
  $(".FAQlink").mouseenter(function(){
    $(".dropdown_content_FAQ").addClass('show')
  })
})

$(document).ready(function(){
  $(".FAQlink").mouseleave(function(){
    $(".dropdown_content_FAQ").removeClass('show')
  })
})
