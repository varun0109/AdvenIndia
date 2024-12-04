let suggestions = [
   "shirt",
   "green",
   "Tez",
   "Garam",
   "Ginger",
   "Ginger powder",
   "Ginger ale",
   "Ginger tea",
   "Walnut",
   "floral",
   "flower",
   "flow",
   "flowering",
   "How",
  "Solar",
  "solar"
];

  const searchWrapper= document.querySelector('.search-wrapper');
  const inputBox =searchWrapper.querySelector('input');
  const suggBox = searchWrapper.querySelector(".autocom-box1");
  const icon = searchWrapper.querySelector(".icon");
  let submitbt = searchWrapper.querySelector("#submitform");
  let webLink;

  let userData="mm";
  inputBox.onkeyup = (e)=>{
    let userData = e.target.value; //user enetered data
    let emptyArray = [];
    if(userData){
        icon.onclick = ()=>{
            inputBox.value = userData;
           //webLink = `https://www.google.com/search?q=${userData}`;
           //fill userdata in input box
           
           //submitbt.setAttribute("href", webLink);
           document.getElementById('submitform').submit();
           //submitbt.click();
        }
        emptyArray = suggestions.filter((data)=>{
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            // passing return data inside li tag
            return data = `<li>${data}</li>`;
        }); 
         
        searchWrapper.classList.add("active"); //show autocomplete box
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "select(this)");
        }
    }else{
        searchWrapper.classList.remove("active"); //hide autocomplete box
    }
}  // end 

function select(element){
    let selectData = element.textContent;
    inputBox.value = selectData;
    
        //webLink = `https://www.google.com/search?q=${selectData}`;
        //submitbt.setAttribute("href", webLink);
       // submitbt.click();
       document.getElementById('submitform').submit();
    
    searchWrapper.classList.remove("active");
}
function showSuggestions(list){
    let listData;
    if(!list.length){
        userValue = inputBox.value;
        listData = `<li>${userValue}</li>`;
    }else{
      listData = list.join('');
    }
    suggBox.innerHTML = listData;
}
