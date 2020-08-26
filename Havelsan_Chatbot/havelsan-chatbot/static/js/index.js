var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
    var speech = [];
    speech.push('Merhaba, ben HAVELSAN CHATBOT . Size nasıl yardımcı olabilirim ?')
    speech.push('')
    $.post('/postmethod', {
    		text: JSON.stringify(speech)
    	}).done(function(hop) 
    	{
    	}).fail(function() {
			alert('error calling function');
	});  		
    $messages.mCustomScrollbar();
    setTimeout(function() {
       //fakeMessage();
    }, 100);
      //console.log(val)
    printMessage('Merhaba, ben HAVELSAN CHATBOT. ');
    printMessage('Size nasıl yardımcı olabilirim?');

});

function printMessage(msj){
 $('<div class="message new"><figure class="avatar"><img src="/static/res/speech.png" /></figure><b>' + msj + '</b></div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
}

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
	interact(msg);
  setTimeout(function() {
    //fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() { 
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})


function insertVoice() {
	
  	$.post('/voice',).done(function(listen) {
	   returnedText = listen['text'];
	   if(returnedText == '...'){     
	   $('<div class="message new"><figure class="avatar"><img src="/static/res/speech.png" /></figure><b>' + 'Sesinizi Algılayamadık, Lütfen Cevabınızı Tekrar Ediniz' + '</b></div>').appendTo($('.mCSB_container')).addClass('new');

		setDate();
		updateScrollbar();			
			
	}
	else{
	
    $('<div class="message message-personal">' + returnedText + '</div>').appendTo($('.mCSB_container')).addClass('new');
	setDate();
    updateScrollbar();
	interact(returnedText);
	}
	
   $('.voice-listen').css("backgroundColor", "#12054E");
	}).fail(function() {
				alert('error calling function');
				});
	
  setTimeout(function() {
  }, 1000 + (Math.random() * 20) * 100);
	
}
$('.voice-listen').click(function() {
    $('.voice-listen').css("backgroundColor", "#12054E");
    insertVoice();
});



function interact(message){
    console.log(message)
	// loading message
  $('<div class="message loading new"><figure class="avatar"><img src="/static/res/speech.png" /></figure><span></span></div>').appendTo($('.mCSB_container'));
	// make a POST request [ajax call]
	$.post('/message', {
		msg: message,
	}).done(function(reply) {
		// Message Received
		// 	remove loading meassage
    $('.message.loading').remove();
       if(reply['reload'] == true){
       
          console.log(reply['reload'])
          console.log(reply['text'])
			$( reply['text'] ).each(function() { 
        
          console.log(reply['reload'])
          console.log(this)
            // Add message to chatbox
            $('<div class="message new"><figure class="avatar"><img src="/static/res/speech.png" /></figure>' + this + '</div>').appendTo($('.mCSB_container')).addClass('new');
            setDate();
            updateScrollbar();    
        }); 
			
			
         setTimeout(function() {
               window.location.reload(false)
    	   }, 5000);
	   }
	   else
	   {	     
          console.log('reload false')
        $( reply['text'] ).each(function() { 
        
          console.log(reply['reload'])
          console.log(this)
            // Add message to chatbox
            $('<div class="message new"><figure class="avatar"><img src="/static/res/speech.png" /></figure>' + this + '</div>').appendTo($('.mCSB_container')).addClass('new');
            setDate();
            updateScrollbar();    
        });    
	   }
    
    
  
	

		}).fail(function() {
				alert('error calling function');
				});
}