// Generated by CoffeeScript 1.4.0

/*
RECORDING
*/


(function() {
  var RECORDING_LIMIT, file_input, play, record, stop, timecode, upload, submit;
  var recording = true;
  RECORDING_LIMIT = 10 * 1000;

  timecode = function(ms) {
    var hms, tc;
    hms = {
      h: Math.floor(ms / (60 * 60 * 1000)),
      m: Math.floor((ms / 60000) % 60),
      s: Math.floor(ms / 1000 % 60)
    };
    tc = [];
    if (hms.h > 0) {
      tc.push(hms.h);
    }
    tc.push(hms.m < 10 && hms.h > 0 ? "0" + hms.m : hms.m);
    tc.push(hms.s < 10 ? "0" + hms.s : hms.s);
    return tc.join(':');
  };

  Recorder.initialize({
    swfSrc: "/static/libs/recorder/recorder.swf"
  });

  record = function() {
    return Recorder.record({
      start: function() {
        return document.getElementById('record_button').value = 'Stop';
        //return document.getElementById("stop_button").disabled = false;
      },
      progress: function(milliseconds) {
        document.getElementById("time").innerHTML = timecode(milliseconds);
        if (milliseconds > RECORDING_LIMIT) {
          return Recorder.stop();
        }
      },
      cancel: function() {
        document.getElementById('record_button').disabled = false;
        return document.getElementById("stop_button").disabled = true;
      }
    });
  };

  play = function() {
    Recorder.stop();
    return Recorder.play({
      progress: function(milliseconds) {
        return document.getElementById('time').innerHTML = timecode(milliseconds);
      },
      finished: function() {}
    });
  };

  stop = function() {
    document.getElementById("time").innerHTML = '';
    document.getElementById('record_button').value = 'Record';
    //document.getElementById("stop_button").disabled = true;
    Recorder.stop();
    return upload();
  };

  fill_form = function(text) {
	document.getElementById('user_text').value = text;
  };
  
  upload = function() {
    document.getElementById('user_text').value = '...';
    Recorder.upload({
      url: "/",
      audioParam: "audio_file",
      success: function(response) {
        var response_json,
            user_text = document.getElementById('user_text'),
            interval = document.getElementById('interval');
        response_json = $.parseJSON(response);
        window.n_channels = 1;
        console.log(response_json.transcription);
        console.log(response_json.interval);
        user_text.value = response_json.transcription;
        interval.value = response_json.interval;
        return false;
        //return load_sound_file(response_json.filepath);
      }
    });
  };
  
  //submit = function() {
  //    var form;
  //    form = document.getElementById("user_input");
  //    console.log(form);
  //    return form.submit();
  //};
  
  $('#record_button').click(function() {
  	if (recording) {
  	  recording = false;
  	  return record();
  	} else {
  	  recording = true;
  	  return stop();
  	}
  });

  $('#play_button').click(function() {
    return play();
  });

  $('#stop_button').click(function() {
    return stop();
  });

  $('#upload_button').click(function() {
    return upload();
  });
  
  //$('#submit_button').click(function() {
  //  return submit();
  //}
  //);

  file_input = document.querySelector('input[type="file"]');
  
  //file_input.addEventListener('change', function(e) {
  //  var reader;
  //  reader = new FileReader();
  //  reader.onload = function(e) {
  //    window.n_channels = 2;
  //    return init_sound(this.result);
  //  };
  //  return reader.readAsArrayBuffer(this.files[0]);
  //}, false);
  
  $('#play_reversed').click(function() {
    stop_sound;
    return play_reversed();
  });

  $('#stop_sound').click(function() {
    return stop_sound();
  });
  
}).call(this);
