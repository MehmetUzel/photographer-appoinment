function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
    
    const csrftoken = getCookie('csrftoken')

    var req_data = {
        csrfmiddlewaretoken: csrftoken,
    }

    var current = -1
    var month = 0
    var data 
    var week_entry 
    var has_appo
    var user_apdate
    var user_aptime
    var user_name
    var morning_row = document.getElementById("morning")
    var noon_row = document.getElementById("noon")
    var evening_row = document.getElementById("evening")
    var today = Date.now();

    $(document).ready(function(){
        get_data();
    });

    function get_data(){
        $.ajax({
            url: '/appoinment/data/',
            type: 'POST',
            dataType: 'json',
            data: req_data
          }).done(function(response) {
              data = response.data
              week_entry = response.week
              has_appo = response.has_app
              if (has_appo == true){
                get_data_user();
              }
              else{
                get_this_week();
              }
            })
    }

    function get_week_data(){
        $.ajax({
            url: '/appoinment/data/week',
            type: 'POST',
            dataType: 'json',
            data: req_data
          }).done(function(response) {
              week_entry = response.week
              has_appo = response.has_app
              if (has_appo == true){
                get_data_user();
              }
              else{
                get_this_week();
              }
            })
    }

    function get_data_user(){
      $.ajax({
          url: '/appoinment/users/data/',
          type: 'POST',
          dataType: 'json',
          data: req_data
        }).done(function(response) {
            user_apdate = response.user_app_date
            user_aptime = response.user_app_time
            user_name = response.user_name
            get_this_week();
          })
  }


  const monthlist = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];

    var d = new Date();

    function get_this_week(){
        if (current == -1){
            current = 0
        }
        change_values();
    }

    function next(){
        current += 1
        
        if (current == data[month].length) {
            month += 1
            current = 0
            if (month == data.length){
                month = 0
            }
        }
        change_values()
    }
    function previous(){
        current -= 1
        if (current <= -1) {
            month -= 1
            if (month <= -1){
                month = data.length-1
                current = data[month].length-1
            }
            else{
            current = data[month].length-1
            }
        }
        change_values()
    }

    function change_values(){
        clear_content_of_calendar()

        var d = new Date(data[month][current][3])
        var monthtext = monthlist[d.getMonth()];
        document.getElementById("monthl").innerHTML = monthtext + " "+d.getFullYear();
        document.getElementById("months").innerHTML = monthtext + " "+d.getFullYear();


        var monhml = `<h3>${monthtext}</h3>`

        var dayslist = document.getElementsByClassName("day");

        data[month][current].forEach(myFunction);

        function myFunction(value, index, arr) {
        var current_date = new Date(value)
        if (has_appo == false && today < current_date){
          appoinment_add_button(value,index+1);
        }
        add_info_appoinment_offday(value)
        if(value == user_apdate){
        show_users_appoinment(value,user_aptime,user_name)
        }
        dayslist[index].innerHTML = current_date.getDate()	
        }
    }
    function clear_content_of_calendar(){
      for (let i = 1; i < 8; i++) { 
        morning_row.children[i].style.backgroundColor = null;
        noon_row.children[i].style.backgroundColor = null;
        evening_row.children[i].style.backgroundColor = null;
        morning_row.children[i].innerHTML = null;
        noon_row.children[i].innerHTML = null;
        evening_row.children[i].innerHTML = null;
      }
    }
    function appoinment_add_button(current_date,i){
        morning_row.children[i].innerHTML = '<button onclick="add_appoinment(\''+current_date+'\',\'MO\')">AL</button>';
        noon_row.children[i].innerHTML = '<button onclick="add_appoinment(\''+current_date+'\',\'NO\')">AL</button>';
        evening_row.children[i].innerHTML = '<button onclick="add_appoinment(\''+current_date+'\',\'EV\')">AL</button>';
    }

    function add_appoinment(date_app,time_app,is_add = true){
      var data = {
          app_date: date_app,
          app_time: time_app,
          app_add: is_add,
          csrfmiddlewaretoken: csrftoken,
        }
        $.ajax({
          url: '/appoinment/add/',
          type: 'POST',
          dataType: 'json',
          data: data
        }).done(function(response) {
            get_week_data();
            get_data_user();
            change_values();
          })
  }


    function prepare_app_deletion_html(date_to_delete, time_to_delete,user){
      return '<div style="text-align: center;"><p>DOLU<br>'+ user +'</p><div style="display: flex; justify-content: space-evenly;"><button class="btn-close" aria-label="Close" onclick="add_appoinment(\''+date_to_delete+'\',\''+time_to_delete+'\',false)"></button></div></div>';
    }

    function add_info_appoinment_offday(day_to_fill){
        var dt = new Date(day_to_fill)
        var day_of_week = (((dt.getDay() +6) % 7))+1 //To change starting of week as monday - getDay method assumes sunday as first day of week
        
        if (week_entry[day_to_fill]){
        week_entry[day_to_fill].forEach(add_to_cal);
        }
        function add_to_cal(day_slot) {

          colorize_week_slots(day_of_week, "DOLU", "red",day_slot) 
        }
        
    }

    function colorize_week_slots(day_of_week, text_of_slot, color_of_slot,day_slot){
      if (day_slot.includes("MO")){
        morning_row.children[day_of_week].innerHTML =  text_of_slot;
        morning_row.children[day_of_week].style.backgroundColor = color_of_slot;
      }
      else if (day_slot.includes("NO")){
        noon_row.children[day_of_week].innerHTML =  text_of_slot;
        noon_row.children[day_of_week].style.backgroundColor = color_of_slot;
      }
      else if (day_slot.includes("EV")){
        evening_row.children[day_of_week].innerHTML =  text_of_slot;
        evening_row.children[day_of_week].style.backgroundColor = color_of_slot;
      }
    }

    function show_users_appoinment(date_of_app,slot,name){
      var dt = new Date(date_of_app)
      var day_of_week = (((dt.getDay() +6) % 7))+1
      if (slot.includes("MO")){
        morning_row.children[day_of_week].innerHTML = prepare_app_deletion_html(date_of_app, "MO",name.substr(0, name.indexOf("@")));
        morning_row.children[day_of_week].style.backgroundColor = 'red';

      }
      else if (slot.includes("NO")){
        noon_row.children[day_of_week].innerHTML = prepare_app_deletion_html(date_of_app, "NO",name.substr(0, name.indexOf("@")));
        noon_row.children[day_of_week].style.backgroundColor = 'red';

      }
      else if (slot.includes("EV")){
        evening_row.children[day_of_week].innerHTML = prepare_app_deletion_html(date_of_app, "EV",name.substr(0, name.indexOf("@")));
        evening_row.children[day_of_week].style.backgroundColor = 'red';

      }
    }