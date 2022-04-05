
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
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
    var morning_row = document.getElementById("morning")
    var noon_row = document.getElementById("noon")
    var evening_row = document.getElementById("evening")

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
              get_this_week();
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
              get_this_week();
            })
    }


    const monthlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    var d = new Date();

    //To Do ** Make Update or Fetch method here to get current values for this.

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
        appoinment_add_button(value,index+1)
        add_info_appoinment_offday(value)
        dayslist[index].innerHTML = current_date.getDate()	
        }
    }
    function clear_content_of_calendar(){
      for (let i = 1; i < 8; i++) { 
        morning_row.children[i].style.backgroundColor = null;
        noon_row.children[i].style.backgroundColor = null;
        evening_row.children[i].style.backgroundColor = null;
      }
    }
    function appoinment_add_button(current_date,i){
        morning_row.children[i].innerHTML = '<button onclick="add_appoinment(\''+current_date+'\',\'MO\')">AL</button>';
        noon_row.children[i].innerHTML = '<button onclick="add_appoinment(\''+current_date+'\',\'NO\')">AL</button>';
        evening_row.children[i].innerHTML = '<button onclick="add_appoinment(\''+current_date+'\',\'EV\')">AL</button>';
    }

    function add_appoinment(date_app,time_app){
        var data = {
            app_date: date_app,
            app_time: time_app,
            app_add: true,
            csrfmiddlewaretoken: csrftoken,
          }
          $.ajax({
            url: '/appoinment/add/',
            type: 'POST',
            dataType: 'json',
            data: data
          }).done(function(response) {
              console.log("success") 
              get_week_data();
              change_values();
              console.log("finished fetching")
            })
        
    }

    function add_info_appoinment_offday(day_to_fill){
        console.log("start")
        console.log(week_entry[day_to_fill])
        var dt = new Date(day_to_fill)
        console.log(day_to_fill)
        console.log(dt.getDay())
        var day_of_week = (((dt.getDay() +6) % 7))+1
        
        if (week_entry[day_to_fill]){
        week_entry[day_to_fill].forEach(add_to_cal);
        }
        function add_to_cal(day_slot) {
          console.log(day_of_week)

          if (day_slot.includes("OFF")){
            if (day_slot.includes("MO")){
                morning_row.children[day_of_week].innerHTML = "İZİN";
                morning_row.children[day_of_week].style.backgroundColor = 'blue';
            }
            else if (day_slot.includes("NO")){
              noon_row.children[day_of_week].innerHTML = "İZİN";
              noon_row.children[day_of_week].style.backgroundColor = 'blue';
            }
            else if (day_slot.includes("EV")){
              evening_row.children[day_of_week].innerHTML = "İZİN";
              evening_row.children[day_of_week].style.backgroundColor = 'blue';

            }
            else if (day_slot.includes("ALL")){
              morning_row.children[day_of_week].innerHTML = "İZİN";
              noon_row.children[day_of_week].innerHTML = "İZİN";
              evening_row.children[day_of_week].innerHTML = "İZİN";
              morning_row.children[day_of_week].style.backgroundColor = 'blue';
              noon_row.children[day_of_week].style.backgroundColor = 'blue';
              evening_row.children[day_of_week].style.backgroundColor = 'blue';


            }
          }
          else {
            if (day_slot.includes("MO")){
              morning_row.children[day_of_week].innerHTML = "DOLU";
              morning_row.children[day_of_week].style.backgroundColor = 'red';

            }
            else if (day_slot.includes("NO")){
              noon_row.children[day_of_week].innerHTML = "DOLU";
              noon_row.children[day_of_week].style.backgroundColor = 'red';

            }
            else if (day_slot.includes("EV")){
              evening_row.children[day_of_week].innerHTML = "DOLU";
              evening_row.children[day_of_week].style.backgroundColor = 'red';

            }
          } 
        }
        
        console.log("end")


    }