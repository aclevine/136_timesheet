$(function () {
    var calendar = document.getElementById('calendar'),
        table = document.createElement('table');
    table.id = 'table'
    // Pad a number with leading zeros (or an arbitrary string)
    function pad(n, width, z) {
      var z = z || '0';
      var n = n + '';
      return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
    }
    
    // Format an integer as HH:00
    function getHour(number) {
        return pad(number, 2) + ":00";
    }
    
    function getHumanTimeString(dateTime) {
        var dt = dateTime.value.toLocaleTimeString().split(' '),
            hms = dt[0].split(':'),
            hm = hms.slice(0,2).join(':'),
            apm = dt[1];
        return [hm, apm].join(' ');
    }
    
    // Constants for time arithmetic
    var millisecond = 1,
        second = 1000 * millisecond,
        minute = 60 * second,
        hour = 60 * minute,
        day = 24 * hour,
        week = 7 * day;
    
    // A DateTime object that is a little more versatile than the built-in Date
    function DateTime() {
        this.value = new Date();
        this.toString = function() {
            return this.value.toLocaleString();
        };
        this.set = function(dt) {
            this.value.setTime(dt.getTime());
            return this;
        };
        this.year = function() {                 // [0000-9999]
            return this.value.getFullYear();
        };
        this.month = function() {                // [0-11]
            return this.value.getMonth();
        };
        this.day = function() {                  // [1-31]
            return this.value.getDate();
        };
        this.hour = function() {                 // [0-23]
            return this.value.getHours();
        };
        this.minute = function() {               // [0-59]
            return this.value.getMinutes();
        };
        this.second = function() {               // [0-59]
            return this.value.getSeconds();
        };
        this.millisecond = function() {           // [0-999]
            return this.value.getMilliseconds();
        };
        this.weekday = function() {              // [0-6]
            return this.value.getDay();
        };
        this.date = function() {                 // YYYY-MM-DD
            return [this.year(), this.month() + 1, this.day()].join('-');
        };
        this.time = function() {                 // HH:MM:SS
            return [this.hour(), this.minute(), this.second()].join(':');
        }
        this.move = function(delta) {
            this.value.setTime(this.value.getTime() + delta);
            return this;
        };
        this.next = function(unit) {
            if (typeof(unit) !== 'undefined' && unit > 0) {
                this.move(unit);
            } else {
                this.move(+day);
            };
            return this;
        };
        this.previous = function(unit) {
            if (typeof(unit) !== 'undefined' && unit > 0) {
                this.move(-unit);
            } else {
                this.move(-day);
            };
            return this;
        };
    }
    
    // Return a DateTime that is midnight (12:00:00 AM) on the day of dateTime
    // Default is 12:00:00 AM today
    function getDayStart(dateTime) {
        var start = new DateTime();
        if (typeof(dateTime) !== 'undefined') {
            start.set(dateTime.value);
        };
        start.value.setHours(0);
        start.value.setMinutes(0);
        start.value.setSeconds(0);
        start.value.setMilliseconds(0);
        return start;
    }
    
    // Return a DateTime that is midnight (12:00:00 AM) on the first day of the 
    // the week containing dateTime if specified
    // Default is 12:00:00 AM on Sunday of this week
    function getWeekStart(dateTime) {
        var start = new DateTime();
        if (typeof(dateTime) !== 'undefined') {
            start.set(dateTime.value);
        };
        while (start.weekday() !== 0) {
            start.previous();
        };
        return getDayStart(start);
    }
    
    // Create an array of 7 DateTimes [Sun,Mon,Tue,Wed,Thu,Fri,Sat]
    // The week contains the given dateTime if specified
    // Default is this week
    function Week(dateTime) {
        var date = new DateTime();
        if (typeof(dateTime) !== 'undefined'){
            date.set(dateTime.value);
        };
        this.days = [getWeekStart(date)];
        for (var i = 1; i < 7; i++) {
            this.days.push(getWeekStart(date).next((i) * day));
        }
        this.toString = function() {
            return '[ ' + this.days.join(',\n  ') + ' ]';
        };
    }
    
    // Some convenient DateTime and Week objects
    var now = new DateTime(),
        today = getDayStart(now),
        tomorrow = getDayStart(new DateTime().next(day)),
        yesterday = getDayStart(new DateTime().previous(day)),
        nextHour = new DateTime().next(hour),
        lastHour = new DateTime().previous(hour),
        thisWeek = new Week(),
        nextWeek = new Week(new DateTime().next(week)),
        lastWeek = new Week(new DateTime().previous(week));
    
    (function tableCreate() {
        var time = getDayStart(new DateTime()).previous(hour);
        // 2014-11-29T8:0:0Z/2014-11-29T17:0:0Z
        
        // Get Begin and End Time
        //var startTime = '10:05:00';
        //var endTime = '12:05:00';
          
        //start = startTime.split(":");
        //end   = startTime.split(":");
        //  
        //// Get Hour            
        //start    = parseInt(start[0]);
        //end      = parseInt(end[0]);
        
        //if(start > end) {
        //    var temp  = start;
        //        start = end;
        //        end   = temp;
        //}
        
        // Draw Table
        for(var i = 0; i < 25; i++){
            var tr = table.insertRow();
            for(var j = 0; j < 2; j++){
                var td = tr.insertCell();
                // HeadCell Color
                if (i == 0 || j == 0) {
                    td.style.backgroundColor = '#c3dde0';
                }
                // Current Date in TableHead
                if ( i == 0 && j == 1) {
                    td.appendChild(
                        document.createTextNode(time.value.toLocaleDateString())
                    );
                }
                // Hours
                if (i > 0 && j == 0) {
                    td.appendChild(
                        document.createTextNode(getHumanTimeString(time))
                    );
                }
                if (i == now.hour()+1 && j == 0) {
                    td.style.backgroundColor = 'Red'
                }
                // Filling   
                //if(i > start && i-1 <= end && j == 1 ) {
                //    td.style.backgroundColor = '#33cc66';
                //}
            }
            time.next(hour);
        }
        
        // Append the table to page contents
        calendar.appendChild(table);
    })();
    
    colorize = function(start, end, color) {
            trs = table.firstElementChild.children;
        for (var i = start+1; i <= end; i++) {
            trs[i].style.backgroundColor = color
        }
        return false;
    }
    
    fillHours = function() {
        var interval = document.getElementById('interval').value,
            start = parseInt(interval.split('/')[0].split('T')[1].split(':')[0]),
            end = parseInt(interval.split('/')[1].split('T')[1].split(':')[0]);
        return colorize(start, end, 'LightGreen');
    }
})